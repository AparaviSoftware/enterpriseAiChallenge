# 🤖 How to Get Your OpenAI API Key & Use It for Generative AI

OpenAI provides **powerful AI models** such as GPT-4o, which can be used for **chatbots, text generation, and AI-driven enterprise applications**. This guide will walk you through how to:
✅ **Create an OpenAI account & get an API key**
✅ **Configure the API key for your project**
✅ **Understand and optimize key GenAI parameters**

---

## 📌 Step 1: Sign Up for OpenAI & Get Your API Key

### 🔹 **Create an OpenAI Account**
1. **Go to OpenAI’s website:**
   👉 [https://platform.openai.com/signup](https://platform.openai.com/signup)
2. **Sign up using Email, Google, or Microsoft**.
3. **Verify your email and log in** to your OpenAI account.

### 🔹 **Obtain Your API Key**
1. **Go to API Keys Settings:**
   👉 [https://platform.openai.com/api-keys](https://platform.openai.com/api-keys)
2. Click **“Create API Key”**.
3. **Copy the key and store it securely** – OpenAI will only show it **once**.

🔹 **Update your `config.json` file with the API key:**
```json
{
  "openai_api_key": "your-api-key"
}
```

---

## 📌 Step 2: Install OpenAI’s Python Package

Before using the API, install OpenAI’s Python SDK:

```bash
pip install openai
```

---

## 📌 Step 3: Test Your OpenAI API Key

Run this Python script to verify that your API key is working:

```python
import openai

# Load your OpenAI API key
api_key = "your-api-key"

# Send a test query to OpenAI
response = openai.ChatCompletion.create(
    model="gpt-4o",
    messages=[{"role": "system", "content": "Say hello!"}],
    temperature=0.7,
    max_tokens=50
)

print(response["choices"][0]["message"]["content"])
```

If everything is set up correctly, the output should be:

    "Hello!" ✅

---

## 📌 Step 4: Understanding OpenAI Model Parameters

In the PixelProofy AI chatbot, the following parameters are used to fine-tune responses and ensure AI reliability.
🔹 Configuration Parameters (config.json)

```json
{
  "openai_api_key"  : "<your-openai-api-key>",
  "openai_model"    : "gpt-4o",
  "system_prompt"   : "You are PixelProofy’s AI assistant, specializing in answering enterprise-related questions using the most relevant retrieved context. Your goal is to provide precise, well-structured, and professional responses based on the available context. If the provided context is insufficient, acknowledge it and avoid making assumptions. Always prioritize accuracy, clarity, and security when responding to sensitive topics.",
  "user_prompt"     : "You are answering as PixelProofy's AI Assistant. Use the retrieved context to generate an accurate response. If the context does not contain relevant information, state that explicitly rather than making assumptions.\n\nContext:\n{context}\n\nUser Question:\n{message}\n\nChat History:\n{history}\n\n---\nEnsure responses are concise yet informative, maintaining a professional tone. Cite sources from the provided context when applicable.",
  "temperature"     : 0.7,
  "max_tokens"      : 1000
}
```

🔹 Explaining Each Parameter

| Parameter         | Description                                                                 |
|-------------------|-----------------------------------------------------------------------------|
| openai_api_key    | Your OpenAI API key for authentication.                                      |
| openai_model      | Defines which OpenAI model to use (e.g., "gpt-4o", "gpt-3.5-turbo").       |
| system_prompt     | The base instruction given to the AI, defining its role (e.g., enterprise assistant). |
| user_prompt       | The prompt template used to structure user interactions, ensuring relevant responses. |
| temperature       | Controls randomness of responses (🔹 Lower = more predictable, Higher = more creative). |
| max_tokens        | Limits response length (1000 tokens ≈ 750 words).                            |

---

## 📌 Step 5: Adjusting AI Behavior with Parameters

🎯 1. Choosing the Right Model (openai_model)

| Model         | Best For                                | Cost        |
|---------------|-----------------------------------------|-------------|
| gpt-4o        | Best for reasoning & enterprise chatbots | Higher cost |
| gpt-3.5-turbo | Faster & cheaper, good for general-purpose chatbots | Lower cost  |

📝 Example: Switch models in config.json:

```json
{
  "openai_model": "gpt-3.5-turbo"
}
```

🎯 2. Controlling Creativity (temperature)

| Value   | Effect                                                                  |
|---------|-------------------------------------------------------------------------|
| 0.0 – 0.3 | Strict & precise (Great for enterprise FAQs, structured answers).     |
| 0.4 – 0.7 | Balanced (Good for natural, engaging responses).                      |
| 0.8 – 1.0 | Creative & unpredictable (Best for brainstorming).                    |

📝 Example: Adjust temperature in config.json:

```json
{
  "temperature": 0.3
}
```

🎯 3. Controlling Response Length (max_tokens)

| Value | Use Case                            |
|-------|-------------------------------------|
| 500   | Shorter responses (concise answers).|
| 1000  | Medium-length responses (detailed but controlled). |
| 2000+ | Long-form content generation.       |

📝 Example: Adjust token limit in config.json:

```json
{
  "max_tokens": 500
}
```

---

## 📌 Step 6: Making an API Call with Context

Here’s how PixelProofy uses retrieved context to improve responses:

```python
import openai

api_key = "your-api-key"

messages = [
    {"role": "system", "content": "You are PixelProofy’s AI assistant, specializing in enterprise AI support."},
    {"role": "user", "content": "What is our deepfake detection accuracy?"}
]

response = openai.ChatCompletion.create(
    model="gpt-4o",
    messages=messages,
    temperature=0.7,
    max_tokens=1000
)

print(response["choices"][0]["message"]["content"])
```
