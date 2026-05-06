```python
import streamlit as st
import numpy as np
import cv2
from PIL import Image
from tensorflow.keras.models import load_model

# ----------------------------
# Load Model
# ----------------------------
@st.cache_resource
def load_cnn_model():
    return load_model("mask_detector.h5")

model = load_cnn_model()

# ----------------------------
# App Title
# ----------------------------
st.title("😷 Face Mask Detection App")
st.write("Upload an image or use webcam to detect mask")

# ----------------------------
# Sidebar Options
# ----------------------------
option = st.sidebar.selectbox(
    "Choose Input Method",
    ("Upload Image", "Use Webcam")
)

# ----------------------------
# Image Preprocessing
# ----------------------------
def preprocess_image(img):
    img = cv2.resize(img, (128, 128))
    img = img / 255.0
    img = np.reshape(img, (1, 128, 128, 3))
    return img

# ----------------------------
# Prediction Function
# ----------------------------
def predict_mask(img):
    processed = preprocess_image(img)
    pred = model.predict(processed)[0][0]

    if pred > 0.5:
        return "No Mask", pred
    else:
        return "Mask", 1 - pred

# ----------------------------
# Face Detection
# ----------------------------
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

def detect_and_predict(image):
    img = np.array(image)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        face = img[y:y+h, x:x+w]
        label, confidence = predict_mask(face)

        color = (0, 255, 0) if label == "Mask" else (0, 0, 255)

        cv2.rectangle(img, (x, y), (x+w, y+h), color, 2)
        cv2.putText(
            img,
            f"{label} ({confidence:.2f})",
            (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            color,
            2
        )

    return img

# ----------------------------
# Upload Image Mode
# ----------------------------
if option == "Upload Image":
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        if st.button("Detect Mask"):
            result_img = detect_and_predict(image)
            st.image(result_img, caption="Result", use_column_width=True)

# ----------------------------
# Webcam Mode
# ----------------------------
elif option == "Use Webcam":
    st.warning("Click start and allow camera access")

    run = st.checkbox("Start Camera")

    FRAME_WINDOW = st.image([])

    camera = cv2.VideoCapture(0)

    while run:
        ret, frame = camera.read()
        if not ret:
            st.error("Failed to access webcam")
            break

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = detect_and_predict(frame)

        FRAME_WINDOW.image(result)

    camera.release()
```
