import streamlit as st
from chatbot import predict_class, get_response, intents

st.title("🤖 MaxBot")

if "messages" not in st.session_state:
    st.session_state.messages = []  
if "first_message" not in st.session_state:
    st.session_state.first_message = True  

avatar_icon = ":material/smart_toy:"

for message in st.session_state.messages:
    with st.chat_message(message["role"], avatar=message.get("avatar")): 
        st.markdown(message["content"])  

if st.session_state.first_message:
    response_text = "Hello, how can I help you?"

    st.session_state.messages.append({"role": "MaxBot", "content": response_text, "avatar": avatar_icon})
    
    with st.chat_message("MaxBot", avatar=avatar_icon): 
        st.markdown(response_text)  
    
    st.session_state.first_message = False  

if prompt := st.chat_input("How can I help you?"):
    with st.chat_message("user"):  
        st.markdown(prompt)  
    st.session_state.messages.append({"role": "user", "content": prompt})

    insts = predict_class(prompt)
    res = get_response(insts, intents)

    with st.chat_message("MaxBot", avatar=avatar_icon):  
        st.markdown(res)  
    st.session_state.messages.append({"role": "MaxBot", "content": res, "avatar": avatar_icon})