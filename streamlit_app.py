import joblib

import streamlit as st

import numpy as np

lasso_model = joblib.load(r'C:\Users\yashr\Downloads\Streamlit_Used_car_Prediction-main\Streamlit_Used_car_Prediction-main\Streamlit\lasso_model.pkl')


# Load the Lasso model
# lasso_model = joblib.load('lasso_model.pkl')

# Streamlit app title
st.title('Used Car Price Prediction for Maruti Cars')
# Model Name input as a radio
model_name = st.selectbox('Select Car Model', [
    'A Star', 'Alto', 'Baleno', 'Brezza', 'Celerio', 'Ciaz', 'Dzire', 'Eeco', 'Ertiga',
    'Ignis', 'Omni', 'Ritz', 'S Cross', 'S Presso', 'Swift', 'Wagon R', 'XL6', 'Zen Estilo'
])


# Manufacturing year input as a slider
manufacturing_year = st.slider("Select Manufacturing Year", 2011, 2023, 2015)


# Define user input features
engine_capacity = st.slider("Enter engine capacity (in cc)", 500, 2500, 1200)
km_driven = st.slider("Enter kilometers driven", 1000, 200000, 50000)
ownership = st.radio("Select Ownership", ('First Owner', 'Second Owner'))
imperfections = st.slider("Imperfections?", 0,15,35)
repainted_parts = st.slider("Repainted Parts?", 0,8,15)
transmission = st.radio("Select Transmission Type", ('Manual', 'Automatic'))
fuel_type = st.radio("Select Fuel Type", ('Petrol', 'Diesel', 'CNG'))
spare_key = st.radio("Spare Key Available?", ('Yes', 'No'))


# Initialize features list for one-hot encoded values
feature_list = [
    'Engine capacity', 'KM driven', 'Ownership', 'Imperfections', 'Repainted Parts',
    'Transmission_Automatic', 'Transmission_Manual', 'Fuel type_CNG', 'Fuel type_Diesel', 
    'Fuel type_Petrol', 'Model Name_A Star', 'Model Name_Alto', 'Model Name_Baleno', 
    'Model Name_Brezza', 'Model Name_Celerio', 'Model Name_Ciaz', 'Model Name_Dzire', 
    'Model Name_Eeco', 'Model Name_Ertiga', 'Model Name_Ignis', 'Model Name_Omni', 
    'Model Name_Ritz', 'Model Name_S Cross', 'Model Name_S Presso', 'Model Name_Swift', 
    'Model Name_Wagon R', 'Model Name_XL6', 'Model Name_Zen Estilo', 'Manufacturing_year_2011', 
    'Manufacturing_year_2012', 'Manufacturing_year_2013', 'Manufacturing_year_2014', 
    'Manufacturing_year_2015', 'Manufacturing_year_2016', 'Manufacturing_year_2017', 
    'Manufacturing_year_2018', 'Manufacturing_year_2019', 'Manufacturing_year_2020', 
    'Manufacturing_year_2021', 'Manufacturing_year_2022', 'Manufacturing_year_2023', 
    'Spare key_No', 'Spare key_Yes'
]

# Initialize a dictionary with zeros for all features
feature_dict = {feature: 0 for feature in feature_list}


# Set the values based on user inputs
feature_dict[f'Engine capacity'] = engine_capacity
feature_dict[f'KM driven'] = km_driven

# One-hot encoding for categorical variables
# Ownership
if ownership == 'First Owner':
    feature_dict['Ownership'] = 0
elif ownership == 'Second Owner':
    feature_dict['Ownership'] = 1
else:
    feature_dict['Ownership'] = 2

# Imperfections
feature_dict['Imperfections'] = 1 if imperfections == 'Yes' else 0

# Repainted Parts
feature_dict['Repainted Parts'] = 1 if repainted_parts == 'Yes' else 0

# Transmission
feature_dict['Transmission_Automatic'] = 1 if transmission == 'Automatic' else 0
feature_dict['Transmission_Manual'] = 1 if transmission == 'Manual' else 0

# Fuel Type
feature_dict['Fuel type_Petrol'] = 1 if fuel_type == 'Petrol' else 0
feature_dict['Fuel type_Diesel'] = 1 if fuel_type == 'Diesel' else 0
feature_dict['Fuel type_CNG'] = 1 if fuel_type == 'CNG' else 0

# Spare key
feature_dict['Spare key_Yes'] = 1 if spare_key == 'Yes' else 0
feature_dict['Spare key_No'] = 1 if spare_key == 'No' else 0

# Model Name
feature_dict[f'Model Name_{model_name}'] = 1

# Manufacturing year
feature_dict[f'Manufacturing_year_{manufacturing_year}'] = 1

# Convert the dictionary to a numpy array for prediction
features = np.array([list(feature_dict.values())])

# Predict button
if st.button('Predict Car Price'):
    prediction = lasso_model.predict(features)[0]
    st.success(f'The predicted price for the car is: ₹{int(prediction):,}')
