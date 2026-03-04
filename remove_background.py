import streamlit as st
import os
from PIL import Image
from rembg import remove

st.title("AI Background Remover")

uploaded_file = st.file_uploader("Upload an Image")

if uploaded_file :
    #  Open the input image
    img = Image.open(uploaded_file)
    # Subheader for original image
    st.subheader("Original Image")

    st.image(img, width="stretch")

    if st.button("Remove Background"):
        with st.spinner("Removing Background.....Please Wait !!"):
            output = remove(img)
        # Subheader for Back_ground removed image
        st.subheader("Background Removed")

        st.image(output)
