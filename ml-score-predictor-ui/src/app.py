import streamlit as st
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Title and description
st.title("Student Score Predictor")
st.write("This app predicts student scores based on various input features.")

# Input fields
study_hours = st.number_input("Study Hours", min_value=0.0, step=0.1)
previous_score = st.number_input("Previous Score", min_value=0.0, step=0.1)
sleep_hours = st.number_input("Sleep Hours", min_value=0.0, step=0.1)
practice_papers = st.number_input("Practiced Sample Paper Count", min_value=0, step=1)
extracurricular = st.selectbox("Extracurricular Activities", ["No", "Yes"])

# Convert extracurricular to boolean
extracurricular = 1 if extracurricular == "Yes" else 0

# Placeholder for model training (to be replaced with actual logic)
def train_model():
    # Example data (replace with actual dataset and logic)
    data = pd.DataFrame({
        "Study Hours": [1, 2, 3, 4, 5],
        "Previous Score": [50, 60, 70, 80, 90],
        "Sleep Hours": [6, 7, 8, 5, 6],
        "Practiced Sample Paper Count": [1, 2, 3, 4, 5],
        "Extracurricular Activities": [0, 1, 0, 1, 0],
        "Score": [55, 65, 75, 85, 95]
    })

    X = data.drop("Score", axis=1)
    y = data["Score"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

    model = LinearRegression()
    model.fit(X_train, y_train)

    return model

# Train the model
model = train_model()

# Predict button
if st.button("Predict"):
    # Create input array
    input_data = np.array([study_hours, previous_score, sleep_hours, practice_papers, extracurricular]).reshape(1, -1)

    # Make prediction
    prediction = model.predict(input_data)

    # Display result
    st.write(f"Predicted Score: {prediction[0]:.2f}")