import streamlit as st
import streamlit.components.v1 as components

# Set page config
st.set_page_config(page_title="🛍️ ShopSmart – Chatbot Assistant", layout="centered")

# Title and intro
st.title("🛍️ ShopSmart – E-commerce Chatbot")
st.markdown("""
Welcome to **ShopSmart's virtual assistant** 🤖  
Ask me anything about your **orders, payments, refunds, returns, or shipping**! 📦💳  
Start chatting below ⬇️
""")

# Embed Dialogflow Messenger Widget (CX)
components.html(
    """
    <script src="https://www.gstatic.com/dialogflow-console/fast/messenger/bootstrap.js?v=1"></script>
    <df-messenger
      intent="WELCOME"
      chat-title="ShopSmart Assistant"
      agent-id="05ecc3e6-d0b3-4061-a3e8-b983bfe9b36f"  
      language-code="en">
    </df-messenger>
    """,
    height=600,
)

