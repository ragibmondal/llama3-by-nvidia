Llama3 Chat App
================

A Streamlit app for conversational AI using the Llama3-70b language model from Meta.

**Dependencies**

* `streamlit` (latest)
* `openai` (latest)
* `dotenv` (latest)

**Environment Variables**

* `NVIDIA_API_KEY`: Your NVIDIA API key (required)

**Setup**

1. `pip install -r requirements.txt`
2. Create a `.env` file with your NVIDIA API key: `NVIDIA_API_KEY=YOUR_API_KEY_HERE`
3. Run the app: `streamlit run app.py`

**Code Structure**

* `app.py`: The main app file, contains the Streamlit UI and OpenAI API integration
* `requirements.txt`: Lists the dependencies required to run the app
* `.env`: Environment variables file, contains the NVIDIA API key
* `README.md`: This file, provides an overview of the app and setup instructions

**Features**

* Conversational interface with the Llama3-70b language model
* Adjustable max tokens slider to control the response length
* Model information and description
* Chat history displayed on app rerun
* Clear chat and download chat history buttons

**How to Use**

1. Run the app by executing `streamlit run app.py` in your terminal.
2. Enter your prompt in the chat input field and press Enter.
3. The app will respond with a chat response from the Llama3-70b model.
4. Adjust the max tokens slider to control the response length.
5. Use the clear chat and download chat history buttons as needed.

**Troubleshooting**

* Check the OpenAI API documentation for any rate limiting or usage guidelines.
* If you encounter any errors, please report them as an issue on this repository.

**License**
Apache-2.0 license
