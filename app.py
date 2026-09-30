import streamlit as st
import requests

st.title("Clinton Microclimate Monitor")
st.write("Real-time atmospheric data local to rural Indiana")

channelid = "3513439"
url = (f"https://api.thingspeak.com/channels/{channelid}/feeds/last.json")

data = requests.get(url).json()
st.header("Live Weather/Conditions")

soil_moisture = data["field1"]
temperature = data["field2"]
humidity = data["field3"]

st.metric("Soil Moisture: ", f"{float(soil_moisture):.1f} %")
st.metric("Temperature: ", f"{float(temperature):.1f} degrees F")
st.metric("Humidity: ", f"{float(humidity):.1f}")
