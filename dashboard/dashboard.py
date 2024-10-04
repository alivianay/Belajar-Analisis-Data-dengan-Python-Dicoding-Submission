import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# Load data
df_day_cleaned = pd.read_csv('bike_sharing_cleaned.csv')


# Title layout
st.title("🚴‍♂️ Bike Sharing Analysis Dashboard")

# Sidebar navigation
st.sidebar.header("Navigation")
st.sidebar.text("Select a section to view:")
overview_option = st.sidebar.button("Overview")
rfm_analysis_option = st.sidebar.button("RFM Analysis")
weather_conditions_option = st.sidebar.button("Weather Conditions Impact")
clustering_analysis_option = st.sidebar.button("Clustering Analysis")

# Overview Section
if overview_option:
    st.header("Overview of Bike Rentals")
    st.write("This dashboard provides insights into bike rental patterns based on weather conditions and rental timings.")
    st.write(df_day_cleaned)

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
        st.pyplot(fig)

# Weather Conditions Impact Section
if weather_conditions_option:
    st.header("🌦️ Weather Conditions Impact on Rentals")
    st.write("This section analyzes how various weather conditions impact bike rental demand.")

    # Plotting the impact of temperature on bike rentals
    st.subheader("Impact of Temperature on Bike Rentals")
    fig, ax = plt.subplots()
    sns.barplot(data=df_day_cleaned, x='temp_category', y='cnt', ax=ax, palette='coolwarm')
    plt.title("Average Bike Rentals by Temperature Category")
    plt.xlabel("Temperature Category")
    plt.ylabel("Average Bike Rentals")
    st.pyplot(fig)

    # Plotting the impact of humidity on bike rentals
    st.subheader("Impact of Humidity on Bike Rentals")
    fig, ax = plt.subplots()
    sns.barplot(data=df_day_cleaned, x='hum_category', y='cnt', ax=ax, palette='viridis')
    plt.title("Average Bike Rentals by Humidity Category")
    plt.xlabel("Humidity Category")
    plt.ylabel("Average Bike Rentals")
    st.pyplot(fig)

    # Plotting the impact of windspeed on bike rentals
    st.subheader("Impact of Windspeed on Bike Rentals")
    fig, ax = plt.subplots()
    sns.barplot(data=df_day_cleaned, x='windspeed_category', y='cnt', ax=ax, palette='magma')
    plt.title("Average Bike Rentals by Windspeed Category")
    plt.xlabel("Windspeed Category")
    plt.ylabel("Average Bike Rentals")
    st.pyplot(fig)

# Clustering Analysis Section
if clustering_analysis_option:
    st.header("🔍 Clustering Analysis")
    st.write("Analyzing bike rentals based on weather conditions by grouping the data to observe patterns.")

    # Grouping by weather conditions
    st.subheader("Bike Rentals by Weather Conditions")
    weather_grouping = df_day_cleaned.groupby(['temp_category', 'hum_category']).agg({'cnt': 'mean'}).reset_index()
    st.write(weather_grouping)

    # Visualization for Clustering Results
    fig, ax = plt.subplots()
    sns.barplot(data=weather_grouping, x='temp_category', y='cnt', hue='hum_category', ax=ax, palette='crest')
    plt.title("Average Bike Rentals by Weather Conditions")
    st.pyplot(fig)

# Final Note
st.write("tolonk jangan eror")
