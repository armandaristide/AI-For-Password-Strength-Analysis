import streamlit as st
import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import Tokenizer
import pickle


# Load the trained model
model = tf.keras.models.load_model("password_strength_lstm.h5")


# Recompile the model (if needed)
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Load tokenizer

tokenizer = Tokenizer()
# (Possibly fit it on some data before saving)

with open("tokenizer.pkl", "wb") as handle:
    pickle.dump(tokenizer, handle, protocol=pickle.HIGHEST_PROTOCOL)

# Define max_length (must match training configuration)
max_length = 50

# Function to predict password strength
def predict_strength(password):
    st.write("Debug: Checking if model and tokenizer are loaded.")
    sequence = tokenizer.texts_to_sequences([password])
    padded_sequence = pad_sequences(sequence, maxlen=max_length, padding='post')
    prediction = model.predict(padded_sequence)
    strength_labels = ["Weak", "Moderate", "Strong"]
    return strength_labels[np.argmax(prediction)], np.max(prediction)


# Streamlit UI
def main():
    # Debugging logs
    st.set_page_config(layout="wide")
    st.write("🔍 Checking model and tokenizer loading...")

    try:
        model = tf.keras.models.load_model("password_strength_lstm.h5")
        st.write("✅ Model loaded successfully.")
    except Exception as e:
        st.error(f"❌ Model loading failed: {e}")
    
    try:
        with open("tokenizer.pkl", "rb") as handle:
            tokenizer = pickle.load(handle)
        st.write("✅ Tokenizer loaded successfully.")
    except Exception as e:
        st.error(f"❌ Tokenizer loading failed: {e}")

    st.title("🔐 AI-Based Password Strength Analyzer")
    st.write("Enter a password to check its strength using an AI model.")
    
    password = st.text_input("Enter Password:", type="password")
    if st.button("Check Strength"):
        if password:
            strength, confidence = predict_strength(password)
            st.success(f"Password Strength: {strength} (Confidence: {confidence:.2f})")
        else:
            st.warning("Please enter a password.")

if __name__ == "__main__":
    main()

