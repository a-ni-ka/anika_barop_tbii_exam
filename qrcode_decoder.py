import streamlit as st
import numpy as np
import cv2


def decoder_page():
    st.title("Decode a QR Code")

    qrcode = st.file_uploader("Upload your QR code here",
                              type=["jpg", "jpeg", "png"])

    if qrcode:
        file_bytes = np.asarray(bytearray(qrcode.read()), dtype=np.uint8)
        opencv_image = cv2.imdecode(file_bytes, 1)
        st.image(opencv_image)
        detector = cv2.QRCodeDetector()
        decoded_info, point, straight_qr = detector.detectAndDecode(opencv_image)
        st.write(f"Your QR Code contains: {decoded_info}")
