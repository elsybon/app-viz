import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import streamlit as st
import random
from PIL import Image

image_c= Image.open('cour.png')
st.image(image_c, width=500)

st.title("Coursera Stats")
st.sidebar.header("Dashboard")
st.sidebar.markdown("---")

df = pd.read_csv("coursera.csv")
st.markdown("## Visualization")
tab1, tab2= st.tabs(["Line Chart", "Bar Chart"])

tab1.subheader("Line Chart")
tab1.line_chart(data=df, x="Rating", y="Number of Review", width=0, height=0, use_container_width=True)

tab2.subheader("Bar Chart")
tab2.bar_chart(data=df, x="Number of Review", y="Rating", use_container_width=True)
