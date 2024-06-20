import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
#from src.key import GOOGLE_API_KEY

# Initialize the model with your API key
llm = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key = st.secrets["GOOGLE_API_KEY"])

def chat(input_text):
    # Invoke the model with user input
    result = llm.invoke(input_text)
    return result.content

# Streamlit UI
st.title("Gemini Chat Model")
st.write("Type 'exit' to end the conversation.")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# User input
user_input = st.text_input("You:", key="user_input")

if st.button("Send"):
    if user_input.lower() == 'exit':
        st.session_state.chat_history.append(("You", "Goodbye!"))
        st.session_state.chat_history.append(("Gemini", "Bye!"))
    else:
        response = chat(user_input)
        st.session_state.chat_history.append(("You", user_input))
        st.session_state.chat_history.append(("Gemini", response))

# Display chat history
for speaker, message in st.session_state.chat_history:
    st.write(f"**{speaker}:** {message}")
