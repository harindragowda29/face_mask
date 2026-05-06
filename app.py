
import streamlit as st
import numpy as np
from PIL import Image
import random

st.set_page_config(page_title="Face Mask Detection")

st.title("😷 Face Mask Detection App (Demo)")

uploaded_file = st.file_uploader("Upload Image", type=["jpg","png","jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, width=300)

    # Fake prediction (for demo)
    label = random.choice(["✅ Mask", "❌ No Mask"])
    confidence = random.uniform(0.7, 0.99)

    st.subheader(label)
    st.progress(int(confidence * 100))
    st.write(f"Confidence: {confidence*100:.2f}%")

