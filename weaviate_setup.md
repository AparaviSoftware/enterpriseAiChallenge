# 🚀 How to Set Up a Weaviate Sandbox & Get Your API Key

Weaviate is a powerful **vector database** that allows for **semantic search** and **retrieval-augmented generation (RAG)** for AI applications. Follow this guide to **create a Weaviate sandbox**, deploy it, and obtain your **endpoint URL & API key**.

---

## 📌 Step 1: Sign Up for Weaviate Cloud
1. **Go to the Weaviate Cloud Console:**
   👉 [https://console.weaviate.io/](https://console.weaviate.io/)
2. **Click on "Sign Up"**
   - You can use **Google, GitHub, or Email** to create an account.
3. **Verify Your Email**
   - Check your inbox and click the verification link.

---

## 📌 Step 2: Create a Free Sandbox Cluster
1. Once logged in, click **"Create Cluster"**.
2. Select **"Free Tier (Sandbox)"**.
3. Choose a **Region** closest to you (e.g., US-West, Europe).
4. Click **"Deploy"** – Your cluster will start provisioning.
5. **Wait a few minutes** for the deployment to complete.

---

## 📌 Step 3: Get Your Weaviate Endpoint URL
1. Once your cluster is ready, go to **"Cluster Details"**.
2. You will see your **Weaviate URL**, which looks like: `https://your-instance.weaviate.cloud`
3. Copy this URL – you’ll need it to connect your chatbot.

---

## 📌 Step 4: Obtain Your API Key
1. Inside the **Cluster Details** page, scroll down to **"API Key"**.
2. Click **"Generate API Key"** (if you haven’t already).
3. Copy the API key – you’ll need it for authentication.

---

## 📌 Step 5: Update Your `config.json` File
Once you have your **Weaviate URL** and **API key**, update your `config.json` file:

```json
{
  "weaviate_url": "https://your-instance.weaviate.cloud",
  "weaviate_api_key": "your-api-key"
}
```

---

## 📌 Step 6: Verify Your Weaviate Connection

Run this Python script to check if Weaviate is properly set up:

```python
import weaviate
from weaviate.classes.init import Auth

weaviate_client = weaviate.connect_to_weaviate_cloud(
    cluster_url="https://your-instance.weaviate.cloud",
    auth_credentials=Auth.api_key("your-api-key"),
)

if weaviate_client.is_ready():
    print("✅ Weaviate is successfully connected!")
else:
    print("❌ Connection failed. Check your API key and URL.")
```

---

## 📌 Step 7: Start Using Weaviate!

Now that your sandbox is deployed and your API key is configured, you’re ready to:
- ✅ Store embeddings for AI chatbots
- ✅ Perform fast semantic search
- ✅ Integrate Weaviate with LangChain, OpenAI, and Hugging Face

---

### 📺 Bonus: Watch a Video Tutorial

🎥 Want a visual walkthrough? Check out this YouTube guide:
👉 [Weaviate Cloud Setup Tutorial](#) (Replace with actual link)

---

### 🎯 Next Steps

- 🔹 Sign up & deploy your Weaviate instance
- 🔹 Copy your API key & update `config.json`
- 🔹 Run a test query to verify your setup
- 🔹 Start integrating Weaviate into your AI projects! 🚀