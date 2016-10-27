import sqlite3 as sql


def create_trip(name_of_trip, destination, friend1, friend2):
    ''' 
    Creates a trip entry to db
    '''
    with sql.connect("app.db") as con:
        cur = con.cursor()
        cur.execute("PRAGMA foreign_keys=ON;")
        try:
            cur.execute(
                "INSERT INTO trips (trip_name, destination, friend1, friend2) VALUES (?, ?, ?, ?)", (name_of_trip, destination, friend1, friend2))
            con.commit()
        except Exception as e:
            print("Error in inseting trip records: ", e)


def create_user(user_name, password):
    '''
    Creates a user entry to db
    '''
    with sql.connect("app.db") as con:
        cur = con.cursor()
        try:
            cur.execute(
                "INSERT INTO users (user_name, password) VALUES (?, ?)", (user_name, password))
            con.commit()
        except Exception as e:
            print("Error in inseting user records: ", e)


def retrieve_users():
    '''
    Retrieves users from db
    '''
    with sql.connect("app.db") as con:
        con.row_factory = sql.Row
        cur = con.cursor()
        users = cur.execute("SELECT * FROM users").fetchall()
    return users


def retrieve_trips():
    '''
    Retrieves trip details from db
    '''
    with sql.connect("app.db") as con:
        con.row_factory = sql.Row
        cur = con.cursor()
        trips = cur.execute(
            "SELECT * from trips").fetchall()
    return trips


def delete_trip(trip_name):
    '''
    Deletes trip details from db
    '''
    stmt = "DELETE FROM trips where trip_name = '" + trip_name + "'"
    with sql.connect("app.db") as con:
        cur = con.cursor()
        cur.execute(stmt)
        con.commit()
