import streamlit as st
import cv2
import numpy as np
from PIL import Image
import sys

st.set_page_config(page_title="Test App")
st.title("TEST APP")

st.write("Python version:", sys.version)

try:
    st.write("Mencoba import cv2...")
    import cv2
    st.success("✅ OpenCV berhasil diimport!")
    st.write("OpenCV version:", cv2.__version__)
except Exception as e:
    st.error(f"❌ OpenCV gagal: {e}")

st.write("Jika ini muncul, app berjalan!")
