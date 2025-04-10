import streamlit as st
import joblib
import pandas as pd

# Load the model
# Cargar el modelo
model = joblib.load('models/loan_eligibility_model.pkl')  # Ensure the correct path to the model

# App title
# Título de la app
st.title('Loan Eligibility Model')

# User inputs
# Entradas del usuario
income = st.number_input('Monthly income', min_value=0)  # Monthly income / Ingreso mensual
credit_score = st.number_input('Credit score', min_value=0)  # Credit score / Puntuación de crédito

# Make prediction when the user clicks 'Predict' button
# Realizar la predicción cuando el usuario haga clic en el botón 'Predecir'
if st.button('Predict'):
    # Create a DataFrame with the provided data
    # Crear un DataFrame con los datos proporcionados
    # Ensure column names match those used during model training
    # Asegúrate de que los nombres de las columnas coincidan con los usados durante el entrenamiento
    input_data = pd.DataFrame([[income, credit_score]], columns=['income', 'credit_score'])
    
    # Make the prediction
    # Realizar la predicción
    prediction = model.predict(input_data)
    
    # Output prediction result
    # Mostrar el resultado de la predicción
    if prediction == 1:
        st.write("The loan has been approved!")  # The loan has been approved! / ¡El préstamo ha sido aprobado!
    else:
        st.write("Sorry, the loan has not been approved.")  # The loan has not been approved / Lo siento, el préstamo no ha sido aprobado.
