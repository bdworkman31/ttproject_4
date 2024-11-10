import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

df_vehicles = pd.read_csv('vehicles_us.csv')

st.header("Explore the Raw Data", divider = True)

st.write("Raw DataFrame:", df_vehicles)



# Check for Duplicated Values and null values
vehicle_duplicates = df_vehicles[df_vehicles.duplicated]

#Truncate the values for the model column to include just the maker of the car.  
# This provides a simplifed view; all models for each maker would make an extremely large amount of values on the respective axis
df_vehicles['model'] = df_vehicles['model'].apply(lambda x: x.split()[0])
print(df_vehicles['model'])

#Remove outliers from data
df_vehicles['price'] = df_vehicles['price'][df_vehicles['price'] < 30000]
df_vehicles['model_year'] = df_vehicles['model_year'][df_vehicles['model_year'] > 1980]
df_vehicles['odometer'] = df_vehicles['odometer'][df_vehicles['odometer'] < 400000]
df_vehicles['days_listed'] = df_vehicles['days_listed'][df_vehicles['days_listed'] < 120]

#Empty dataframe is returned, therefore there are no duplicates

#In the model_year column, we have null values.  Without these values, we cannot accurately assess a cars values, as there are notable differences between years 
#These empty columns will be changed the median per model
#Use transform function to add the median model year for each model to null values
model_median = df_vehicles.groupby('model')['model_year'].median()
df_vehicles['model_year'] = df_vehicles.groupby('model')['model_year'].transform(lambda x: x.fillna(model_median[x.name]))

odometer_mean = df_vehicles.groupby('model')['odometer'].mean()
df_vehicles['odometer'] = df_vehicles.groupby('model')['odometer'].transform(lambda x: x.fillna(odometer_mean[x.name]))

cylinders_median = df_vehicles.groupby('model')['cylinders'].median()
df_vehicles['cylinders'] = df_vehicles.groupby('model')['cylinders'].transform(lambda x: x.fillna(cylinders_median[x.name]))


#Check to see if the null values have been filled
df2 = df_vehicles['model_year'][df_vehicles['model_year'].isna()]
df3 = df_vehicles['odometer'][df_vehicles['odometer'].isna()]
df4 = df_vehicles['cylinders'][df_vehicles['cylinders'].isna()]

"""  """

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
    
