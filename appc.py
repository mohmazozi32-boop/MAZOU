import streamlit as st

st.title("🌞 اول موقع لي باستخدام Python")

st.write("مرحبا بك في اول تطبيق ويب بسيط")

name = st.text_input("اكتب اسمك")
number = st.number_input("ادخل رقم")

if st.button("احسب"):
    st.write("مرحبا", name)
    st.write("مربع الرقم هو:", number**2)

option = st.selectbox(
    "اختر تخصصك",
    ["رياضيات", "فيزياء", "إعلام آلي", "طاقات متجددة"]
)
st.write("اخترت:", option)