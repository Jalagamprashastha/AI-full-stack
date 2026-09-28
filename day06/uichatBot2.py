import ollama 
import streamlit as st 
st.title(''':blue[Welcome] :yellow[to my] :green[ChatBot App]:violet[!!!]''')
with st.sidebar:
    st.header("Chat settings 🤣")
    if st.button("Clear chat🗑️"):
        st.session_state.messages = []
        st.student("chat cleared")
    personalities = {
        "kid👧" : "Answer the questions like you are explaining to a 5 year old kid. Give answer in 2 lines only.",
        "Friend🫂" : "Answer the question in a friendly and casual manner. Give in 2 lines only."    
    }
    personality = st.selectbox("Select a personality", personalities.keys())
    uploaded_file = st.file_uploader("Upload a text file....😊")
    try:
        if uploaded_file:
            st.success("File uploaded successfully!")
            context = uploaded_file.read().decode("utf-8")
            if st.button("Display"):
                st.write(context)
    except Exception as e:
        st.error("Error occurred while reading the file.")
if "messages" not in st.session_state:
    st.session_state.messages = []
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])
question = st.chat_input("Ask anything:❓")
if question:
    st.session_state.messages.append(
            {"role" : "user",
            "content" : question}
        )
    with st.chat_message("user"):
        st.write(question)
    with st.spinner("Thinking...💭"):
        response = ollama.chat(
            model = "llama3.2:3b",
            messages= [
            {"role" : "system", "content": personalities[personality]} ]
                + st.session_state.messages)
    st.session_state.messages.append(
        {"role":"assistant",
        "content":response["message"]["content"]
        })
    with st.chat_message("assistant"):
        st.write(response["message"]["content"])
        