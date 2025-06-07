import streamlit as st

st.title("Selamat Datang Di Web Informatika")
st.write("ngoding seru bersama Belva")
st.image("IMG_3224.jpeg", width=500)
st.title("bjorkababayo")
angka = st.number_input("write a number:", value=0, step=1)
if (angka%2) == 0: 
st.write (f"{angka} adalah bilangan genap")
else:
st.write(f"{angka} adalah bilangan ganjil")
