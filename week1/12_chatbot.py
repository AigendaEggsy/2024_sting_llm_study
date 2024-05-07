# https://github.com/streamlit/docs/blob/main/python/api-examples-source/chat.llm.py
import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv() 
from openai import OpenAI
from langchain_openai import ChatOpenAI

st.title("Sting chatbot")

client = OpenAI(api_key = os.getenv('OPENAI_API_KEY'))
chat = ChatOpenAI(model_name="gpt-3.5-turbo-0125")

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

if "messages" not in st.session_state:
    st.session_state.messages = []

if "max_messages" not in st.session_state:
    # Counting both user and assistant messages, so 10 rounds of conversation
    st.session_state.max_messages = 20

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if len(st.session_state.messages) >= st.session_state.max_messages:
    st.info(
        """Notice: The maximum message limit for this demo version has been reached. We value your interest!
        We encourage you to experience further interactions by building your own application with instructions
        from Streamlit's [Build a basic LLM chat app](https://docs.streamlit.io/develop/tutorials/llms/build-conversational-apps)
        tutorial. Thank you for your understanding."""
    )

else:
    if prompt := st.chat_input("What is up?"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            try:
                stream = client.chat.completions.create(
                    model=st.session_state["openai_model"],
                    messages=[
                        {"role": m["role"], "content": m["content"]}
                        for m in st.session_state.messages
                    ],
                    stream=True,
                )
                response = st.write_stream(stream)
                st.session_state.messages.append(
                    {"role": "assistant", "content": response}
                )
            except:
                st.session_state.max_messages = len(st.session_state.messages)
                rate_limit_message = """
                    Oops! Sorry, I can't talk now. Too many people have used
                    this service recently.
                """
                st.session_state.messages.append(
                    {"role": "assistant", "content": rate_limit_message}
                )
                st.rerun()