import streamlit as st
import pickle
import pandas as pd
import numpy as np



with open('aqi_model.pkl', 'rb') as file:
    loaded_model = pickle.load(file)
    print("model loaded")

def predict_air_quality(input_data):
    # Convert input DataFrame to NumPy array
    input_array = np.array(input_data.values).reshape(1, -1)

    # Use the loaded model to generate predictions
    predictions = loaded_model.predict(input_array)

    return predictions


def main():
    
    st.title("Air Quality Prediction")

    st.text("Hello! Welcome to the AQI prediction app!")
    st.subheader("Enter the input data for air quality prediction:")
    co = st.number_input("CO (ppm)")
    no = st.number_input("NO (ppm)")
    no2 = st.number_input("NO2 (ppm)")
    o3 = st.number_input("O3 (ppm)")
    so2 = st.number_input("SO2 (ppm)")
    pm2_5 = st.number_input("PM2.5 (µg/m³)")
    pm10 = st.number_input("PM10 (µg/m³)")
    nh3 = st.number_input("NH3 (ppm)")

    user_input_data = {
        "components.co": co,
        "components.no": no,
        "components.no2": no2,
        "components.o3": o3,
        "components.so2": so2,
        "components.pm2_5": pm2_5,
        "components.pm10": pm10,
        "components.nh3": nh3,
        # Add more input fields as needed
  
    }

    df = pd.DataFrame.from_dict(user_input_data, orient='index', columns=['value'])

    predictions = predict_air_quality(df)


    st.subheader("Air Quality Prediction Results:")
    st.write("CO:", user_input_data["components.co"])
    st.write("NO:", user_input_data["components.no"])
    st.write("NO2:", user_input_data["components.no2"])
    st.write("O3:", user_input_data["components.o3"])
    st.write("SO2:", user_input_data["components.so2"])
    st.write("PM2.5:", user_input_data["components.pm2_5"])
    st.write("PM10:", user_input_data["components.pm10"])
    st.write("NH3:", user_input_data["components.nh3"])
    st.write("Predicted Air Quality:", predictions)

    if predictions<1:
        st.text("The air quality is GOOD")
    elif predictions<2:
        st.text("The air quality is MODERATE")
    elif predictions<3:
        st.text("The air quality is POOR")
    elif predictions<4:
        st.text("The air quality is UNHEALTHY")
    else:
        st.text("The air quality is HAZARDOUS!")




main()