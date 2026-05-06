import streamlit as st
import numpy as np
import cv2
from PIL import Image
from tensorflow.keras.models import load_model

# ----------------------------
# Load Model
# ----------------------------
model = load_model("mask_detector.h5")

# ----------------------------
# Page Config
# ----------------------------
st.set_page_config(page_title="Face Mask Detection", layout="wide")

st.title("😷 Face Mask Detection + Chatbot")

# ----------------------------
# Tabs
# ----------------------------
tab1, tab2 = st.tabs(["🖼 Detection", "🤖 Chatbot"])

# =====================================================
# TAB 1 → MASK DETECTION
# =====================================================
with tab1:

    st.header("Upload Image")

    uploaded_file = st.file_uploader("Upload Image", type=["jpg", "png", "jpeg"])

    def predict(img):
        img = cv2.resize(img, (128,128))
        img = img / 255.0
        img = np.reshape(img, (1,128,128,3))

        pred = model.predict(img)[0][0]

        if pred > 0.5:
            return "No Mask", pred
        else:
            return "Mask", 1 - pred

    if uploaded_file:
        image = Image.open(uploaded_file)
        st.image(image, width=300)

        img = np.array(image)

        label, confidence = predict(img)

        if label == "Mask":
            st.success(f"✅ Wearing Mask")
        else:
            st.error(f"❌ No Mask")

        st.subheader("📊 Confidence Level")
        st.progress(int(confidence * 100))

        st.write(f"Confidence: {confidence*100:.2f}%")

# =====================================================
# TAB 2 → CHATBOT
# =====================================================
with tab2:

    st.header("🤖 Project Chatbot")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    def get_response(user_input):
        user_input = user_input.lower()

        if "overview" in user_input:
            return "Face Mask Detection system uses CNN and MobileNetV2 to detect masks."

        elif "problem" in user_input:
            return "Manual monitoring is difficult, so we automate mask detection."

        elif "objective" in user_input:
            return "Build model, apply deep learning, deploy with Streamlit."

        elif "tools" in user_input:
            return "Pandas, NumPy, TensorFlow, OpenCV, Streamlit."

        elif "accuracy" in user_input:
            return "Model evaluated using accuracy, precision, recall."

        else:
            return "Ask about overview, problem, objectives, tools, or model."

    user_input = st.chat_input("Ask about project...")

    if user_input:
        st.session_state.messages.append(("user", user_input))
        response = get_response(user_input)
        st.session_state.messages.append(("bot", response))

    for role, msg in st.session_state.messages:
        if role == "user":
            st.chat_message("user").write(msg)
        else:
            st.chat_message("assistant").write(msg)
