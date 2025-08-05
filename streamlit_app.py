
import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("NYC Ride Fare Estimator")
st.write("Enter trip details below to estimate fare:")

# Collect user inputs
pickup_longitude = st.number_input("Pickup Longitude", value=-73.985428)
pickup_latitude = st.number_input("Pickup Latitude", value=40.748817)
dropoff_longitude = st.number_input("Dropoff Longitude", value=-73.985428)
dropoff_latitude = st.number_input("Dropoff Latitude", value=40.748817)
passenger_count = st.slider("Passenger Count", 1, 10, 1)

# Predict fare
if st.button("Estimate Fare"):
    input_data = np.array([[pickup_longitude, pickup_latitude,
                            dropoff_longitude, dropoff_latitude,
                            passenger_count]])
    prediction = model.predict(input_data)[0]
    st.success(f"Estimated Fare: ${prediction:.2f}")
