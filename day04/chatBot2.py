import ollama 
import streamlit as st 
st.markdown("Welcome to my ChatBot App!!!")
with st.sidebar:
    st.header(":blue[chat settings]")
    if st.button("[Clear chat 🗑️]"):
        if "messages" not in st.session_state:
            st.session_state.messages = []
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])
question = st.chat_input("You:")
if question:
    st.session_state.messages.append(
            {"role" : "user",
            "content" : question}
        )
    with st.chat_message("user"):
        st.write(question)
with st.spinner("Thinking..."):
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