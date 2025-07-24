import os
import google.generativeai as genai

# Configure the Gemini API Key
genai.configure(api_key=os.getenv("GROQ_API_KEY"))

# Set up the model
model = genai.GenerativeModel("gemini-pro")

def get_groq_response(user_input):
    response = model.generate_content(user_input)
    return response.text
