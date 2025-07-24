# chatt.py

import streamlit as st
from chat import get_groq_response



# Streamlit page setup
st.set_page_config(page_title="Groq Chatbot 🤖", layout="centered")
st.title("Welcome to Vidhi's Chatbot (●'◡'●)")
st.markdown("Ask anything to the AI model powered by Groq's LLaMA-3")

# Text input
user_input = st.text_input("You:", placeholder="Type your message here...")

# When user types something
if user_input:
    with st.spinner("Thinking... 💬"):
        response = get_groq_response(user_input)
        if response.startswith("❌") or response.startswith("⚠️"):
            st.error(response)
        else:
            st.success(response)
