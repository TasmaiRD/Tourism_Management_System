import pandas as pd
import streamlit as st
from database import view_users, view_all_admins, view_all_buses, view_all_flights, view_all_tragency
# ,view_all_hdata


def read_users():
    result = view_users()
    # st.write(result)
    df = pd.DataFrame(result, columns=[
                      'User ID', 'User Name', 'Age', 'Address', 'Phone number', 'Admin Id'])
    with st.expander("View all User Details"):
        st.dataframe(df)


def read_admins():
    result = view_all_admins()
    # st.write(result)
    df = pd.DataFrame(result, columns=['Admin ID', 'Admin Name'])
    with st.expander("View all Admins"):
        st.dataframe(df)


def read_all_agencies():
    result = view_all_tragency()
    # st.write(result)
    df = pd.DataFrame(result, columns=[
                      'Travel Agency Id', 'Agency Name', 'Phone number', 'Address', 'Agent Name', 'Admin Id'])
    with st.expander("View all Agencies"):
        st.dataframe(df)


def read_flights():
    result = view_all_flights()
    # st.write(result)
    df = pd.DataFrame(result, columns=[
                      'Flight ID', 'From source', 'To Destination', 'Travel agency Id'])
    with st.expander("View all Flights"):
        st.dataframe(df)


def read_buses():
    result = view_all_buses()
    # st.write(result)
    df = pd.DataFrame(result, columns=['Bus ID', 'Arrival time', 'Departure time',
                      'No. of persons', 'Seats', 'Start Date', 'Destination', 'Travel Agency Id'])
    with st.expander("View all Bus information"):
        st.dataframe(df)
