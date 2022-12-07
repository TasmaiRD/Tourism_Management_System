import pandas as pd
import streamlit as st
from database import view_users,view_user1,view_admin,view_all_admins,edit_user,get_user,edit_admin,get_admin,view_all_buses,view_all_flights,view_all_tragency,edit_agency,edit_bus,edit_flight,get_agency,get_bus,get_flight
#,view_all_hdata, view_only_h_names, get_hospitaldata

def update_user_info():
    result = view_users()
    df = pd.DataFrame(
        result, columns=['User ID', 'User Name','Age','Address','Phone','Admin Id'])
    with st.expander("Current Status of User:"):
        st.dataframe(df)
    list_of_users = [i[0] for i in view_user1()]
    selected_user = st.selectbox("Selected User", list_of_users)
    selected_result = get_user(selected_user)
    if selected_result:
        user_id = selected_result[0][0]
        username = selected_result[0][1]
        age = selected_result[0][2]
        address_user = selected_result[0][3]
        phone = selected_result[0][4]
        admin_id = selected_result[0][5]
        
        new_id = st.text_input("User ID:",user_id)
        new_username = st.text_input("User Name:",username)
        new_age=st.text_input("Age:",age)
        new_address=st.text_input("Address:",address_user)
        new_phone=st.text_input("Phone number:",phone)
        new_aid=st.text_input("Admin id:",admin_id)
        if st.button("Update User"):
            edit_user(new_id,new_username,new_age,new_address,new_phone,new_aid,user_id,username,age,address_user,phone,admin_id)
            st.success("Successfully updated {} to {}".format(username, new_username))
        result2 = view_users()
        df2 = pd.DataFrame(result2, columns=['User ID', 'User Name','Age','Address','Phone','Admin-id'])
    with st.expander("Updated data"):
        st.dataframe(df2)


def update_admin_entry():
    result = view_all_admins()
    df = pd.DataFrame(
        result, columns=['Admin ID', 'Admin Name'])
    with st.expander("Current Status of Admin:"):
        st.dataframe(df)
    list_of_admin = [i[0] for i in view_all_admins()]
    selected_admin = st.selectbox("Selected faculty", list_of_admin)
    selected_result = get_admin(selected_admin)
    if selected_result:
        admin_id = selected_result[0][0]
        admin_name = selected_result[0][1]
        
        new_id = st.text_input("Admin ID:",admin_id)
        new_name=st.text_input("Admin name:",admin_name)
   
        if st.button("Update Admin"):
            edit_admin(new_id,new_name,admin_id,admin_name)
            st.success("Successfully updated {} to {}".format(admin_name, new_name))
        result2 = view_admin()
        df2 = pd.DataFrame(result2, columns=['Admin ID', 'Admin Name'])
        with st.expander("Updated data"):
            st.dataframe(df2)

def update_agency_entry():
    result = view_all_tragency()
    df = pd.DataFrame(
        result, columns=['Agency ID', 'Agency Name','Phone number','Address','Agent Name','Admin Id'])
    with st.expander("Current Status of Agency:"):
        st.dataframe(df)
    list_of_agencies = [i[0] for i in view_all_tragency()]
    selected_ag = st.selectbox("Selected Agency", list_of_agencies)
    selected_result = get_agency(selected_ag)
    if selected_result:
        ta_id = selected_result[0][0]
        ag_name = selected_result[0][1]
        phone = selected_result[0][2]
        ag_address = selected_result[0][3]
        ag_person = selected_result[0][4]
        admin_id = selected_result[0][5]
        
        new_id = st.text_input("Agency ID:",ta_id)
        new_name = st.text_input("Agency Name:",ag_name)
        new_phone=st.text_input("Phone number:",phone)
        new_addr=st.text_input("Address:",ag_address)
        new_agent=st.text_input("Agent Name:",ag_person)
        new_aid=st.text_input("Admin id:",admin_id)
        if st.button("Update Agency details"):
            edit_agency(new_id,new_name,new_phone,new_addr,new_agent,new_aid,ta_id,ag_name,phone,ag_address,ag_person,admin_id)
            st.success("Successfully updated {} to {}".format(ag_name, new_name))
        result2 = view_all_tragency()
        df2 = pd.DataFrame(result2, columns=['Agency ID', 'Agency Name','Phone number','Address','Agent Name','Admin Id'])
    with st.expander("Updated data"):
        st.dataframe(df2)

def update_flight_entry():
    result = view_all_flights()
    df = pd.DataFrame(
        result, columns=['Flight ID', 'From Source','To Destination','Agency Id'])
    with st.expander("Current Status of Flight:"):
        st.dataframe(df)
    flight_list = [i[0] for i in view_all_flights()]
    sel_flight = st.selectbox("Selected Flight", flight_list)
    selected_result = get_flight(sel_flight)
    if selected_result:
        flight_id = selected_result[0][0]
        from_src = selected_result[0][1]
        to_dest = selected_result[0][2]
        ta_id = selected_result[0][3]

        new_id = st.text_input("Flight ID:",flight_id)
        new_src = st.text_input("From Source:",from_src)
        new_dest=st.text_input("To Destination:",to_dest)
        new_tid=st.text_input("Travel Agency Id:",ta_id)

        if st.button("Update Flight"):
            edit_flight(new_id,new_src,new_dest,new_tid,flight_id,from_src,to_dest,ta_id)
            st.success("Successfully updated {} details".format(flight_id))
        result2 = view_all_flights()
        df2 = pd.DataFrame(result2, columns=['Flight ID','From Source','To Destination','Agency Id'])
    with st.expander("Updated data"):
        st.dataframe(df2)

def update_Bus_entry():
    result = view_all_buses()
    df = pd.DataFrame(
        result, columns=['Bus ID', 'Arrival time','Departure time', 'Persons','Seats','StartDate','Destination','Agency Id'])
    with st.expander("Current Status of Agency:"):
        st.dataframe(df)
    bus_list = [i[0] for i in view_all_buses()]
    sel_bus = st.selectbox("Selected Bus details", bus_list)
    selected_result = get_bus(sel_bus)
    if selected_result:
        bus_id = selected_result[0][0]
        arrival_time = selected_result[0][1]
        depart_time = selected_result[0][2]
        no_of_person = selected_result[0][3]
        seats = selected_result[0][4]
        startDate = selected_result[0][5]
        destination = selected_result[0][6]
        ta_id = selected_result[0][7]
        
        new_id = st.text_input("Bus ID:",bus_id)
        new_arrival = st.text_input("Arrival Time:",arrival_time)
        new_depart=st.text_input("Departure Time:",depart_time)
        new_persons=st.text_input("No of Persons:",no_of_person)
        new_seats=st.text_input("Seats:",seats)
        new_Date=st.text_input("Start Date:",startDate)
        new_dest=st.text_input("Destination:",destination)
        new_tid=st.text_input("Agency Id:",ta_id)
        if st.button("Update Agency details"):
            edit_bus(new_id,new_arrival,new_depart,new_persons,new_seats,new_Date,new_dest,new_tid,bus_id,arrival_time,depart_time,no_of_person,seats,startDate,destination,ta_id)
            st.success("Successfully updated {} details".format(bus_id))
        result2 = view_all_buses()
        df2 = pd.DataFrame(result2, columns=['Bus ID', 'Arrival time','Departure time', 'Persons','Seats','StartDate','Destination','Agency Id'])
    with st.expander("Updated data"):
        st.dataframe(df2)