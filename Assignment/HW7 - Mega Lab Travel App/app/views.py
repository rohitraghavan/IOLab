from flask import render_template, redirect, request, session, escape, json
from app import app, models, db
from .forms import *
from .models import *


@app.route('/')
@app.route('/home', methods=['GET', 'POST'])
def display_trips():
    '''
    Displays trips for the logged in user
    '''
    current_user = ""
    if 'username' in session:
        current_user = escape(session['username'])
        trips = retrieve_trip_data(current_user)
        return render_template('home.html', trips=trips, user=current_user)
    else:
        return redirect('login')


def retrieve_trip_data(current_user):
    trips = []
    trip_rows = models.retrieve_trips()
    for trip_row in trip_rows:
        if trip_row['friend1'] == current_user or trip_row['friend2'] == current_user:
            trips.append(trip_row)
    return trips


@app.route('/login', methods=['GET', 'POST'])
def login():
    '''
    Authenticates and logs in user
    '''
    login_form = LoginForm()
    if login_form.validate_on_submit():
        # Get data from the form
        user_name = login_form.user_name.data
        password = login_form.password.data
        # Authenticate user
        if authenticate_user(user_name, password):
            session['username'] = user_name
            return redirect('home')
        else:
            return redirect('login')

    return render_template('login.html', form=login_form)


def authenticate_user(user_name, password):
    '''
    Retrieves users from db to authenticate attempted login
    '''
    user_rows = models.retrieve_users()
    for user_row in user_rows:
        if user_row['user_name'] == user_name and user_row['password'] == password:
            return True
    return False


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    session.pop('username')
    return redirect('login')


@app.route('/create_user', methods=['GET', 'POST'])
def create_user():
    '''
    Creates a new user entry in db
    '''
    signup_form = SignupForm()
    if signup_form.validate_on_submit():
        # Get data from the form
        user_name = signup_form.user_name.data
        password = signup_form.password.data
        # Send data from form to Database
        models.create_user(user_name, password)
        return redirect('login')

    return render_template('signup.html', form=signup_form)


@app.route('/create_trip', methods=['GET', 'POST'])
def create_trip():
    '''
    Creates a new trip entry in db
    '''
    if 'username' in session:
        current_user = escape(session['username'])
        trip_form = TripForm()
        trip_form.friend2.choices = retrieve_users()
        if trip_form.validate_on_submit():
            # Get data from the form
            name_of_trip = trip_form.name_of_trip.data
            destination = trip_form.destination.data
            friend2 = trip_form.friend2.data

            # Send data from form to Database
            models.create_trip(name_of_trip, destination,
                               current_user, friend2)
            return redirect('home')

        return render_template('trip.html', form=trip_form, user=current_user)

    else:
        return redirect('login')


def retrieve_users():
    '''
    Retrieves users from db to display in Friends dropdown in Create User page. 
    Remove currently logged in user from the list
    '''
    user_rows = models.retrieve_users()
    users = []
    current_user = ""
    if 'username' in session:
        current_user = escape(session['username'])
    for user_row in user_rows:
        if user_row['user_name'] == current_user:
            continue
        users.append(user_row['user_name'])

    return [(user, user) for user in users]


@app.route('/delete_trip', methods=['GET', 'POST'])
def delete_trip():
    '''
    Deletes trip row from the db
    '''
    print("Invoked!")
    responseJson = request.get_json(force=True)
    models.delete_trip(responseJson['tripName'].strip())

    return json.dumps({'status': 'OK'})
