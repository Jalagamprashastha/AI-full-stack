import ollama 
import streamlit as st 
st.title("Welcome to my ChatBot App!!!")
if "messages" not in st.session_state:
    st.session_state.messages = []
question = st.chat_input("You:")
if question:
    st.session_state.messages.append(
            {"role" : "user",
            "content" : question}
        )
    with st.chat_message("user"):
        st.write(question)
    response = ollama.chat(
            model = "llama3.2:3b",
            messages = st.session_state.messages
            )
    st.session_state.messages.append(
            {"role":"assistant",
            "content":response["message"]["content"]
            }
        )
    with st.chat_message("assistant"):
        st.write(response["message"]["content"])