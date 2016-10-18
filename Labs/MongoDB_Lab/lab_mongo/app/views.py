from app import myapp, model
from flask import request, render_template, session, redirect, url_for, escape
import os

myapp.secret_key = os.urandom(24)


@myapp.route('/')
@myapp.route('/index')
def index():
    username = ''
    if 'username' in session:
        username = escape(session['username'])
        return render_template('survey.html', name=username)
    else:
        return render_template('login.html')


@myapp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        session['email'] = request.form['email']
        return redirect(url_for('index'))


@myapp.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('email', None)
    return redirect(url_for('index'))


@myapp.route('/aggregate')
def newpage():
    if 'username' in session:
        username = escape(session['username'])
    else:
        username = 'Guest'
    # Fetch Data to calculate the average

    # calculate score

    return render_template('aggregate.html', name=username, score_before=avg_score_before, score_after=avg_score_after, count=total_responses)


@myapp.route('/submit-survey', methods=['GET', 'POST'])
def submitSurvey():
    username = ''
    email = ''
    if 'username' in session:
        username = escape(session['username'])
        email = escape(session['email'])
        surveyResponse = {}
        surveyResponse['color'] = request.form.get('color')
        surveyResponse['food'] = request.form.get('food')
        surveyResponse['vacation'] = request.form.get('vacation')
        surveyResponse['fe-before'] = request.form.get('feBefore')
        surveyResponse['fe-after'] = request.form.get('feAfter')
        # new fields for comments and focus
        model.insertRecords(username, email, surveyResponse)

        return render_template('results.html', name=username, email=email, surveyResponse=surveyResponse)
    else:
        return render_template('login.html')


@myapp.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404
