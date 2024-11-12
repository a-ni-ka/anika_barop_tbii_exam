import streamlit as st
from qrcode_decoder import decoder_page
from qrcode_generator import generator_page

st.set_page_config(page_title="QR-Code App",
                   page_icon="🪄")

options = ["Create QR Code", "Decode QR Code", "About"]
page_selection = st.sidebar.selectbox("Menu", options)

if page_selection == "Create QR Code":
    generator_page()
elif page_selection == "Decode QR Code":
    decoder_page()
elif page_selection == "About":
    st.write("This app was developed by Anika")
