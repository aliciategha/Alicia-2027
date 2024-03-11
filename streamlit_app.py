import streamlit as st 
st.write("Hello") 
name=st.text_input("Your name") 
st.write("Hello" + name )
genre = st.radio(
    "chien/chat",
    [":chien", "chat:"],
