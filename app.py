
import streamlit as st
import pickle
import numpy as np

# Load trained model
model = pickle.load(open("model.pkl", "rb"))

st.title("🏠 House Price Prediction App")

st.markdown("Enter the details of the house to predict the price.")

# Input fields
area = st.number_input("Area (in sq. ft)", min_value=100, max_value=10000, value=1200)
bedrooms = st.number_input("Bedrooms", min_value=1, max_value=10, value=3)
bathrooms = st.number_input("Bathrooms", min_value=1, max_value=5, value=2)
stories = st.number_input("Stories", min_value=1, max_value=5, value=1)
mainroad = st.selectbox("Main Road?", ["Yes","No"])
guestroom = st.selectbox("Guest Room?", ["Yes","No"])
basement = st.selectbox("Basement?", ["Yes","No"])
hotwaterheating = st.selectbox("Hot Water Heating?", ["Yes","No"])
airconditioning = st.selectbox("Air Conditioning?", ["Yes","No"])
parking = st.number_input("Parking Spaces", min_value=0, max_value=5, value=1)
prefarea = st.selectbox("Preferred Area?", ["Yes","No"])
furnishingstatus = st.selectbox("Furnishing Status", ["Unfurnished","Semi-furnished","Furnished"])

# Map categorical to numeric
yes_no_map = {"Yes":1,"No":0}
furnish_map = {"Unfurnished":0,"Semi-furnished":1,"Furnished":2}

mainroad = yes_no_map[mainroad]
guestroom = yes_no_map[guestroom]
basement = yes_no_map[basement]
hotwaterheating = yes_no_map[hotwaterheating]
airconditioning = yes_no_map[airconditioning]
prefarea = yes_no_map[prefarea]
furnishingstatus = furnish_map[furnishingstatus]

# Predict button
if st.button("Predict Price"):
    features = np.array([[area, bedrooms, bathrooms, stories, mainroad, guestroom,
                          basement, hotwaterheating, airconditioning, parking,
                          prefarea, furnishingstatus]])
    prediction = model.predict(features)
    st.success(f"🏡 Estimated Price: ${prediction[0]:,.2f}")
