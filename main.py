from openai import OpenAI
from dotenv import load_dotenv
import streamlit as st
import os

# Load environment variables from .env file
load_dotenv()

# Get the NVIDIA API key from the environment variable
nvidia_api_key = os.getenv("NVIDIA_API_KEY")
if not nvidia_api_key:
    st.error("NVIDIA_API_KEY environment variable not found. Please set it in the .env file.")
    st.stop()

# Initialize OpenAI client
client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key=nvidia_api_key,
)

# Define the chat function
def chatter(user_input):
    completion = client.chat.completions.create(
        model="meta/llama3-70b",
        messages=[
            {
                "role": "user",
                "content": user_input,
            }
        ],
        temperature=1,
        top_p=1,
        max_tokens=1024,
        stream=False,
    )
    return completion.choices[0].message.content

# Set the page title
st.set_page_config(page_title="Your Favorite Chatbot")

# Display the title
st.title("Your Favorite Chatbot")

# Get user input
query = st.text_input("Enter your message", "How are you?")

# When the user clicks the Submit button
if st.button("Submit"):
    if query:
        output = chatter(query)
        st.write(output)
