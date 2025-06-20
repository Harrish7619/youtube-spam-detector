import streamlit as st
from joblib import load
import numpy as np


# Wider layout
st.markdown("<h1 style='text-align: center;'>🎯 YouTube Spam Comment Detector</h1>", unsafe_allow_html=True)

# Load TF-IDF Vectorizer
vectorizer = load('saved_models/tfidf_vectorizer.joblib')

# Load all models
models = {
    'Logistic Regression': load('saved_models/lr_model.joblib'),
    'Naive Bayes': load('saved_models/nb_model.joblib'),
    'MLP Classifier': load('saved_models/mlp_model.joblib'),
    'SVC Classifier': load('saved_models/svc_model.joblib'),
    'Decision Tree': load('saved_models/dt_model.joblib'),
    'Random Forest': load('saved_models/rf_model.joblib'),
    'KNN': load('saved_models/knn_model.joblib'),
    'Voting Classifier': load('saved_models/voting_model.joblib')
}

# App title
#st.title("🎯 YouTube Spam Comment Detector")

# User input
user_input = st.text_area("📝 Enter a YouTube comment:", height=150)

# Dropdown to choose model
selected_model_name = st.selectbox("🤖 Select a model:", list(models.keys()))

# Predict button
if st.button("Predict"):
    if user_input.strip() == "":
        st.warning("Please enter a comment.")
    else:
        model = models[selected_model_name]

        # Vectorize input
        vectorized_input = vectorizer.transform([user_input])

        # For models that need dense input like Naive Bayes
        if selected_model_name == 'Naive Bayes':
            vectorized_input = vectorized_input.toarray()

        prediction = model.predict(vectorized_input)[0]
        label = "📦 Spam" if prediction == 1 else "✅ Ham (Not Spam)"

        st.markdown(f"### 🔍 Prediction using {selected_model_name}: {label}")
