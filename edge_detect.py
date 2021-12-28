import cv2
import numpy as np
import streamlit as st
import base64

max = st.slider('max', 0, 500)
min = st.slider('min', 0, 500)
img = st.file_uploader('imge pls:')
if img != None:
    img_b = base64.b64encode(img.read())
    imD = base64.b64decode(img_b)
    nparr = np.fromstring(imD, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    canny_img = cv2.Canny(img_gray, min, max)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if canny_img[i, j] != 0:
                img[i, j, :] = 0
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    st.image(img, channels='RGB')