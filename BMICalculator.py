import streamlit as st

st.title("BMI Calculator")

height_in_cm = st.slider("Enter your Height (in cm) : ", 100, 250)
weight_in_kg = st.slider("Enter your Weight (in kg) :", 40, 200)
bmi = weight_in_kg / ((height_in_cm / 100) ** 2)

if st.button("Calculate BMI"):
    st.markdown(f"Your BMI is :red-background[**{round(bmi, 2)}**]")

    if bmi < 18.5:
        st.markdown(":blue[you are in **Underweight** category]")

    elif 18.5 < bmi < 24.9:
        st.markdown(":rainbow[You have **Normal** weight]")
        st.balloons()

    elif 25 < bmi < 25.9:
        st.markdown(":green[You are in **Overweight** category]")

    else:
        st.markdown(":red[You are Obese!]")



st.header("BMI Guide")
st.write("**Underweight** : BMI less than 18.5")
st.write("**Normal Weight** : BMI between 18.5 and 24.9")
st.write("**Overweight** : BMI between 25 and 29.9")
st.write("**Obesity** : BMI 30 or greater")
