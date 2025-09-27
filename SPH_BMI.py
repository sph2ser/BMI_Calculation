import streamlit as st
from PIL import Image
# App Title
st.title("Body Mass Index (BMI) Calculater")

#Display Image
image=Image.open("BMI.png")
st.image(image,use_column_width=True)

#Input Fields
name=st.text_input("Enter Your Name and Lastname")
height=st.number_input("Enter your height in cm:",format="%.2f")
weight=st.number_input("Enter your weight in kg:",format="%.2f")

#Calculate BMI
if st.button("Calculate Body Mass Index (BMI)"):
    if height > 0:
        height_m = height/100
        bmi = weight/(height_m**2)
        if bmi<18.5:
            category="Underweight"
        elif 18.5 <= bmi < 24.9:
            category="Normal weight"
        elif 25 <= bmi < 29.9:
            category="Overweight"
        else:
            category="Obese"
        st.success(f"{name},your BMI is {bmi:.2F} which is considered {category}")
    else:
        st.error("Please enter the valid height")