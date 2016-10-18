from flask import render_template, redirect, request
from app import app, models, db
from .forms import CustomerForm


@app.route('/')
def index():
    return redirect('/create_customer')


@app.route('/create_customer', methods=['GET', 'POST'])
def create_customer():
    form = CustomerForm()
    # Capture form data and send to database
    if form.validate_on_submit():
        customer = models.Customer(
            company=form.company.data,
            email=form.email.data)
        db.session.add(customer)
        db.session.commit()
        return redirect('/customers')
    return render_template('customer.html', form=form)


@app.route('/customers')
def display_customer():
    # Fetch customer data from database
    customers = models.Customer.query.all()
    return render_template('home.html',
                           customers=customers)
