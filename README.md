# AI-For-Password-Strength-Analysis
This project utilizes a Long Short-Term Memory (LSTM) model, a type of recurrent neural network (RNN) well-suited for sequence prediction tasks. LSTMs have been widely used for natural language processing (NLP) tasks, including text generation and sequence classification. The model is trained on leaked password datasets.

## Overview

The **AI Password Strength Checker** is a web application that evaluates password strength using machine learning models. It leverages **FastAPI** for the backend and a simple **HTML, CSS, and JavaScript** frontend for user interaction. The backend processes password inputs and provides a security score, helping users create stronger passwords.

## Technology Stack
- **Framework**: Streamlit (Python)
- **Machine Learning**: TensorFlow, scikit-learn

## Project Structure
```
project_root/
│── app.py  # Streamlit UI and backend logic
│── preprocessed_passwords.csv  # Training dataset
│── tokenizer.pkl  # Trained ML model
├── passwordstrength.ipynb  # Jupyter Notebook for exploration
│── rockyou dataset.txt  # Link to download the dataset used for training the model
```

## How to Run the Project

### 1️⃣ Install Dependencies
Ensure you have Python installed, then install the required dependencies:
```bash
pip install streamlit scikit-learn pandas pickle5
```

### 2️⃣ Run the Streamlit App
Navigate to the project root and run:
```bash
streamlit run app.py
```
This starts the UI in your browser.

### 3️⃣ Check Password Strength
- Enter a password in the Streamlit input field.
- Click **Check Strength**.
- The result is displayed directly in the UI.

  ![image](https://github.com/user-attachments/assets/df23cfc0-12dc-4fb0-9431-76078257a707)


## Troubleshooting
- If the app does not launch, ensure all dependencies are installed properly.
- If you get a `ModuleNotFoundError`, reinstall the missing package using:
  ```bash
  pip install <missing_package>
  ```
- If an error occurs with the ML model, ensure the `tokenizer.pkl` file exists in thesame folder as the app.py.



## Contributing

Feel free to fork this repository, make changes, and submit pull requests!

## Conclusion
This project demonstrates how AI can be used to assess password strength effectively. Future improvements may include real-time feedback and integration with authentication systems.

---
**Author**: [LANGIA, ARMAND ARISTIDE FEH]  
**Date**: [March 2025]

