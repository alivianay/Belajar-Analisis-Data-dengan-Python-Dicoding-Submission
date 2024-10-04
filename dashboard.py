import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import folium
from datetime import datetime

# Load your dataset
df_day_cleaned = pd.read_csv('bike_sharing_cleaned.csv')  # Make sure this matches your dataset name

# Set up the Streamlit app layout
st.title("Bike Sharing Analysis Dashboard")

# Section for Overview
st.header("Overview of Bike Rentals")
st.write(df_day_cleaned)

# RFM Analysis Section
st.header("RFM Analysis")

# Assuming 'last_rental_date' and 'user_id' columns are present in your dataset
# Create a simulated last_rental_date for demonstration purposes (you can modify this)
df_day_cleaned['last_rental_date'] = pd.to_datetime('2024-10-04')  # Example date for recency calculation

# Calculate Recency, Frequency, and Monetary
if 'last_rental_date' in df_day_cleaned.columns:
    df_day_cleaned['Recency'] = (datetime.now() - df_day_cleaned['last_rental_date']).dt.days
    df_rfm = df_day_cleaned.groupby('user_id').agg({
        'Recency': 'min',
        'cnt': 'count',  # Frequency
        'total_spent': 'sum'  # Monetary, if available
    }).reset_index()

    st.write(df_rfm)

    # RFM Scatter Plot
    st.subheader("RFM Scatter Plot")
    fig, ax = plt.subplots()
    sns.scatterplot(data=df_rfm, x='Recency', y='cnt', size='total_spent', sizes=(20, 200), alpha=0.5, ax=ax)
    plt.title("RFM Analysis")
    st.pyplot(fig)

# Geospatial Analysis Section
st.header("Geospatial Analysis")

# Example: If you had a dataset with latitude and longitude
if 'latitude' in df_day_cleaned.columns and 'longitude' in df_day_cleaned.columns:
    st.subheader("Bike Rental Locations")
    
    # Create a map centered around the average location
    m = folium.Map(location=[df_day_cleaned['latitude'].mean(), df_day_cleaned['longitude'].mean()], zoom_start=12)
    
    for idx, row in df_day_cleaned.iterrows():
        folium.CircleMarker(
            location=(row['latitude'], row['longitude']),
            radius=5,
            color='blue',
            fill=True,
            fill_color='blue',
            fill_opacity=0.6,
            popup=f'Count: {row["cnt"]}'
        ).add_to(m)
    
    st.write(m)

# Clustering Analysis Section
st.header("Clustering Analysis")

# Manual Grouping Example
st.subheader("Bike Rentals by Weather Conditions")
weather_grouping = df_day_cleaned.groupby(['temp_category', 'hum_category']).agg({'cnt': 'mean'}).reset_index()
st.write(weather_grouping)

# Visualization for Clustering Results
fig, ax = plt.subplots()
sns.barplot(data=weather_grouping, x='temp_category', y='cnt', hue='hum_category', ax=ax)
plt.title("Average Bike Rentals by Weather Conditions")
st.pyplot(fig)

# Final Note: Add any additional analyses as necessary

# To run the app, use: streamlit run dashboard.py in your command line
