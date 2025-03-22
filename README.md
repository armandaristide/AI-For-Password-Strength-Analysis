# AI-For-Password-Strength-Analysis
This project utilizes a Long Short-Term Memory (LSTM) model, a type of recurrent neural network (RNN) well-suited for sequence prediction tasks. LSTMs have been widely used for natural language processing (NLP) tasks, including text generation and sequence classification. The model is trained on leaked password datasets.

## Overview

The **AI Password Strength Checker** is a web application that evaluates password strength using machine learning models. It leverages **FastAPI** for the backend and a simple **HTML, CSS, and JavaScript** frontend for user interaction. The backend processes password inputs and provides a security score, helping users create stronger passwords.

## Technology Stack
- **Backend**: FastAPI (Python)
- **Frontend**: HTML, JavaScript, and Fetch API
- **Machine Learning**: TensorFlow
- **Deployment**: Uvicorn (for running FastAPI)

## Project Structure
```
project_root/
│── main.py  # FastAPI backend
│── model.py  # ML model loading and evaluation
│── index.html  # UI
│── leaked_passwords.csv  # Training dataset
│── password_strength_model.pkl  # Trained ML model
```

## How to Run the Project

### 1️⃣ Install Dependencies
Ensure you have Python installed, then install FastAPI and Uvicorn:
```bash
pip install fastapi uvicorn scikit-learn pandas
```

### 2️⃣ Run the FastAPI Server
Navigate to the project folder and run:
```bash
uvicorn main:app --reload
```
This starts the API at `http://127.0.0.1:8000`.

### 3️⃣ Start the Frontend
Open `index.html` in a browser.

### 4️⃣ Check Password Strength
- Enter a password in the input field.
- Click **Check Strength**.
- The result is fetched from FastAPI and displayed.

## API Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST   | `/predict` | Predicts password strength |
| GET    | `/status`  | Health check endpoint |

## Troubleshooting
- If `Address already in use` error appears, kill the existing process:
  ```bash
  sudo lsof -i :8000
  sudo kill -9 <PID>
  ```
- If the frontend does not fetch results, ensure FastAPI is running and update JavaScript to use `http://127.0.0.1:8000/predict`.


## Features

- **AI-powered password strength analysis**
- **FastAPI backend for processing requests**
- **Interactive frontend for user input**
- **Real-time feedback on password security**

## Contributing

Feel free to fork this repository, make changes, and submit pull requests!

## Conclusion
This project demonstrates how AI can be used to assess password strength effectively. Future improvements may include real-time feedback and integration with authentication systems.

---
**Author**: [LANGIA, ARMAND ARISTIDE FEH]  
**Date**: [March 2025]

