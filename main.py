import streamlit as st
from PIL import Image
st.header("Digi o KYC")
st.subheader("Digi sign is used for signing the document")
st.markdown("Intelligent airline planning. Cirium Diio™ provides complete end-to-end schedule and route planning. With Diio, track flight schedules by airlines")
st.text("Hello I am Text")
name= st.text_input("Enter your name")
st.write("I am **just** and **_writing_**") #in st.write we can make bold text by double strict

dc= {"a":10, "b":20, "c":30}
st.write(dc)