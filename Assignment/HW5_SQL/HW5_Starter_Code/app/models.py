import sqlite3 as sql


def insert_customer(customer, address):
    # SQL statement to insert into database goes here
    with sql.connect("app.db") as con:
        cur = con.cursor()
        cur.execute(
            "INSERT INTO customers (first_name, last_name, company, email, phone) VALUES (?, ?, ?, ?, ?)", (customer[
                'first_name'], customer['last_name'], customer['company'], customer['email'], customer['phone']))
        customer_id = cur.lastrowid
        cur.execute(
            "INSERT INTO address (street_address, city, state, country, zip_code, customer_id) VALUES (?, ?, ?, ?, ?, ?)", (address[
                'street_address'], address['city'], address['state'], address['country'], address['zip_code'], customer_id))
        con.commit()


def add_address(address, customer_id):
    # SQL statement to insert into database goes here
    with sql.connect("app.db") as con:
        cur = con.cursor()
        cur.execute(
            "INSERT INTO address (street_address, city, state, country, zip_code, customer_id) VALUES (?, ?, ?, ?, ?, ?)", (address[
                'street_address'], address['city'], address['state'], address['country'], address['zip_code'], customer_id))
        con.commit()


def insert_order(name_of_part, manufacturer_of_part, customer_id):
    # SQL statement to insert into database goes here
    with sql.connect("app.db") as con:
        cur = con.cursor()
        order_result = cur.execute(
            "select * from order_details where name_of_part=? and manufacturer_of_part=?", (name_of_part, manufacturer_of_part)).fetchall()

        if(len(order_result)) > 0:
            # Order already exists, associate with customer
            order_id = order_result[0][0]
            cur.execute(
                "INSERT INTO customer_orders (customer_id, order_id) VALUES (?, ?)", (customer_id, order_id))
        else:
            # Order is new. Create order and associate with customer
            cur.execute(
                "INSERT INTO order_details (name_of_part, manufacturer_of_part) VALUES (?, ?)", (name_of_part, manufacturer_of_part))
            order_id = cur.lastrowid
            cur.execute(
                "INSERT INTO customer_orders (customer_id, order_id) VALUES (?, ?)", (customer_id, order_id))
        con.commit()


def retrieve_data():
    # SQL statement to query database goes here
    with sql.connect("app.db") as con:
        con.row_factory = sql.Row
        cur = con.cursor()
        customers = cur.execute("select * from customers").fetchall()
        addresses = cur.execute("select * from address").fetchall()
        orders = cur.execute(
            "select * from order_details od, customer_orders co where od.order_id = co.order_id").fetchall()
    return customers, addresses, orders
