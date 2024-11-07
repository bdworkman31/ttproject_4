import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

df_vehicles = pd.read_csv('vehicles_us.csv')

st.header("Explore the Raw Data", divider = True)

st.write("Raw DataFrame:", df_vehicles)



fig = px.histogram(
    df_vehicles,
    x = 'days_listed',
    color = 'type'
)

fig.show()


"""
Next, we create a scatter plot for three variables in plotly: 
(1.) Price (2.) Odometer Reading (3.) Model_Year
Price is lowered to exclude outliers and make the graph more readable
As we can see from the graph, a newer year and lower odometer reading,
as one would suspect, yields a higher price typically
"""
df_vehicles['price'] = df_vehicles['price'][df_vehicles['price'] < 30000]
df_vehicles['odometer'] = df_vehicles['odometer'].dropna()

show_hist = st.checkbox("Show Histogram")
show_scatterplot = st.checkbox("Show Scatterplot")

if show_hist:
#Here is the histogram showing the amount of days listed per vehicle type:
    st.header(":blue[Histogram] Plot of Type vs Days Listed")
    
    fig = px.histogram(
    df_vehicles,
    x = 'days_listed',
    color = 'type'
    )
    
    st.plotly_chart(fig)

if show_scatterplot:
    st.header(":green[Scatterplot] Plot of Type vs Days Listed")
    
    fig1 = px.scatter(df_vehicles, x="model_year", y="odometer", color='price')
    st.plotly_chart(fig1)
    
