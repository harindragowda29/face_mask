
import streamlit as st
import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model

# Load model
model = load_model("mask_detector.h5")

st.set_page_config(page_title="Face Mask Detection")

st.title("😷 Face Mask Detection App")

uploaded_file = st.file_uploader("Upload Image", type=["jpg","png","jpeg"])

def predict(img):
    img = img.resize((128,128))
    img = np.array(img) / 255.0
    img = img.reshape(1,128,128,3)

    pred = model.predict(img)[0][0]

    if pred > 0.5:
        return "❌ No Mask", pred
    else:
        return "✅ Mask", 1 - pred

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, width=300)

    label, confidence = predict(image)

    st.subheader(label)

    st.progress(int(confidence * 100))
    st.write(f"Confidence: {confidence*100:.2f}%")
