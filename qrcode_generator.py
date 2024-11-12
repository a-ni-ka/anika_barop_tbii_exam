import streamlit as st
import segno
import time
from urllib.request import urlopen


def generator_page():
    st.title("Create Your Unique QR Code")
    style = st.radio("Pick a QR Code style", ["Standard (.png)", "Animated (.gif)"])

    if style == "Standard (.png)":
        dark_color = st.color_picker("Pick a dark color")
        light_color = st.color_picker("Pick a light color", value="#ffffff")
    elif style == "Animated (.gif)":
        gif = st.text_input("Enter a giphy link:")

    url = st.text_input("Enter the data you would like to encode:")

    def generate_qrcode(url):
        global qrcode
        qrcode = segno.make_qr(url)

    button = st.button("GENERATE", on_click=generate_qrcode(url))

    if button and url:
        with st.spinner("Working on it"):
            time.sleep(2)
        generate_qrcode(url)
        if style == "Standard (.png)":
            st.image(qrcode.to_pil(scale=10, dark=dark_color, light=light_color))
        elif style == "Animated (.gif)" and gif:
            giphy = urlopen(gif)
            qrcode.to_artistic(background=giphy, scale=10, target="../qrcode.gif")
            st.markdown("")
