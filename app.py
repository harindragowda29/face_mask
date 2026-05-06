
import streamlit as st

st.set_page_config(page_title="Face Mask Detection Bot")

st.title("🤖 Face Mask Detection Project Bot")

st.write("Ask me about the project 👇")

# Sidebar menu (like chatbot options)
option = st.sidebar.radio(
    "Choose Topic",
    [
        "Project Overview",
        "Problem Statement",
        "Objectives",
        "System Architecture",
        "Tools & Technologies",
        "Data Understanding",
        "Preprocessing",
        "Model Building",
        "Model Evaluation",
        "Deployment",
        "Limitations",
        "Future Enhancements"
    ]
)

# -----------------------------
# Bot Responses
# -----------------------------

if option == "Project Overview":
    st.success("📌 Project Overview")
    st.write("""
The Face Mask Detection system is a deep learning-based application designed to automatically detect whether a person is wearing a face mask or not.

It uses Convolutional Neural Networks (CNN) and MobileNetV2, a lightweight and efficient model for image classification.

This system is useful in public health monitoring, surveillance systems, and access control during pandemic situations.
""")

elif option == "Problem Statement":
    st.warning("⚠ Problem Statement")
    st.write("""
Manual monitoring of mask usage in crowded places is difficult and error-prone.

This project solves this by building an automated system that detects mask and no-mask faces using CNN and MobileNetV2.
""")

elif option == "Objectives":
    st.info("🎯 Objectives")
    st.write("""
- Build an automated mask detection system
- Apply deep learning concepts
- Use transfer learning with MobileNetV2
- Improve model accuracy with preprocessing
- Deploy as a web application using Streamlit
""")

elif option == "System Architecture":
    st.info("🧠 System Architecture")
    st.write("""
1. Input Layer – Image dataset
2. Preprocessing – Resize, normalize, augment
3. Feature Extraction – MobileNetV2
4. Classification – Dense layers
5. Output – Mask / No Mask
""")

elif option == "Tools & Technologies":
    st.info("🛠 Tools & Technologies")
    st.write("""
- Pandas → Data handling
- NumPy → Numerical operations
- Scikit-learn → ML utilities
- TensorFlow/Keras → Deep learning
- Matplotlib & Seaborn → Visualization
- Streamlit → Deployment
""")

elif option == "Data Understanding":
    st.info("📊 Data Understanding")
    st.write("""
Dataset contains two classes:
- Mask
- No Mask

Images vary in lighting, pose, and background.
Balanced dataset improves performance.
""")

elif option == "Preprocessing":
    st.info("⚙ Data Preprocessing")
    st.write("""
- Resize images (224x224)
- Normalize pixel values (0–1)
- Data augmentation:
  - Rotation
  - Flipping
  - Zoom

This improves accuracy and prevents overfitting.
""")

elif option == "Model Building":
    st.info("🤖 Model Building")
    st.write("""
Model uses MobileNetV2 (pre-trained on ImageNet).

Added layers:
- Global Average Pooling
- Dense layers
- Output layer (Softmax)

Loss: Binary Crossentropy  
Optimizer: Adam
""")

elif option == "Model Evaluation":
    st.info("📈 Model Evaluation")
    st.write("""
Metrics used:
- Accuracy
- Confusion Matrix
- Precision & Recall

These help measure model performance and errors.
""")

elif option == "Deployment":
    st.info("🌐 Deployment")
    st.write("""
The model is deployed using Streamlit.

Features:
- Upload image
- Real-time prediction
- Simple user interface
""")

elif option == "Limitations":
    st.error("⚠ Limitations")
    st.write("""
- Poor performance on low-quality images
- Cannot detect improper mask usage
- Depends on lighting conditions
""")

elif option == "Future Enhancements":
    st.success("🚀 Future Enhancements")
    st.write("""
- Real-time webcam detection
- CCTV integration
- Mobile app deployment
- Alert system for violations
""")


