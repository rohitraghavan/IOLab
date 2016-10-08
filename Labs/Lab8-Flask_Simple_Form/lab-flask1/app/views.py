from app import myapp
from flask import request,render_template

@myapp.route('/')
@myapp.route('/index')
def index():
    print("This is a log ..comes on your console")
    return "Hello  - this the page for your form !!"

