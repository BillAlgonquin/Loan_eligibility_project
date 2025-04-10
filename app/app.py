import streamlit as st
import joblib
import pandas as pd
import logging

# Configure logging
# Configurar logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

# Load the model
# Cargar el modelo
try:
    model = joblib.load('models/loan_eligibility_model.pkl')  # Ensure the correct path to the model
    logging.info("Model loaded successfully.")  # Log the successful model load
except Exception as e:
    logging.error(f"Error loading the model: {e}")  # Log any error that occurs

# App title
# Título de la app
st.title('Loan Eligibility Model')

# User inputs
# Entradas del usuario
income = st.number_input('Monthly income', min_value=0)  # Monthly income / Ingreso mensual
credit_score = st.number_input('Credit score', min_value=0)  # Credit score / Puntuación de crédito

# Log user inputs
logging.info(f"User input - Monthly income: {income}, Credit score: {credit_score}")  # Log the user inputs

# Make prediction when the user clicks 'Predict' button
# Realizar la predicción cuando el usuario haga clic en el botón 'Predecir'
if st.button('Predict'):
    # Create a DataFrame with the provided data
    # Crear un DataFrame con los datos proporcionados
    # Ensure column names match those used during model training
    # Asegúrate de que los nombres de las columnas coincidan con los usados durante el entrenamiento
    input_data = pd.DataFrame([[income, credit_score]], columns=['income', 'credit_score'])
    
    # Log input data before prediction
    logging.info(f"Input data for prediction: {input_data}")  # Log the data used for prediction

    # Make the prediction
    # Realizar la predicción
    try:
        prediction = model.predict(input_data)
        logging.info(f"Prediction result: {prediction}")  # Log the prediction result
    except Exception as e:
        logging.error(f"Error during prediction: {e}")  # Log any error during prediction
    
    # Output prediction result
    # Mostrar el resultado de la predicción
    if prediction == 1:
        st.write("The loan has been approved!")  # The loan has been approved! / ¡El préstamo ha sido aprobado!
        logging.info("The loan has been approved.")  # Log when the loan is approved
    else:
        st.write("Sorry, the loan has not been approved.")  # The loan has not been approved / Lo siento, el préstamo no ha sido aprobado.
        logging.info("The loan has not been approved.")  # Log when the loan is not approved
