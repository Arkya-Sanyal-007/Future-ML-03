import streamlit as st

st.set_page_config(page_title="E-commerce Chatbot", layout="centered")

st.title("🛒 ShopSmart – E-commerce Chatbot")

st.markdown("""
Welcome to our support assistant! Ask about your orders, refunds, returns, and more.👇
""")

# Insert HTML code for Dialogflow Messenger widget
st.components.v1.html("""
  <script src="https://www.gstatic.com/dialogflow-console/fast/messenger/bootstrap.js?v=1"></script>
  <df-messenger
    intent="WELCOME"
    chat-title="ShopSmart Assistant"
    agent-id="05ecc3e6-d0b3-4061-a3e8-b983bfe9b36f"
    language-code="en">
  </df-messenger>
""", height=600)
