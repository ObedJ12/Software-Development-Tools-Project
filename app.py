# app.py

import streamlit as st
import pandas as pd
import plotly.express as px

# Load dataset
df = pd.read_csv("your_dataset.csv")  # Replace with your actual CSV file name

# Header
st.header("Random Event Simulator Dashboard")

# Histogram
st.subheader("Distribution of a Column")
selected_column = st.selectbox("Choose a column for histogram", df.columns)
hist = px.histogram(df, x=selected_column)
st.plotly_chart(hist)

# Scatter Plot
st.subheader("Scatter Plot Viewer")
x_axis = st.selectbox("X-axis", df.columns, index=0)
y_axis = st.selectbox("Y-axis", df.columns, index=1)
scatter = px.scatter(df, x=x_axis, y=y_axis)
st.plotly_chart(scatter)

# Checkbox: Show raw data
if st.checkbox("Show raw data"):
    st.subheader("Raw Data")
    st.write(df)
