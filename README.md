# AI-Based Medical Diagnosis System

An AI-powered medical diagnosis system that predicts possible diseases from a user's description of symptoms using a Machine Learning text classification model. The system analyzes symptom descriptions and returns probabilities for multiple diseases through an interactive Gradio interface.

---

# Project Overview

This project uses Natural Language Processing (NLP) to analyze symptom descriptions provided by users and predict possible diseases. The model is trained using FastAI and deployed with a simple web interface using Gradio.

The goal of this system is to demonstrate how AI and Machine Learning can assist in preliminary medical analysis by interpreting symptom descriptions and predicting potential health conditions.

---

# Features

- Predict diseases based on symptom descriptions
- Text classification using FastAI
- Interactive user interface with Gradio
- Probability scores for each disease category
- Simple and lightweight AI model deployment

---

# Diseases Predicted

The model predicts probabilities for the following diseases:

- Allergy
- Anemia
- Bronchitis
- Diabetes
- Diarrhea
- Fatigue
- Flu
- Malaria
- Stress

---

# Project Architecture


User Input (Symptom Description)
↓
Text Processing
↓
FastAI NLP Model (Text Classification)
↓
Disease Probability Prediction
↓
Gradio Interface Displays Results


---

# System Workflow

1. User enters a description of their symptoms.
2. The input text is sent to the trained machine learning model.
3. The FastAI model analyzes the text using NLP techniques.
4. The model predicts probabilities for different diseases.
5. The results are displayed through the Gradio interface.

---

# Tech Stack

**Programming Language**

- Python

**Machine Learning Framework**

- FastAI

**User Interface**

- Gradio

**Model Type**

- NLP Text Classification Model

---

# Project Structure


medical-diagnosis-ai
│
├── app.py
├── model.pkl
├── requirements.txt
├── README.md
└── .gitattributes


---

# Installation

Clone the repository:

bash
git clone https://github.com/yourusername/medical-diagnosis-ai.git

Navigate into the project folder:

cd medical-diagnosis-ai

Install dependencies:

pip install -r requirements.txt
Running the Application

Run the application using:

python app.py

After running, the Gradio interface will launch in your browser.

Example Input

I have no interest in physical activity and feel very tired.


Example output:


Diabetes: 0.62
Fatigue: 0.21
Stress: 0.10

Dependencies

fastai
gradio


Install them using:

pip install fastai gradio
Future Improvements

Improve dataset size and model accuracy

Add more disease categories

Deploy the model using a cloud service

Add user history and symptom tracking

Build a full web application with frontend and backend

Disclaimer

This project is intended for educational and demonstration purposes only.
It should not be used as a substitute for professional medical advice.

Author

Rahul Kumar Chaudhary
B.Tech CSE (AI & ML)


---

# Bonus (Optional but Recommended)

Add these **GitHub topics/tags** to your repo:


machine-learning
nlp
medical-ai
fastai
gradio
ai-healthcare
text-classification
