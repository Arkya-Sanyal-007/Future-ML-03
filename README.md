# 🛒 ShopSmart – E-commerce Chatbot (Streamlit + Dialogflow)

A user-friendly and modern chatbot UI built using Streamlit and Dialogflow Messenger. This app provides automated support for e-commerce customers.

---

## 💡 Features

- 🤖 Dialogflow CX integration for intelligent conversation  
- 💬 Real-time chat interface using Streamlit
- 🖤 Dark mode layout for better UI/UX  
- 🧠 Responds to custom intents from your own Dialogflow agent
- 🌐 Deployable to Streamlit Cloud or local server

---

## 📁 Folder Structure

```bash
Shopsmart_Chatbot/
│
├── app.py                  # Streamlit app
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

---

## 📸 Preview

<div align="center">

    ![ShopSmart Demo](https://github.com/Arkya-Sanyal-007/Future-ML-03/assets/your-image-demo-link.gif)
</div>

---

## 🚀 Getting Started

### 🧩 Prerequisites

- Python 3.8+
- A Dialogflow CX Agent
- `agent-id` of your Dialogflow CX bot (from Dialogflow Console)

---

### 🛠️ Setup Instructions

1. Clone this repository:
    ```bash
    git clone https://github.com/Arkya-Sanyal-007/Shopsmart_Chatbot.git
    cd Shopsmart_Chatbot
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```
    
---

# 🧠 Dialogflow Integration

In your app.py, replace the agent-id with your actual Dialogflow CX agent ID:

```bash
html
Copy
Edit
<df-messenger
  intent="WELCOME"
  chat-title="ShopSmart Assistant"
  agent-id="YOUR_AGENT_ID_HERE"          # Replace this with your actual agent_ID
  language-code="en">
</df-messenger>
```

---

# 💡 Use Cases:

- 🛍️ Order status inquiries
- 🔁 Return/refund process guidance
- 📦 Delivery time/status updates
- 🧾 Invoice and billing queries
- 🧠 General product support

---

# 🙋‍♂️ Author

Made with ❤️ by Arkya Sanyal
📧 Email: arkyasanyal03@gmail.com

---

# ⭐ Support

If you like this project, give it a ⭐ and share it with your peers!
Feel free to fork the repo, suggest improvements, or submit PRs. 
PRs and suggestions are always welcome 🙌

---

# 📄 License

This project is licensed under the MIT License.
Feel free to use, modify, and share!
