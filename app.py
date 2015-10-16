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
# example taken from http://techarena51.com/index.php/many-to-many-relationships-with-flask-sqlalchemy/
standardcurricula_courses=db.Table('standardcurricula_courses',                            
                             db.Column('standardcurriculum_id', db.Integer,db.ForeignKey('standardCurricula.id'), nullable=False),
                             db.Column('course_id',db.Integer,db.ForeignKey('courses.id'),nullable=False),
                             db.PrimaryKeyConstraint('standardcurriculum_id', 'course_id') )


class StandardCurriculum(db.Model):
    __tablename__ = 'standardCurricula'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique= True, nullable = False)
    description = db.Column(db.Text, nullable = True)
    grade = db.Column(db.String(100), nullable = False)
    

    def __init__(self, name, description, grade):
        self.name = name
        self.description = description
        self.grade = grade

    def __repr__(self):
        # return '<E-mail %r>' % self.email
        return '<id {}>'.format(self.id)

# # used for customizing order and inclusion of courses, topics and subtopics
# class SchoolCurriculum(StandardCurriculum):
#     __tablename__ = 'schoolCurricula'
#     # This id below should reference StandardCurriculum. Hence, define it as foreign key. 
#     # Source: http://stackoverflow.com/questions/25189017/tablemodel-inheritance-with-flask-sqlalchemy
#     id = db.Column(db.Integer, ForeignKey('standardcurriculum.id'), primary_key=True)
#     current_balance = db.Column(db.Float)

# class CourseGroup(object):
#     """
#     CourseGroup could serve as an unifying connection between the same courses in different 
#     grades - e.g. mathematics on elementary school would be linked to mathematics on secodnary, 
#     high- and university courses
#     """
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100), nullable = False)
#     description = db.Column(db.Text, nullable = True)
#     category = db.Column(db.List) # check if list exists. this should hold info on categories eg natural sciences, social sciences etc.
#     #i need to add "coursegroup_id" to course class in order to complete it

#     def __init__(self, arg):
#         self.arg = arg
        

class Course(db.Model):
    __tablename__ = 'courses'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable = False)
    description = db.Column(db.Text, nullable = True)
    grade = db.Column(db.String(100), nullable = False)
    standardCurricula = db.relationship("StandardCurriculum", secondary=standardcurricula_courses, backref='courses')
    topics = db.relationship("Topic", backref="course")

    def __init__(self, name, description, grade):
        self.name = name
        self.description = description
        self.grade = grade

    def __repr__(self):
        # return '<E-mail %r>' % self.email
        return '<id {}>'.format(self.id)

class Topic(db.Model):
    __tablename__ = 'topics'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable = False)
    description = db.Column(db.Text, nullable = True)
    topic_order = db.Column(db.Integer, nullable = True)
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'))
    subtopics = db.relationship("Subtopic", backref="topic")

    def __init__(self, name, description, topic_order, course_id):
        self.name = name
        self.description = description
        self.year = year
        self.topic_order = topic_order
        self.course_id = course_id

    def __repr__(self):
        # return '<E-mail %r>' % self.email
        return '<id {}>'.format(self.id)

class Subtopic(db.Model):
    __tablename__ = 'subtopics'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable = False)
    description = db.Column(db.String(1000), nullable = True)
    year = db.Column(db.Integer, nullable = True)
    subtopic_order = db.Column(db.Integer, nullable = True)
    hours =  db.Column(db.Float, nullable = True, default=0.0)
    topic_id = db.Column(db.Integer, db.ForeignKey('topics.id'))

    def __init__(self, name, description, year, subtopic_order, hours, topic_id):
        self.name = name
        self.description = description
        self.year = year
        self.subtopic_order = subtopic_order
        self.hours = hours
        self.topic_id = topic_id

    def __repr__(self):
        # return '<E-mail %r>' % self.email
        return '<id {}>'.format(self.id)

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
            user = authenticate(email, password)
            
            if user:
                return render_template('student/home.html', user = user)
        return render_template('out/index.html', login_email = email, login_error = "incorrect username or password")

    return render_template('out/index.html')

# Register user and create an entry to the database. send to welcome page
@app.route('/register', methods=['GET', 'POST'])
def register():
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
            return render_template('student/welcome.html', user = reg)

    return render_template('out/asdf@asdf.as.html')


@app.route('/admin', methods=['GET'])
def admin():
    return render_template('admin/home/index.html')



@app.route('/admin/courses', methods=['GET'])
def courses():
    try:
        courses = db.session.query(Course).all()
        print "courses", repr(courses)
        return render_template('admin/courses/all.html', courses = courses)
    except:
        return "ooops, what happened here?"
        # Deal with it

@app.route('/admin/courses/new', methods=['GET'])
def new_course():
    return render_template('admin/courses/new.html')

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