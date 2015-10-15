import os
import re
import random
import hashlib
from string import letters

from flask import Flask, render_template, request
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm.exc import MultipleResultsFound

###############################################################
###############################################################
###################### CONFIGURATION ##########################
###############################################################
###############################################################

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/pre-registration'
db = SQLAlchemy(app)


# from flask import Flask, render_template, request
# from flask.ext.sqlalchemy import SQLAlchemy

# from flask.ext.heroku import Heroku

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/pre-registration'
# heroku = Heroku(app)
# db = SQLAlchemy(app)




# Create our database model
class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True)
    given_name = db.Column(db.String(50)) #, nullable=False)
    family_name = db.Column(db.String(120)) #, nullable=False)
    pw_hash = db.Column(db.String(600)) #, nullable=False)


    def __init__(self, email, given_name, family_name, pw_hash):
        self.email = email
        self.given_name = given_name
        self.family_name = family_name
        self.pw_hash = pw_hash

    def __repr__(self):
        # return '<E-mail %r>' % self.email
        return '<id {}>'.format(self.id)
        # return self

###############################################################
###############################################################
###################### CONTROLLERS ############################
###############################################################
###############################################################
# Set "homepage" to index.html
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # Check that email does not already exist (not a great query, but works)
        if email and password:
            print "login"
            user = authenticate(email, password)
            print "authenticate user", user
            if user:
                return render_template('home.html', user = user)
        return render_template('index.html', login_email = email, login_error = "wrong username or password")
        # params['login_error'] = "incorrect username or password"

    

    return render_template('index.html')

# Register user and create an entry to the database. send to welcome page
@app.route('/register', methods=['POST'])
def register():
    email = None
    family_name = None
    given_name = None
    password = None

    if request.method == 'POST':
        have_error = False
        email = request.form['email']
        given_name = request.form['given_name']
        family_name = request.form['family_name']
        password = request.form['password']
        verify = request.form['verify']

        params = dict(email = email,
                given_name = given_name,
                family_name = given_name)    

        if not valid_name(given_name):
            params['error_given_name'] = "That's not a valid given name."
            have_error = True
        

        if not valid_name(family_name):
            params['error_family_name'] = "That's not a valid family name."
            have_error = True
        print "have_error2", have_error


        if not valid_password(password):
            params['error_password'] = "That wasn't a valid password."
            have_error = True
            
        elif password != verify:
            params['error_verify'] = "Your passwords didn't match."
            have_error = True
        print "have_error3", have_error

        print "email validation"
        if not valid_email(email):
            params['error_email'] = "That's not a valid email."
            have_error = True
        elif taken_email(email):
          params['error_email'] = "This email has already been taken."
          have_error = True
        print "have_error4", have_error



        # Check that email does not already exist (not a great query, but works)
        if not have_error:
            pw_hash = make_pw_hash(email, password)
            reg = User(email, given_name, family_name, pw_hash)
            db.session.add(reg)
            db.session.commit()
            return render_template('welcome.html', user = reg)

    return render_template('index.html', **params)


# Register user and create an entry to the database. send to welcome page
@app.route('/home', methods=['POST'])
def login():
    email = None

    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # Check that email does not already exist (not a great query, but works)
        if email and password:
            print "login"
            user = authenticate(email, password)
            print "authenticate user", user
            if user:
                return render_template('home.html', user = user)
        # params['login_error'] = "incorrect username or password"

    return render_template('index.html', login_email = email)





###############################################################
###############################################################
#################### SUPPORT METHODS ##########################
###############################################################
###############################################################
def authenticate(email, password):
    user = taken_email(email)
    if user:
        print "email", email
        print "password", password
        print "user.pw_hash", user.pw_hash
        if valid_pw(email, password, user.pw_hash):
            return user
    return None
    
def check_auth_cookie(cookie):
    pass


NAME_RE = re.compile(r"^[a-zA-Z-]{2,20}$")
def valid_name(name):
    return name and NAME_RE.match(name)

PASS_RE = re.compile(r"^.{4,20}$")
def valid_password(password):
    return password and PASS_RE.match(password)

EMAIL_RE  = re.compile(r'^[\S]+@[\S]+\.[\S]+$')
def valid_email(email):
    print "valid_email", email
    return not email or EMAIL_RE.match(email)

def taken_email(email):

    try:
        user = db.session.query(User).filter_by(email = email).one()
        print "user", repr(user)
        return user
    except MultipleResultsFound, e:
        return None
        # Deal with it
    except NoResultFound, e:
        return None
        # Deal with that as well

def check_email(email):
    return(taken_email(email))

def make_secure_val(val):
    return '%s|%s' % (val, hmac.new(SECRET, val).hexdigest())

def check_secure_val(secure_val):
    val = secure_val.split('|')[0]
    if secure_val == make_secure_val(val):
        return val

def make_salt(length = 20):
    return ''.join(random.choice(letters) for x in xrange(length))

def make_pw_hash(name, pw, salt = None):
    if not salt:
        salt = make_salt()
    h = hashlib.sha512(name + pw + salt).hexdigest() #it should be replaced with bcrypt or ADUCID
    return '%s|%s' % (salt, h)

def valid_pw(name, password, pw_hash):
    salt = pw_hash.split('|')[0]
    print "name", name
    print "password", password
    print "pw_hash", pw_hash
    print "salt", salt
    correct_pw_hash = make_pw_hash(name, password, salt)
    print "correct_pw_hash", correct_pw_hash
    print "pw_hash == correct_pw_hash", pw_hash == correct_pw_hash
    return pw_hash == correct_pw_hash



if __name__ == '__main__':
    app.debug = True
    app.run()