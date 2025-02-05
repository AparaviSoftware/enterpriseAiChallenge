import json
import gradio as gr
from openai import OpenAI
from langchain_community.embeddings.huggingface import HuggingFaceInferenceAPIEmbeddings
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.query import MetadataQuery
import os

# Get the current directory where the script is run
current_dir = os.path.dirname(os.path.abspath(__file__))

# Load configuration from config.json in the current directory
config_path = os.path.join(current_dir, 'config.json')
with open(config_path) as config_file:
    config = json.load(config_file)

# Load LLM settings from llm_settings.json
llm_settings_path = os.path.join(current_dir, 'llm_settings.json')
with open(llm_settings_path) as llm_settings_file:
    llm_settings = json.load(llm_settings_file)

# Extract the configuration values
huggingface_api_key = config["huggingface_api_key"]
weaviate_url        = config["weaviate_url"]
weaviate_api_key    = config["weaviate_api_key"]
embedding_model     = config["embedding_model"]

# Extract LLM settings
openai_api_key  = llm_settings["openai_api_key"]
openai_model    = llm_settings["openai_model"]
system_prompt   = llm_settings["system_prompt"]
user_prompt     = llm_settings["user_prompt"]
temperature     = llm_settings["temperature"]
max_tokens      = llm_settings["max_tokens"]

# Initialize the OpenAI client
openai_client = OpenAI(api_key=openai_api_key)

# Initialize Weaviate client
weaviate_client = weaviate.connect_to_weaviate_cloud(
    cluster_url      = weaviate_url,
    auth_credentials = Auth.api_key(weaviate_api_key),
)

# Function to get available collections from Weaviate
def get_available_collections():
    try:
        weaviate_collections = weaviate_client.collections.list_all()
        return list(weaviate_collections.keys())
    except Exception as e:
        print(f"Error getting collections: {e}")
        return []

# Function to get embeddings from HuggingFace
def get_embedding(text):
    embeddings = HuggingFaceInferenceAPIEmbeddings(
        api_key    = huggingface_api_key,
        model_name = embedding_model
    )
    return embeddings.embed_query(text)

# Define the predict function
def predict(message, history, collection_names):
    if not collection_names:
        return "Please select at least one collection."
    
    try:
        # Get embedding for the query
        query_embedding = get_embedding(message)
        
        # Initialize variables for response
        all_results = []
        
        # Search each selected collection
        for collection_name in collection_names:
            
            # Get the Weaviate collection
            weaviate_collection = weaviate_client.collections.get(collection_name)
            response            = weaviate_collection.query.near_vector(
                near_vector         = query_embedding,
                limit               = 10,
                return_metadata     = MetadataQuery(distance=True)
            )
            
            if response:
                all_results.extend(response.objects)
        
        if not all_results:
            return "No relevant information found in the selected collections."

        # Extract and format content from all_results
        context = "\n".join([
            f"Content: {obj.properties.get('content', '')}\n"
            f"Parent: {obj.properties.get('parent', '')}\n"
            f"Chunk: {obj.properties.get('chunk', '')}\n"
            f"Semantic Distance: {obj.metadata.distance}\n"
            for obj in all_results
        ])
        
        # Prepare messages for OpenAI
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user",   "content": user_prompt.format(context=context, message=message, history=history)},
        ]
        
        # Get response from OpenAI
        response = openai_client.chat.completions.create(
            model=openai_model,
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens
        )
        
        return response.choices[0].message.content
        
    except Exception as e:
        return f"Error: {str(e)}"

# Define the chat interface
def chat_interface(message, collection_names, history=[]):
    return predict(message, history, collection_names)

# Gradio Interface with collection selection and chat interface
def refresh_collections():
    return gr.Dropdown(choices=get_available_collections())

with gr.Blocks() as interface:
    gr.Markdown("# Weaviate Chat with Collection Selection")
    
    with gr.Row():
        collection_dropdown = gr.Dropdown(
            choices=get_available_collections(),
            label="Select Collection(s)",
            multiselect=True
        )
        refresh_button = gr.Button("Refresh Collections")
    
    chatbot = gr.Chatbot()
    message_input = gr.Textbox(label="Type your message here")
    send_button = gr.Button("Send")
    current_collections = gr.State([])
    
    def user_interaction(message, history, collection_names, current_collections):
        if not message:
            return history, current_collections
        
        user_message = ("You", message)
        bot_message = ("Assistant", chat_interface(message, collection_names, history + [user_message]))
        history.append(user_message)
        history.append(bot_message)
        return history, current_collections
    
    send_button.click(
        user_interaction,
        inputs=[message_input, chatbot, collection_dropdown, current_collections],
        outputs=[chatbot, current_collections]
    )
    
    # Reset the chat when collections change
    collection_dropdown.change(
        lambda: ([], []),
        outputs=[chatbot, current_collections]
    )
    
    refresh_button.click(
        refresh_collections,
        outputs=[collection_dropdown]
    )

interface.launch()
