import streamlit as st
import random
from PIL import Image

st.set_page_config(page_title="Face Mask Detection", layout="centered")

st.title("😷 Face Mask Detection")

st.write("Upload an image to detect mask usage")

uploaded_file = st.file_uploader("Upload Image", type=["jpg","png","jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, width=300)

    # Fake prediction (demo UI)
    label = random.choice(["Mask", "No Mask"])
    confidence = random.uniform(0.85, 1.0)

    st.markdown("##")

    # Result Box
    if label == "Mask":
        st.markdown(
            f"""
            <div style="border:2px solid green; padding:15px; border-radius:10px; text-align:center;">
                <h2 style="color:green;">✅ Wearing Mask</h2>
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            f"""
            <div style="border:2px solid red; padding:15px; border-radius:10px; text-align:center;">
                <h2 style="color:red;">❌ No Mask</h2>
            </div>
            """,
            unsafe_allow_html=True
        )

    # Confidence Section
    st.markdown("### 📊 Confidence Level")
    st.progress(int(confidence * 100))

    st.write(f"Prediction: {label}")
    st.write(f"Confidence: {confidence*100:.2f}%")

    # Confidence Message
    if confidence > 0.9:
        st.success("🔥 High Confidence")
    else:
        st.warning("⚠ Medium Confidence")

