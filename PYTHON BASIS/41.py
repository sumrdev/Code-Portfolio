from google.protobuf import message
import streamlit as st
from cryptography.fernet import Fernet
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd
import plotly as plt
key = Fernet.generate_key()
fernet = Fernet(key)
st.title("ENCRYPT MASTER")

st.write("ENCRYPT YOUR MESSAGE")
msg = st.text_input("Paste here what you want to encrypt")
encMsg = fernet.encrypt(msg.encode())
if st.button("CLICK HERE TO ENCRYPT"):
    st.write(encMsg)

st.write("DECRYPT A MESSAGE")
msg2 = st.text_input("Paste here what you want to decrypt")
if st.button("CLICK HERE TO DECRYPT"):
    dcMsg = fernet.decrypt(msg2.encode())
    st.write(dcMsg)