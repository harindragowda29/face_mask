```python
import streamlit as st

st.title("🤖 Face Mask Detection Chatbot")

# Store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Function to generate reply
def get_response(user_input):
    user_input = user_input.lower()

    if "overview" in user_input:
        return "This project detects whether a person is wearing a face mask using CNN and MobileNetV2."

    elif "problem" in user_input:
        return "Manual monitoring of masks is difficult. This system automates mask detection."

    elif "objective" in user_input:
        return "Objectives include building a mask detection system, using deep learning, and deploying via Streamlit."

    elif "architecture" in user_input:
        return "Architecture includes Input → Preprocessing → MobileNetV2 → Dense Layers → Output."

    elif "tools" in user_input:
        return "Tools used: Pandas, NumPy, Scikit-learn, TensorFlow, Streamlit."

    elif "evaluation" in user_input:
        return "Model is evaluated using Accuracy, Confusion Matrix, Precision, and Recall."

    elif "deployment" in user_input:
        return "The model is deployed using Streamlit for easy web access."

    else:
        return "Sorry, I didn’t understand. Try asking about overview, objectives, or model."

# Chat input
user_input = st.chat_input("Ask something about the project...")

if user_input:
    st.session_state.messages.append(("user", user_input))
    response = get_response(user_input)
    st.session_state.messages.append(("bot", response))

# Display chat
for role, msg in st.session_state.messages:
    if role == "user":
        st.chat_message("user").write(msg)
    else:
        st.chat_message("assistant").write(msg)
```
