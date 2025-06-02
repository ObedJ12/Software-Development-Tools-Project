# app.py

import streamlit as st
import pandas as pd
import plotly.express as px
import os

# Load dataset
df = pd.read_csv("vehicles_us.csv")

# Header
st.header("Random Event Simulator Dashboard")

# Fill missing model_year
df['model_year'] = df.groupby('model')['model_year'].transform(lambda x: x.fillna(x.median()))

# Fill missing cylinders
df['cylinders'] = df.groupby('model')['cylinders'].transform(lambda x: x.fillna(x.median()))

# Fill missing odometer
df['model_year_str'] = df['model_year'].astype(str)
df['model_yr_key'] = df['model'] + '_' + df['model_year_str']
df['odometer'] = df.groupby('model_yr_key')['odometer'].transform(lambda x: x.fillna(x.median()))
df.drop(columns=['model_year_str', 'model_yr_key'], inplace=True)

# Remove outliers
df = df[df['price'].between(df['price'].quantile(0.01), df['price'].quantile(0.99))]
df = df[df['model_year'].between(df['model_year'].quantile(0.01), df['model_year'].quantile(0.99))]

# Create scatter plot
fig = px.scatter(df, x='model_year', y='price', color='type', title='Price vs Model Year')
plot_html = fig.to_html(full_html=False)
 return render_template_string("""
    <html>
        <head><title>Vehicle Dashboard</title></head>
        <body>
            <h1>📊 Price vs Model Year</h1>
            {{ plot_div|safe }}
        </body>
    </html>
    """, plot_div=plot_html)

if __name__ == "__main__":
    app.run(debug=True)

