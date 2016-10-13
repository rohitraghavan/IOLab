from flask import render_template, redirect, request
from app import app, models, db
from .forms import CustomerForm, OrderForm, AddressForm
# Access the models file to use SQL functions


@app.route('/')
def index():
    return redirect('/create_customer')


@app.route('/create_customer', methods=['GET', 'POST'])
def create_customer():
    form = CustomerForm()
    if form.validate_on_submit():
        # Get data from the form
        customer = {}
        customer['first_name'] = form.first_name.data
        customer['last_name'] = form.last_name.data
        customer['company'] = form.company.data
        customer['email'] = form.email.data
        customer['phone'] = form.phone.data

        address = {}
        address['street_address'] = form.street_address.data
        address['city'] = form.city.data
        address['state'] = form.state.data
        address['country'] = form.country.data
        address['zip_code'] = form.zip_code.data
        # Send data from form to Database
        models.insert_customer(customer, address)
        return redirect('/customers')
    return render_template('customer.html', form=form)


@app.route('/create_order/<value>', methods=['GET', 'POST'])
def create_order(value):
    order_form = OrderForm()
    if order_form.validate_on_submit():
        # Get data from the form
        name_of_part = order_form.name_of_part.data
        manufacturer_of_part = order_form.manufacturer_of_part.data
        # Send data from form to Database
        models.insert_order(name_of_part, manufacturer_of_part, value)
        return redirect('/customers')
    return render_template('order.html', form=order_form)


@app.route('/add_address/<value>', methods=['GET', 'POST'])
def add_address(value):
    address_form = AddressForm()
    if address_form.validate_on_submit():
        # Get data from the form
        address = {}
        address['street_address'] = address_form.street_address.data
        address['city'] = address_form.city.data
        address['state'] = address_form.state.data
        address['country'] = address_form.country.data
        address['zip_code'] = address_form.zip_code.data
        # Send data from form to Database
        models.add_address(address, value)
        return redirect('/customers')
    return render_template('address.html', form=address_form)


@app.route('/customers')
def display_customer():
    # Retreive data from database to display
    customers, addresses, orders = models.retrieve_data()
    return render_template('home.html', customers=customers, addresses=addresses, orders=orders)