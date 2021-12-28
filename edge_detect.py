import cv2
import numpy as np
import streamlit as st

max = st.slider('max', 0, 500)
min = st.slider('min', 0, max)
img = cv2.imread('lenna.jpg', -1)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
canny_img = cv2.Canny(img_gray, min, max)
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        if canny_img[i, j] != 0:
            img[i, j, :] = 0
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
st.image(img, channels='RGB')