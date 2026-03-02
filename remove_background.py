import streamlit as st
import os
from PIL import Image
from rembg import remove

st.title("AI Background Remover")

uploaded_file = st.file_uploader("Upload an Image")

if uploaded_file :
    img = Image.open(uploaded_file)

    st.subheader("Original Image")

    st.image(img, use_container_width=True)

    if st.button("Remove Background"):
        with st.spinner("Removing Background.....Please Wait !!"):
            output = remove(img)

        st.subheader("Background Removed")

        st.image(output)