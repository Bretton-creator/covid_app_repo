import streamlit as st
import numpy as np
import pandas as pd
import time
import plotly.express as px

st.title('Covid-19 Cases Analysis')

df = pd.read_csv('time_series_covid_19_confirmed.csv')

df = df.drop(columns=["Province/State", "Lat", "Long"])
df = df.groupby("Country/Region").aggregate(np.sum).T
df.index.name = "Date"
df = df.reset_index()
melt_c_df = df.melt(
    id_vars=["Date"], var_name="Country", value_name='Confirmed')
melt_c_df["Date"] = pd.to_datetime(melt_c_df["Date"])
max_date = melt_c_df["Date"].max()
total_c_df = melt_c_df[melt_c_df["Date"] == max_date]
country = total_c_df['Country']

st.write("""
## Confirmed Cases
""")


option = st.sidebar.selectbox('Select Country', country)
cases = total_c_df.loc[total_c_df["Country"] == option]
cases = cases["Confirmed"].max()
st.write(f"Total cases: {cases}")
line_chart = px.line(
    melt_c_df[melt_c_df["Country"] == option], x="Date", y="Confirmed")
st.plotly_chart(line_chart)

st.write("""
## Death Cases """)

death_df = pd.read_csv('time_series_covid_19_deaths.csv')
death_df = death_df.drop(columns=["Province/State", "Lat", "Long"])
death_df = death_df.groupby("Country/Region").aggregate(np.sum).T
death_df.index.name = "Date"
death_df = death_df.reset_index()
melt_death_df = death_df.melt(
    id_vars=["Date"], var_name="Country", value_name="Deaths")
melt_death_df["Date"] = pd.to_datetime(melt_death_df["Date"])
max_date = melt_death_df["Date"].max()
total_death_df = melt_death_df[melt_death_df["Date"] == max_date]
cases = total_death_df.loc[total_death_df["Country"] == option]
cases = cases["Deaths"].max()
st.write(f"Total Deaths: {cases}")
line_chart = px.line(
    melt_death_df[melt_death_df["Country"] == option], x="Date", y="Deaths")
st.plotly_chart(line_chart)

st.write(""" 
## Recovered Cases
""")

recovered_df = pd.read_csv('time_series_covid_19_recovered.csv')
recovered_df = recovered_df.drop(columns=["Province/State", "Lat", "Long"])
recovered_df = recovered_df.groupby("Country/Region").aggregate(np.sum).T
recovered_df.index.name = "Date"
recovered_df = recovered_df.reset_index()
melt_recovered_df = recovered_df.melt(
    id_vars=["Date"], var_name="Country", value_name="Recovered")
melt_recovered_df["Date"] = pd.to_datetime(melt_recovered_df["Date"])
max_date = melt_recovered_df["Date"].max()
total_recovered_df = melt_recovered_df[melt_recovered_df["Date"] == max_date]
cases = total_recovered_df.loc[total_recovered_df["Country"] == option]
cases = cases["Recovered"].max()
st.write(f"Total Recovered: {cases}")
line_chart = px.line(
    melt_recovered_df[melt_recovered_df["Country"] == option], x="Date", y="Recovered")
st.plotly_chart(line_chart)
