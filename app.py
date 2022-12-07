import streamlit as st
import mysql.connector
import pickle
import streamlit_authenticator as stauth
from create import (create_admin, create_user, create_bus, create_flight,
                    create_tra_agency)
from database import (create_admin_table, create_flight_table, create_bus_table, create_tragency_table,
                      create_user_table, delete_admin, edit_user)
from delete import (delete_admin, delete_user, view_all_admins, view_admin, delete_admin_entry, delete_user_entry,
                    view_users, view_user1, delete_agency, delete_ta_entry, delete_flight_entry, delete_bus_entry)
from read import (read_admins, read_all_agencies, read_buses, read_flights,
                  read_users)
from update import (update_admin_entry, view_admin, view_user1,
                    view_users, update_user_info, update_agency_entry, update_flight_entry, update_Bus_entry)
from query import query


def main():

    st.set_page_config(page_title="Online Tourism Management App")
    st.title("Online Tourism Management System")
    st.markdown(
        f"""
         <style>
         .stApp {{
             background-image: url("https://img.freepik.com/free-vector/india-architectural-skyline-poster_1284-14099.jpg?w=1380&t=st=1669441838~exp=1669442438~hmac=a0bd6cc8c3557a1b4ea9c87cdc4854b2335fa4132d4a3d2bbf11ac650e6ee594");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
        unsafe_allow_html=True
    )

    menu = ["Users", "Admins", "Travel agency", "Flights", "Bus", "Query Box"]
    choice = st.sidebar.selectbox("Menu", menu)
    create_user_table()
    create_admin_table()
    create_tragency_table()
    create_flight_table()
    create_bus_table()
    if choice == "Users":
        user_menu = ["Insert User", "View Users", "Edit Users", "Delete users"]
        user_choice = st.sidebar.selectbox("Operation", user_menu)
        if user_choice == "Insert User":
            # st.subheader("Enter New User details:")
            create_user()
        elif user_choice == "View Users":
            st.subheader("View User")
            read_users()
        elif user_choice == "Edit Users":
            # st.subheader("Edit User details")
            update_user_info()
        elif user_choice == "Delete users":
            # st.subheader("Delete User")
            delete_user_entry()
    elif choice == "Admins":
        admins_menu = ["Insert admin", "View admins",
                       "Edit admin", "Delete admin"]
        admin_choice = st.sidebar.selectbox("Operation", admins_menu)
        if admin_choice == "Insert admin":
            # st.subheader("Enter New admin details:")
            create_admin()
        elif admin_choice == "View admins":
            # st.subheader("View admin")
            read_admins()
        elif admin_choice == "Edit admin":
            # st.subheader("Edit admin details")
            update_admin_entry()
        elif admin_choice == "Delete admin":
            # st.subheader("Delete admin")
            delete_admin_entry()

    elif choice == "Travel agency":
        tr_menu = ["Insert Agency", "View agencies",
                   "Update Agency", "Delete Agency"]
        tr_choice = st.sidebar.selectbox("Operation", tr_menu)
        if tr_choice == "Insert Agency":
            # st.subheader("Enter New Agency details:")
            create_tra_agency()
        elif tr_choice == "View agencies":
            # st.subheader("View agencies")
            read_all_agencies()
        elif tr_choice == "Update Agency":
            update_agency_entry()
        elif tr_choice == "Delete Agency":
            delete_ta_entry()

    elif choice == "Flights":
        fl_menu = ["Insert flight", "View flights",
                   "Edit Flight", "Delete Flights"]
        fl_choice = st.sidebar.selectbox("Operation", fl_menu)
        if fl_choice == "Insert flight":
            # st.subheader("Enter New flight details:")
            create_flight()
        elif fl_choice == "View flights":
            # st.subheader("View flights")
            read_flights()
        elif fl_choice == "Edit Flight":
            update_flight_entry()
        elif fl_choice == "Delete Flights":
            delete_flight_entry()

    elif choice == "Bus":
        bus_menu = ["Insert Bus", "View Buses", "Edit Bus", "Delete Bus"]
        bus_choice = st.sidebar.selectbox("Operation", bus_menu)
        if bus_choice == "Insert Bus":
            # st.subheader("Enter New Bus details:")
            create_bus()
        elif bus_choice == "View Buses":
            # st.subheader("View flights")
            read_buses()
        elif bus_choice == "Edit Bus":
            update_Bus_entry()
        elif bus_choice == "Delete Bus":
            delete_bus_entry()

    elif choice == "Query Box":
        # st.subheader="Query Box"
        query()


if __name__ == main():
    main()
