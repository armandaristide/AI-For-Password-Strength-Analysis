from fastapi import FastAPI
import tensorflow as tf
import numpy as np
import pickle
from tensorflow.keras.preprocessing.sequence import pad_sequences

app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this for security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Load model and tokenizer
model = tf.keras.models.load_model("password_strength_lstm.h5")
with open("tokenizer.pkl", "rb") as handle:
    tokenizer = pickle.load(handle)

max_length = 50  # Must match training

def predict_strength(password):
    sequence = tokenizer.texts_to_sequences([password])
    padded_sequence = pad_sequences(sequence, maxlen=max_length, padding='post')
    prediction = model.predict(padded_sequence)
    strength_labels = ["Weak", "Moderate", "Strong"]
    return {"strength": strength_labels[np.argmax(prediction)], "confidence": float(np.max(prediction))}

@app.get("/")
def home():
    return {"message": "FastAPI is running successfully!"}
    
@app.get("/predict/")
def get_strength(password: str):
    return predict_strength(password)
