import mysql.connector
mydb = mysql.connector.connect(
    host="localhost", user="root", password="", database="tourism_602")
c = mydb.cursor()


def create_user_table():
    c.execute('CREATE TABLE IF NOT EXISTS users (user_id TEXT,username TEXT,age TEXT,address_user TEXT,phone TEXT)')


def add_users(user_id, username, age, address_user, phone, admin_id):
    c.execute('INSERT INTO users(user_id,username,age,address_user,phone,admin_id) '
              'VALUES (%s,%s,%s,%s,%s,%s)',
              (user_id, username, age, address_user, phone, admin_id))
    mydb.commit()


def view_users():
    c.execute('SELECT * FROM users')
    data = c.fetchall()
    return data


def get_user(user_id):
    c.execute('SELECT * FROM users WHERE user_id="{}"'.format(user_id))
    data = c.fetchall()
    return data


def view_user1():
    c.execute('SELECT user_id,username,phone FROM users')
    data = c.fetchall()
    return data


def edit_user(new_id, new_name, new_age, new_addr, new_phone, new_aid, user_id, username, age, address_user, phone, admin_id):
    c.execute("UPDATE users SET user_id=%s,username=%s,age=%s,address_user=%s,phone=%s,admin_id=%s" "WHERE user_id=%s and username=%s and age=%s and address_user=%s and phone=%s and admin_id=%s",
              (new_id, new_name, new_age, new_addr, new_phone, new_aid, user_id, username, age, address_user, phone, admin_id))
    mydb.commit()
    data = c.fetchall()
    return data


def delete_user(user_id):
    c.execute('DELETE FROM users WHERE user_id="{}"'.format(user_id))


# database for faculty

def create_admin_table():
    c.execute('CREATE TABLE IF NOT EXISTS  admin_t(admin_id TEXT, admin_name TEXT)')


def add_admin(admin_id, admin_name):
    c.execute('INSERT INTO admin_t(admin_id,admin_name) '
              'VALUES (%s,%s)',
              (admin_id, admin_name))
    mydb.commit()


def view_all_admins():
    c.execute('SELECT * FROM admin_t')
    data = c.fetchall()
    return data


def view_admin():
    c.execute('SELECT admin_id,admin_name FROM admin_t')
    data = c.fetchall()
    return data


def get_admin(admin_id):
    c.execute('SELECT * FROM admin_t WHERE admin_id="{}"'.format(admin_id))
    data = c.fetchall()
    return data


def edit_admin(new_id, new_name, admin_id, admin_name):
    c.execute("UPDATE admin_t SET admin_id=%s,admin_name=%s" "WHERE admin_id=%s and admin_name=%s",
              (new_id, new_name, admin_id, admin_name))
    mydb.commit()
    data = c.fetchall()
    return data


def delete_admin(admin_id):
    c.execute('DELETE FROM admin_t WHERE admin_id="{}"'.format(admin_id))


# database for travel agency

def create_tragency_table():
    c.execute(
        'CREATE TABLE IF NOT EXISTS tragency(ag_name TEXT,phone TEXT,ag_address TEXT,ag_person TEXT)')


def add_tragency(ta_id, ag_name, phone, ag_address, ag_person, admin_id):
    c.execute('INSERT INTO tragency(ta_id,ag_name,phone,ag_address,ag_person,admin_id) '
              'VALUES (%s,%s,%s,%s,%s,%s)',
              (ta_id, ag_name, phone, ag_address, ag_person, admin_id))
    mydb.commit()


def view_all_tragency():
    c.execute('SELECT * FROM tragency')
    data = c.fetchall()
    return data

# def view_admin():
#     c.execute('SELECT admin_id,admin_name FROM admin_t')
#     data = c.fetchall()
#     return data


def get_agency(ta_id):
    c.execute('SELECT * FROM tragency WHERE ta_id="{}"'.format(ta_id))
    data = c.fetchall()
    return data


def edit_agency(new_id, new_name, new_phone, new_addr, new_agent, new_aid, ta_id, ag_name, phone, ag_address, ag_person, admin_id):
    c.execute("UPDATE tragency SET ta_id=%s,ag_name=%s,phone=%s,ag_address=%s,ag_person=%s,admin_id=%s" "WHERE ta_id=%s and ag_name=%s and phone=%s and ag_address=%s and ag_person=%s and admin_id=%s",
              (new_id, new_name, new_phone, new_addr, new_agent, new_aid, ta_id, ag_name, phone, ag_address, ag_person, admin_id))
    mydb.commit()
    data = c.fetchall()
    return data


def delete_agency(ta_id):
    c.execute('DELETE FROM tragency WHERE ta_id="{}"'.format(ta_id))


# database for flight details

def create_flight_table():
    c.execute(
        'CREATE TABLE IF NOT EXISTS  flight(flight_id TEXT, from_src TEXT, to_dest TEXT,ta_id TEXT)')


def add_flight(flight_id, from_src, to_dest, ta_id):
    c.execute('INSERT INTO flight(flight_id, from_src, to_dest,ta_id) '
              'VALUES (%s,%s,%s,%s)',
              (flight_id, from_src, to_dest, ta_id))
    mydb.commit()


def view_all_flights():
    c.execute('SELECT * FROM flight')
    data = c.fetchall()
    return data


def get_flight(f_id):
    c.execute('SELECT * FROM flight WHERE flight_id="{}"'.format(f_id))
    data = c.fetchall()
    return data


def edit_flight(new_id, new_src, new_dest, new_tid, flight_id, from_src, to_dest, ta_id):
    c.execute("UPDATE flight SET flight_id=%s,from_src=%s,to_dest=%s,ta_id=%s" "WHERE flight_id=%s and from_src=%s and to_dest=%s and ta_id=%s",
              (new_id, new_src, new_dest, new_tid, flight_id, from_src, to_dest, ta_id))
    mydb.commit()
    data = c.fetchall()
    return data


def delete_flight(f_id):
    c.execute('DELETE FROM flight WHERE flight_id="{}"'.format(f_id))


# database for bus

def create_bus_table():
    c.execute('CREATE TABLE IF NOT EXISTS  bus(bus_id TEXT, arrival_time TEXT,depart_time TEXT,no_of_person TEXT, seats TEXT,startDate TEXT,destination TEXT)')


def add_bus(bus_id, arrival_time, depart_time, no_of_person, seats, startDate, destination, ta_id):
    c.execute('INSERT INTO bus(bus_id, arrival_time,depart_time,no_of_person,seats,startDate, destination,ta_id) '
              'VALUES (%s,%s,%s,%s,%s,%s,%s,%s)',
              (bus_id, arrival_time, depart_time, no_of_person, seats, startDate, destination, ta_id))
    mydb.commit()


def view_all_buses():
    c.execute('SELECT * FROM bus')
    data = c.fetchall()
    return data


def get_bus(b_id):
    c.execute('SELECT * FROM bus WHERE bus_id="{}"'.format(b_id))
    data = c.fetchall()
    return data


def edit_bus(new_id, new_arrival, new_depart, new_persons, new_seats, new_Date, new_dest, new_tid, bus_id, arrival_time, depart_time, no_of_person, seats, startDate, destination, ta_id):
    c.execute("UPDATE bus SET bus_id=%s,arrival_time=%s,depart_time=%s,no_of_person=%s,seats=%s,startDate=%s,destination=%s,ta_id=%s" "WHERE bus_id=%s and arrival_time=%s and depart_time=%s and no_of_person=%s and seats=%s and startDate=%s and destination=%s and ta_id=%s",
              (new_id, new_arrival, new_depart, new_persons, new_seats, new_Date, new_dest, new_tid, bus_id, arrival_time, depart_time, no_of_person, seats, startDate, destination, ta_id))
    mydb.commit()
    data = c.fetchall()
    return data


def delete_bus(bid):
    c.execute('DELETE FROM bus WHERE bus_id="{}"'.format(bid))
