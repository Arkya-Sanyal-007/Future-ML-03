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

### 🧩 Requirements

- Python 3.8+
- A Dialogflow CX Agent
- `agent-id` of your Dialogflow CX bot (from Dialogflow Console)

---

### 🛠️ Setup Instructions

```bash
# 1. Clone the repo
git clone https://github.com/Arkya-Sanyal-007/Shopsmart_Chatbot.git
cd Shopsmart_Chatbot

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the Streamlit app
streamlit run app.py

# 4. Deploy
Once the app is running, it will open in your browser at http://localhost:8501.
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

-🛍️ Order status inquiries
-🔁 Return/refund process guidance
-📦 Delivery time/status updates
-🧾 Invoice and billing queries
-🧠 General product support

---

# 🙋‍♂️ Author

Made with ❤️ by Arkya Sanyal
📧 Email: arkyasanyal03@gmail.com

---

# 📄 License

This project is licensed under the MIT License.
Feel free to use, modify, and share!

---

# ⭐ Support
If you like this project, give it a ⭐ and share it with your peers!
PRs and suggestions are always welcome 🙌