import streamlit as st
from database import add_users, add_admin, add_tragency, add_flight, add_bus


def create_user():
    # col1 = st.columns(1)

    userid = st.text_input("User ID:")
    uname = st.text_input("User Name:")
    uage = st.text_input("Age")
    useraddr = st.text_input("Address:")
    uphone = st.text_input("Phone number:")
    uaid = st.text_input("Admin id for user:")

    if st.button("Add this User"):
        add_users(userid, uname, uage, useraddr, uphone, uaid)
        st.success("Successfully added.... Welcome aboard {}".format(uname))

# faculty data


def create_admin():

    id = st.text_input("Admin ID:")
    name = st.text_input("Enter Admin's Name:")

    if st.button("Add the Admin"):
        add_admin(id, name)
        st.success("Successfully added.... Welcome aboard {}".format(name))

# student course


def create_flight():
    col1, col2 = st.columns(2)
    with col1:
        flight_id = st.text_input("Flight ID:")
    with col2:
        from_src = st.text_input("Enter your Starting source:")
        to_dest = st.text_input("Enter your destination:")
        flight_taid = st.text_input("Travel agency ID:")

    if st.button("Add flight {} details ".format(flight_id)):
        add_flight(flight_id, from_src, to_dest, flight_taid)
        st.success("Successfully Added Flight {} details....".format(flight_id))

# faculty course


def create_tra_agency():
    col1, col2 = st.columns(2)
    with col1:
        ta_id = st.text_input("Travel agency id:")
        ag_name = st.text_input("Agency Name:")
        ag_person = st.text_input("Agency contact person:")
    with col2:
        ag_phone = st.text_input("Phone number:")
        ag_address = st.text_input("Address:")
        ta_aid = st.text_input("Admin id:")

    if st.button("Added agency {} ".format(ag_name)):
        add_tragency(ta_id, ag_name, ag_phone, ag_address, ag_person, ta_aid)
        st.success("Successfully added Travel agency {} details".format(ag_name))

# department


def create_bus():
    col1, col2 = st.columns(2)
    with col1:
        bus_id = st.text_input("Bus ID:")
        arrival_time = st.text_input("Arrival time:")
        depart_time = st.text_input("Departure time:")
    with col2:
        no_of_person = st.text_input("No. of persons:")
        seats = st.text_input("Seats:")
        startDate = st.text_input("Date of starting travel:")
        destination = st.text_input("Destination:")
        bus_taid = st.text_input("Travel agency Id:")
    if st.button("Add the Bus {} ".format(bus_id)):
        add_bus(bus_id, arrival_time, depart_time, no_of_person,
                seats, startDate, destination, bus_taid)
        st.success("Successfully added bus {} details".format(bus_id))
