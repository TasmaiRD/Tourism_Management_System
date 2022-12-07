import pandas as pd
import streamlit as st
from database import view_users,view_user1,view_all_admins,view_admin,delete_user,delete_admin,view_all_tragency,delete_agency,view_all_flights,view_all_buses,delete_flight,delete_bus

def delete_user_entry():
    result = view_users()
    df = pd.DataFrame(result, columns=['User ID', 'User Name', 'Age', 'Address','Phone number','Admin-id'])
    with st.expander("Present Users data"):
        st.dataframe(df)
    list_of_users = [i[0] for i in view_user1()]
    selected_user= st.selectbox("Deleting record", list_of_users)
    st.warning("Do you want to delete record {}".format(selected_user))
    if st.button("Delete User record"):
        delete_user(selected_user)
        st.success("User record has been deleted successfully")
    new_result = view_users()
    df2 = pd.DataFrame(new_result, columns=['User ID', 'User Name', 'Age', 'Address','Phone number','Admin-id'])
    with st.expander("Updated data"):
        st.dataframe(df2)

def delete_admin_entry():
    result = view_admin()
    df = pd.DataFrame(result, columns=['Admin ID', 'Admin Name'])
    with st.expander("Present Admin Data"):
        st.dataframe(df)
    list_of_admin = [i[0] for i in view_admin()]
    selected_admin= st.selectbox("Deleting record", list_of_admin)
    st.warning("Do you want to delete record {}".format(selected_admin))
    if st.button("Delete Admin's record"):
        delete_admin(selected_admin)
        st.success("Admin record has been deleted successfully")
    new_result = view_all_admins()
    df2 = pd.DataFrame(new_result, columns=['Admin ID', 'Admin Name'])
    with st.expander("Updated data"):
        st.dataframe(df2)
        
def delete_ta_entry():
    result = view_all_tragency()
    df = pd.DataFrame(result, columns=['Agency ID', 'Agency Name','Phone number','Address','Agent Name','Admin Id'])
    with st.expander("Present Agency Data"):
        st.dataframe(df)
    list_of_agencies = [i[0] for i in view_all_tragency()]
    selected_agency= st.selectbox("Deleting record ", list_of_agencies)
    st.warning("Do you want to delete record {}".format(selected_agency))
    if st.button("Delete Agency's record"):
        delete_agency(selected_agency)
        st.success("Agency record has been deleted successfully")
    new_result = view_all_tragency()
    df2 = pd.DataFrame(new_result, columns=['Agency ID', 'Agency Name','Phone number','Address','Agent Name','Admin Id'])
    with st.expander("Updated data"):
        st.dataframe(df2)

def delete_flight_entry():
    result = view_all_flights()
    df = pd.DataFrame(result, columns=['Flight ID', 'From Source','To Destination','Agency Id'])
    with st.expander("Present Flights Data"):
        st.dataframe(df)
    list_of_flights = [i[0] for i in view_all_flights()]
    selected_flight= st.selectbox("Deleting record ", list_of_flights)
    st.warning("Do you want to delete record {}".format(selected_flight))
    if st.button("Delete Flight's record"):
        delete_flight(selected_flight)
        st.success("Flight record has been deleted successfully")
    new_result = view_all_flights()
    df2 = pd.DataFrame(new_result, columns=['Flight ID', 'From Source','To Destination','Agency Id'])
    with st.expander("Updated data"):
        st.dataframe(df2)
        
        
def delete_bus_entry():
    result = view_all_buses()
    df = pd.DataFrame(result, columns=['Bus ID', 'Arrival time','Departure time', 'Persons','Seats','StartDate','Destination','Agency Id'])
    with st.expander("Present Bus Data"):
        st.dataframe(df)
    list_of_buses = [i[0] for i in view_all_buses()]
    selected_bus= st.selectbox("Deleting record ", list_of_buses)
    st.warning("Do you want to delete record {}".format(selected_bus))
    if st.button("Delete Bus's record"):
        delete_bus(selected_bus)
        st.success("Bus record has been deleted successfully")
    new_result = view_all_buses()
    df2 = pd.DataFrame(new_result, columns=['Bus ID', 'Arrival time','Departure time', 'Persons','Seats','StartDate','Destination','Agency Id'])
    with st.expander("Updated data"):
        st.dataframe(df2)
