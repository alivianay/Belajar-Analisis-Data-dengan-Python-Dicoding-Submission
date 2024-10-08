import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import os

# Load data
# Construct the file path
current_directory = os.path.dirname(__file__)
csv_file_path = os.path.join(current_directory, 'bike_sharing_cleaned.csv')

if not os.path.exists(csv_file_path):
    st.error("The CSV file was not found. Please check the file path.")
else:
    df_day_cleaned = pd.read_csv(csv_file_path)

################   DEFINE VAR  ############# 

# Calculating average rentals by temperature, humidity, and windspeed categories
weather_impact_temp = df_day_cleaned.groupby('temp_category').agg({'cnt': 'mean'})
weather_impact_hum = df_day_cleaned.groupby('hum_category').agg({'cnt': 'mean'})
weather_impact_wind = df_day_cleaned.groupby('windspeed_category').agg({'cnt': 'mean'})

# Grouping by weekday and working day
day_pattern = df_day_cleaned.groupby(['weekday', 'workingday']).agg({
    'cnt': 'mean',
    'temp': 'mean',
    'hum': 'mean',
    'windspeed': 'mean'
})

# Grouping by holidays
holiday_effect = df_day_cleaned.groupby('holiday').agg({
    'cnt': 'mean',
    'temp': 'mean',
    'hum': 'mean',
    'windspeed': 'mean'
})

# Cluster analysis data
cluster_analysis = df_day_cleaned.groupby(['temp_category', 'hum_category']).agg({'cnt': 'mean'}).reset_index()

# Monthly rentals
monthly_rentals = df_day_cleaned.groupby('month').agg({'cnt': 'mean'}).reset_index()

# Seasonal rentals
seasonal_rentals = df_day_cleaned.groupby('season').agg({'cnt': 'mean'}).reset_index()

# Rentals by working day and weather condition
working_weather_rentals = df_day_cleaned.groupby(['weathersit', 'workingday']).agg({'cnt': 'mean'}).reset_index()

# Layout
st.title("🚴‍♂️ Bike Sharing Analysis Dashboard")

# Sidebar navigation
st.sidebar.header("Navigation")
st.sidebar.text("Select a section to view:")
overview_option = st.sidebar.button("Overview")
rfm_analysis_option = st.sidebar.button("RFM Analysis")
weather_conditions_option = st.sidebar.button("Weather Conditions Impact")
clustering_analysis_option = st.sidebar.button("Clustering Analysis")
additional_analysis_option = st.sidebar.button("Additional Weather Impact")

# Overview Section
if overview_option:
    st.header("Overview of Bike Rentals")
    st.write("This dashboard provides insights into bike rental patterns based on weather conditions and rental timings.")
    st.write(df_day_cleaned)

'''Ini udah include at least 2 visualisai yang sama yang ada di dashboard'''

# RFM Analysis Section
if rfm_analysis_option:
    st.header("📊 RFM Analysis")
    st.write("RFM analysis evaluates customer behavior based on Recency, Frequency, and Monetary value.")

    # Simulated last_rental_date for demonstration purposes
    df_day_cleaned['last_rental_date'] = pd.to_datetime('2024-10-04')  # Example date for recency calculation

    # Calculate Recency and Frequency
    if 'last_rental_date' in df_day_cleaned.columns:
        df_day_cleaned['Recency'] = (datetime.now() - df_day_cleaned['last_rental_date']).dt.days
        df_rfm = df_day_cleaned.groupby('instant').agg({
            'Recency': 'min',
            'cnt': 'count'  # Frequency
        }).reset_index()

        st.subheader("RFM Summary")
        st.write(df_rfm)

        # RFM Scatter Plot
        st.subheader("RFM Scatter Plot")
        fig, ax = plt.subplots()
        sns.scatterplot(data=df_rfm, x='Recency', y='cnt', alpha=0.7, ax=ax)
        plt.title("RFM Analysis: Recency vs Frequency")
        st.pyplot(fig)  # Pass the figure object

# Weather Conditions Impact Section > Ini ada di dashboard
if weather_conditions_option:
    st.header("🌦️ Weather Conditions Impact on Rentals")
    st.write("This section analyzes how various weather conditions impact bike rental demand.")

    # Plotting the impact of temperature on bike rentals
    st.subheader("Impact of Temperature on Bike Rentals")
    fig, ax = plt.subplots()
    sns.barplot(data=df_day_cleaned, x='temp_category', y='cnt', ax=ax, hue='temp_category', palette='coolwarm', legend=False)
    plt.title("Average Bike Rentals by Temperature Category")
    plt.xlabel("Temperature Category")
    plt.ylabel("Average Bike Rentals")
    st.pyplot(fig)  # Pass the figure object

    # Plotting the impact of humidity on bike rentals
    st.subheader("Impact of Humidity on Bike Rentals")
    fig, ax = plt.subplots()
    sns.barplot(data=df_day_cleaned, x='hum_category', y='cnt', ax=ax, hue='hum_category', palette='viridis', legend=False)
    plt.title("Average Bike Rentals by Humidity Category")
    plt.xlabel("Humidity Category")
    plt.ylabel("Average Bike Rentals")
    st.pyplot(fig)  # Pass the figure object

    # Plotting the impact of windspeed on bike rentals
    st.subheader("Impact of Windspeed on Bike Rentals")
    fig, ax = plt.subplots()
    sns.barplot(data=df_day_cleaned, x='windspeed_category', y='cnt', ax=ax, hue='windspeed_category', palette='magma', legend=False)
    plt.title("Average Bike Rentals by Windspeed Category")
    plt.xlabel("Windspeed Category")
    plt.ylabel("Average Bike Rentals")
    st.pyplot(fig)  # Pass the figure object

# Clustering Analysis Section > Clusterring ada di dashboard
if clustering_analysis_option:
    st.header("🔍 Clustering Analysis")
    st.write("Analyzing bike rentals based on weather conditions by grouping the data to observe patterns.")

    # Grouping by weather conditions
    st.subheader("Bike Rentals by Weather Conditions")
    st.write(cluster_analysis)

    # Visualization for Clustering Results
    fig, ax = plt.subplots()
    sns.barplot(data=cluster_analysis, x='temp_category', y='cnt', hue='hum_category', ax=ax, palette='crest')
    plt.title("Average Bike Rentals by Weather Conditions")
    st.pyplot(fig)  # Pass the figure object

# Additional Analysis Section: Visualize Weather Impact
if additional_analysis_option:
    st.header("📅 Additional Analysis of Weather and Holiday Impact")
    
    # Average bike rentals by temperature
    st.subheader("Average Bike Rentals by Temperature")
    fig, ax = plt.subplots()
    weather_impact_temp['cnt'].plot(kind='bar', title="Average Bike Rentals by Temperature", ax=ax)
    st.pyplot(fig)  # Pass the figure object

    # Average bike rentals by humidity
    st.subheader("Average Bike Rentals by Humidity")
    fig, ax = plt.subplots()
    weather_impact_hum['cnt'].plot(kind='bar', title="Average Bike Rentals by Humidity", ax=ax)
    st.pyplot(fig)  # Pass the figure object

    # Average bike rentals by windspeed
    st.subheader("Average Bike Rentals by Windspeed")
    fig, ax = plt.subplots()
    weather_impact_wind['cnt'].plot(kind='bar', title="Average Bike Rentals by Windspeed", ax=ax)
    st.pyplot(fig)  # Pass the figure object

    # Visualize weekday and working day pattern
    st.subheader("Average Bike Rentals by Weekday and Working Day")
    fig, ax = plt.subplots()
    day_pattern['cnt'].unstack().plot(kind='bar', title="Average Bike Rentals by Weekday and Working Day", ax=ax)
    st.pyplot(fig)  # Pass the figure object

    # Visualize holiday effect
    st.subheader("Average Bike Rentals on Holidays vs Non-Holidays")
    fig, ax = plt.subplots()
    holiday_effect['cnt'].plot(kind='bar', title="Average Bike Rentals on Holidays vs Non-Holidays", ax=ax)
    st.pyplot(fig)  # Pass the figure object

    # Visualize temperature and humidity cluster impact
    st.subheader("Impact of Temperature and Humidity Clusters on Bike Rentals")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x='temp_category', y='cnt', hue='hum_category', data=cluster_analysis, ax=ax)
    plt.title('Average Bike Rentals Based on Temperature and Humidity Clusters')
    st.pyplot(fig)  # Pass the figure object

    # Visualize bike rentals by month
    st.subheader("Average Bike Rentals by Month")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.lineplot(x='month', y='cnt', data=monthly_rentals, marker='o', ax=ax)
    plt.title("Average Bike Rentals by Month")
    st.pyplot(fig)  # Pass the figure object

    # Visualize bike rentals by season
    st.subheader("Average Bike Rentals by Season")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x='season', y='cnt', data=seasonal_rentals, ax=ax)
    plt.title("Average Bike Rentals by Season")
    st.pyplot(fig)  # Pass the figure object

    # Visualize bike rentals by working day and weather condition
    st.subheader("Average Bike Rentals by Weather Condition and Working Day")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x='weathersit', y='cnt', hue='workingday', data=working_weather_rentals, ax=ax)
    plt.title("Average Bike Rentals by Weather Condition and Working Day")
    st.pyplot(fig)  # Pass the figure object

#footer
st.write("Hope this dashboard helps!")