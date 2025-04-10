# Loan Eligibility Prediction

This project implements a machine learning model to predict loan eligibility based on the applicant's monthly income and credit score. The model is trained using a fictional dataset and is deployed through a Streamlit application for real-time predictions.

## Project Structure

/loan_eligibility_project 
├── /data 
│ └── dataset.csv 
├── /models 
│ └── loan_eligibility_model.pkl 
├── /scripts 
│ └── data_preprocessing.py 
│ └── model_training.py 
├── /app 
│ └── app.py 
├── README.md 
└── requirements.txt


## Requirements

- Python 3.8 or higher
- pandas
- scikit-learn
- joblib
- streamlit

## How to Run the Application

1. Clone this repository:
    ```bash
    git clone https://github.com/BillAlgonquin/loan_eligibility_project.git
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the Streamlit app:
    ```bash
    streamlit run app/app.py
    ```

4. Access the app at `http://localhost:8501`.

## License

This project is licensed under the MIT License.
