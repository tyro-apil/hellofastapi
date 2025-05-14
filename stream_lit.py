import streamlit as st
import json
import requests

st.title("Basic Calculator App")

# Taking user inputs
option = st.selectbox(
    "What operation do you want to perform?",
    ("add", "subtract", "multiply", "divide"),
)

st.write("")
st.write("Select the numbers from the slider below")
x = st.slider("X", 0, 100, 20)
y = st.slider("Y", 0, 100, 10)  # Corrected slider range for Y

# Converting the inputs into a JSON format
inputs = {"operation": option, "x": x, "y": y}

# When the user clicks the button, it will fetch the API
if st.button("Calculate"):
    res = requests.post(url="http://127.0.0.1:8000/calculate", data=json.dumps(inputs))
    st.subheader(f"Response from API = {res.text}")
