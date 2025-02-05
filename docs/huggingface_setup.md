# 🤖 How to Set Up a Hugging Face Account & Get Your API Key

Hugging Face provides **pre-trained AI models**, **embeddings**, and **datasets** that can power your AI chatbot. This guide will show you how to **create an account, generate an API key, and configure it for your project**.

---

## 📌 Step 1: Sign Up for a Hugging Face Account
1. **Go to the Hugging Face website:**  
   👉 [https://huggingface.co/join](https://huggingface.co/join)  
2. **Choose a sign-up method**:  
   - You can register using **email, GitHub, or Google**.  
3. **Verify your email** and log in to your Hugging Face account.

---

## 📌 Step 2: Generate Your API Key
1. **Navigate to the API Keys page:**  
   👉 [https://huggingface.co/settings/tokens](https://huggingface.co/settings/tokens)  
2. **Click “New Token”** to create an API key.  
3. **Give it a name** (e.g., `PixelProofyBot`).  
4. **Set permissions**: Choose **“Write”** access (recommended).  
5. **Click “Generate”** and copy the API key.

---

## 📌 Step 3: Update Your `config.json` File
Once you have your **Hugging Face API key**, update your `config.json` file:

```json
{
  "huggingface_api_key": "your-api-key"
}
```

---

## 📌 Step 4: Install Required Python Packages

To use Hugging Face embeddings, install the required Python dependencies:

```bash
pip install transformers sentence-transformers
```

---

## 📌 Step 5: Verify Your Hugging Face API Key

Run the following Python script to check if your API key works:

```python
from transformers import pipeline

# Define your API key
api_key = "your-api-key"

# Load a text generation model from Hugging Face
generator = pipeline("text-generation", model="gpt2", use_auth_token=api_key)

# Test the model
response = generator("Hello, how are you?", max_length=20)
print(response)
```

If the API key is valid, you should see a generated text response.

---

## 📌 Step 6: Using Hugging Face Embeddings

To retrieve embeddings for AI-powered search and retrieval, use Sentence-Transformers:

```python
from sentence_transformers import SentenceTransformer

# Load a pre-trained embedding model
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

# Convert text into vector embeddings
embedding = model.encode("PixelProofy AI Chatbot Challenge")
print(embedding)
```

---

## 📌 Step 7: Select an Embedding Model

Hugging Face offers various pre-trained sentence transformers for embeddings. Some recommended models:
- ✅ "sentence-transformers/all-MiniLM-L6-v2" (Fast & lightweight)
- ✅ "sentence-transformers/all-mpnet-base-v2" (Higher accuracy)
- ✅ "sentence-transformers/multi-qa-mpnet-base-dot-v1" (Optimized for Q&A retrieval)

To change the model, update your `config.json` file:

```json
{
  "model_name": "sentence-transformers/all-MiniLM-L6-v2"
}