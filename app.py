import os
import re
import random
import hashlib
from string import letters
import json

from flask import Flask, render_template, request, abort, json, jsonify, redirect
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm.exc import MultipleResultsFound

###############################################################
###############################################################
###################### CONFIGURATION ##########################
###############################################################
###############################################################
# this article shows the basics of postgre setup http://blog.sahildiwan.com/posts/flask-and-postgresql-app-deployed-on-heroku/
# good article about declaring data-types in sqlalchemy: https://pythonhosted.org/Flask-SQLAlchemy/models.html
# sqlalchemy postgresql data types http://docs.sqlalchemy.org/en/rel_0_9/dialects/postgresql.html#postgresql-data-types
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/pre-registration'
db = SQLAlchemy(app)



curricula_schools=db.Table('curricula_schools',                            
                             db.Column('curriculum_id', db.Integer,db.ForeignKey('curricula.id'), nullable=False),
                             db.Column('school_id',db.Integer,db.ForeignKey('schools.id'),nullable=False),
                             db.PrimaryKeyConstraint('curriculum_id', 'school_id') )

class School(db.Model):
    """docstring for School"""
    __tablename__ = 'schools'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable = False)
    street = db.Column(db.String(200), nullable = False)
    city = db.Column(db.String(200), nullable = False)
    county = db.Column(db.String(200), nullable = False)
    state = db.Column(db.String(200), nullable = False)
    postcode = db.Column(db.String(200), nullable = False)
    country = db.Column(db.String(100), nullable = False)
    web = db.Column(db.String(200), nullable = True, default="not available")
    phone = db.Column(db.String(20), nullable = True, default="not available")
    curricula = db.relationship("Curriculum", secondary=curricula_schools, backref='schools')

    def __init__(self, name, street, city, state, postcode, country, web, phone, county = "n/a"):
        self.name = name 
        self.street = street
        self.city = city 
        self.county = county
        self.state = state
        self.postcode = postcode
        self.country = country
        self.web = web 
        self.phone = phone
        
    def __repr__(self):
        # return '<E-mail %r>' % self.email
        return '<school_id {}>'.format(self.id)


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
    curricula = db.relationship("Curriculum", backref="standardcurriculum")
    

    def __init__(self, name, description, grade):
        self.name = name
        self.description = description
        self.grade = grade

    def __repr__(self):
        # return '<E-mail %r>' % self.email
        return '<standardcurriculum_id {}>'.format(self.id)

# used for customizing order and inclusion of courses, topics and subtopics
class Curriculum(db.Model):
    __tablename__ = 'curricula'
    # This id below should reference StandardCurriculum. Hence, define it as foreign key. 
    # Source: http://stackoverflow.com/questions/25189017/tablemodel-inheritance-with-flask-sqlalchemy
    # another example of inheritance and method override: http://snipplr.com/view/36330/ 
    id = db.Column(db.Integer, primary_key=True)
    standardcurriculum = db.Column(db.Integer, db.ForeignKey('standardcurriculum.id'))
    # using JSON column with postgresql http://stackoverflow.com/questions/23878070/using-json-type-with-flask-sqlalchemy-postgresql
    ordered_subtopics = db.Column(JSON)
#     ordered_subtopics = {"year_1" : {
#             "course_id" : { 
#                 "1" : "subtopic_id",
#                 "2" : "subtopic_id"
#             },
#             "course_id" : {
#                 "1" : "subtopic_id",
#                 "2" : "subtopic_id"   
#             }
#         }
#     }

    def __init__(self, standardcurriculum, customization_table):
        self.standardcurriculum = standardcurriculum.id
        self.customization_table = customization_table


    def __repr__(self):
        # return '<E-mail %r>' % self.email
        return '<curriculum_id {}>'.format(self.id)

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
        return '<course_id {}>'.format(self.id)

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
        self.topic_order = topic_order
        self.course_id = course_id

    def __repr__(self):
        # return '<E-mail %r>' % self.email
        return '<topic_id {}>'.format(self.id)

class Subtopic(db.Model):
    __tablename__ = 'subtopics'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable = False)
    description = db.Column(db.String(1000), nullable = True)
    year = db.Column(db.Integer, nullable = True) # this might need to be changed in order to personalize curricula
    subtopic_order = db.Column(db.Integer, nullable = True)
    hours =  db.Column(db.Float, nullable = True, default=0.0)
    topic_id = db.Column(db.Integer, db.ForeignKey('topics.id'))

    def __init__(self, name, description, subtopic_order,  topic_id, year = 0, hours = 0):
        self.name = name
        self.description = description
        self.year = year
        self.subtopic_order = subtopic_order
        self.hours = hours
        self.topic_id = topic_id

    def __repr__(self):
        # return '<E-mail %r>' % self.email
        return '<subtopic_id {}>'.format(self.id)

# flask module for user management: https://pythonhosted.org/Flask-User/customization.html
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
        return '<user_id {}>'.format(self.id)

        


###############################################################
###############################################################
#################### OUT CONTROLLERS ##########################
###############################################################
###############################################################
# Set "homepage" to index.html
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        email = request.form['email'].strip()
        password = request.form['password'].strip()

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
        email = request.form['email'].strip()
        given_name = request.form['given_name'].strip()
        family_name = request.form['family_name'].strip()
        password = request.form['password'].strip()
        verify = request.form['verify'].strip()

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

    return render_template('out/index.html')

###############################################################
###############################################################
################### ADMIN CONTROLLERS #########################
###############################################################
###############################################################
@app.route('/admin', methods=['GET'])
def admin():
    return render_template('admin/home/index.html')



@app.route('/admin/courses', methods=['GET'])
def courses():
    # try:  
        courses = db.session.query(Course).all()
        print "courses", repr(courses)
        return render_template('admin/courses/all.html', courses = courses)
    # except:
    #     return "ooops, what happened here?"
    #     # Deal with it

@app.route('/admin/courses/new', methods=['GET','POST', "PUT"])
def new_course():
    if request.method == 'PUT':

        # load json otherwise it will be unicode instead of a dictionary         
        content = json.loads(request.get_json())#["course"]
        print "content ", request.get_json()

        if not content:
            print "bad response format"
            abort(400)
        else:          
            course_name = content["course"]["course_name"]
            course_grade = content["course"]["course_grade"]
            course_description = content["course"]["course_description"]
            new_course = Course(name = course_name, grade = course_grade, description = course_description)
            db.session.add(new_course)
            db.session.commit()

            # iterating through keys and values of course
            for kc, vc in content["course"].items():    
                # if any key of the course starts with topic, create a new topic and...
                if kc.startswith("topic_"):
                    topic_name = vc["topic_name"]
                    topic_order = vc["topic_order"]
                    topic_description = vc["topic_description"]
                    new_topic = Topic(name = topic_name, description = topic_description, topic_order = topic_order, course_id = new_course.id)
                    db.session.add(new_topic)
                    db.session.commit()
                    print "new_topic", new_topic

                    # after topic is created iterating through all the keys and values of topic 
                    for kt, vt in vc.items():
                        # if any key of the topic starts with subtopic, create a new subtopic. Cycle will return to one up (looking for more subtopic, then looking for more topics)
                        if kt.startswith("subtopic_"):
                            subtopic_name = vt["subtopic_name"]
                            subtopic_order = vt["subtopic_order"]
                            subtopic_description = vt["subtopic_description"]
                            subtopic_year = vt["subtopic_year"]

                            subtopic_hours = vt["subtopic_hours"]
                            print "vt: ", vt
                            print "subtopic_year: ", subtopic_year
                            print "subtopic_hours: ", subtopic_hours

                            new_subtopic = Subtopic(name = subtopic_name, 
                                description = subtopic_description, 
                                subtopic_order = subtopic_order, 
                                topic_id = new_topic.id,
                                year = subtopic_year,
                                hours = subtopic_hours)
                            db.session.add(new_subtopic)
                            db.session.commit()
                            print "new_subtopic", new_subtopic

        #### these conditions are WRONG, i need to check all topics and subtopics        
        if new_subtopic and new_topic and new_course: 
            """
            write a function, which will revert changes if there has been a problem with creation of any item
            """
            pass
        return True


    elif request.method == 'POST':   
        return redirect("/admin/courses", code=302)
        # return render_template('admin/courses/all.html')
    else:
        return render_template('admin/courses/new.html')

@app.route('/admin/courses/<int:course_id>', methods=['GET'])
def view_course(course_id):
    course = db.session.query(Course).filter_by(id = course_id).one()
    return render_template('admin/courses/view.html', course = course)

@app.route('/admin/courses/<int:course_id>/edit', methods=['GET', 'POST'])
def edit_course(course_id):
    course = db.session.query(Course).filter_by(id = course_id).one()
    if request.method == 'POST':
        # load json otherwise it will be unicode instead of a dictionary         
        content = json.loads(request.get_json())#["course"]

        if not content:
            print "bad response format"
            abort(400)
        else:          
            course.name = content["course"]["course_name"]
            course.grade = content["course"]["course_grade"]
            course.description = content["course"]["course_description"]
            db.session.add(course)
            db.session.commit()
            # iterating through keys and values of course
            for kc, vc in content["course"].items():    
                # if any key of the course starts with topic, create a new topic and...
                if kc.startswith("topic_"):
                    topic = db.session.query(Topic).filter_by(id = kc.split("_")[-1]).one()
                    topic.name = vc["topic_name"]
                    topic.order = vc["topic_order"]
                    topic.description = vc["topic_description"]
                    db.session.add(topic)
                    db.session.commit()

                    # after topic is created iterating through all the keys and values of topic 
                    for kt, vt in vc.items():
                        # if any key of the topic starts with subtopic, create a new subtopic. Cycle will return to one up (looking for more subtopic, then looking for more topics)
                        if kt.startswith("subtopic_"):
                            subtopic = db.session.query(Subtopic).filter_by(id = kt.split("_")[-1]).one()
                            subtopic.name = vt["subtopic_name"]
                            subtopic.order = vt["subtopic_order"]
                            subtopic.description = vt["subtopic_description"]
                            if vt.has_key("subtopic_year"):
                                subtopic.year = vt["subtopic_year"]
                            if vt.has_key("subtopic_hours"):
                                subtopic.hours = vt["subtopic_hours"]
                            db.session.add(subtopic)
                            db.session.commit()

        #### these conditions are WRONG, i need to check all topics and subtopics        
        if subtopic and topic and course: 
            """
            write a function, which will revert changes if there has been a problem with creation of any item
            """
            pass


    course = db.session.query(Course).filter_by(id = course_id).one()
    for topic in course.topics:
        for subtopic in topic.subtopics:
            print "subtopic.hours: ", subtopic.hours
            print "subtopic.year: ", subtopic.year
    return render_template('admin/courses/edit.html', course = course)

@app.route('/admin/courses/<int:course_id>/delete', methods=['GET'])
def delete_course(course_id):
    course = db.session.query(Course).filter_by(id = course_id).one()
    db.session.delete(course)
    db.session.commit()
    return redirect("/admin/courses", code=302)


###############################################################
################### STANDARD CURRICULA ########################
###############################################################


@app.route('/admin/standard-curricula', methods=['GET'])
def standard_curricula():
    # try:  
        standardcurricula = db.session.query(StandardCurriculum).all()
        print "standardcurricula", repr(standardcurricula)
        for curriculum in standardcurricula:
            print "curriculum.name", curriculum.name
            print "curriculum.courses: ", curriculum.courses
        return render_template('admin/standard-curricula/all.html', standardcurricula = standardcurricula)
    # except:
    #     return "ooops, what happened here?"
    #     # Deal with it

@app.route('/admin/standard-curricula/new', methods=['GET', 'POST'])
def new_standard_curriculum():
    name = ""
    grade = ""
    description = ""
    selected_courses = ""

    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # i am not sure if this construct will reflect latter updates of the variables
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    params = dict(curriculum_name = name,
                grade = grade,
                curriculum_description = description) 

    if request.method == 'POST':   
        have_error = False
        name = request.form['curriculum_name'].strip()
        grade = request.form['curriculum_grade'].strip()
        description = request.form['curriculum_description'].strip()
        selected_courses = request.form.getlist('course')
        courses = []

        for course_id in selected_courses:
            course = db.session.query(Course).filter_by(id = course_id).one()
            courses.append(course)
            if course.grade != grade:
                have_error = True
                params['wrong_course_error'] = "At least one selected course doesn't belong to the curriculum's grade"

        # any_selected = bool(selected)
        if have_error:
            return render_template('admin/standard-curricula/new.html', **params)
        else:
            new_standard_curriculum = StandardCurriculum(name = name, grade = grade, description = description)
            
            for course in courses:
                #Add an association
                new_standard_curriculum.courses.append(course)
            db.session.add(new_standard_curriculum)
            db.session.commit()

        return redirect("/admin/standard-curricula", code=302)

    elif request.method == 'GET':
        params["courses"] = db.session.query(Course).all()
        return render_template('admin/standard-curricula/new.html', **params)

@app.route('/admin/standard-curricula/<int:standardcurriculum_id>', methods=['GET'])
def view_standard_curriculum(standardcurriculum_id):
    standardcurriculum = db.session.query(StandardCurriculum).filter_by(id = standardcurriculum_id).one()
    existing_courses = standardcurriculum.courses

    params = dict(curriculum_name = standardcurriculum.name,
                    grade = standardcurriculum.grade,
                    curriculum_description = standardcurriculum.description,
                    standardcurriculum_id = standardcurriculum.id,
                    courses = existing_courses) 
    
    return render_template('admin/standard-curricula/view.html', **params)

@app.route('/admin/standard-curricula/<int:standardcurriculum_id>/edit', methods=['GET', 'POST'])
def edit_standard_curriculum(standardcurriculum_id):
    name = ""
    grade = ""
    description = ""
    selected_courses = ""

    standardcurriculum = db.session.query(StandardCurriculum).filter_by(id = standardcurriculum_id).one()
    existing_courses = standardcurriculum.courses

    params = dict(curriculum_name = standardcurriculum.name,
                    grade = standardcurriculum.grade,
                    curriculum_description = standardcurriculum.description,
                    standardcurriculum_id = standardcurriculum.id,
                    couse = existing_courses) 
    if request.method == 'POST':  
        have_error = False

        name = request.form['curriculum_name'].strip()
        grade = request.form['curriculum_grade'].strip()
        description = request.form['curriculum_description'].strip()
        selected_courses = request.form.getlist('course')
        courses = []

        for course_id in selected_courses:
            course = db.session.query(Course).filter_by(id = course_id).one()
            courses.append(course)
            if course.grade != grade:
                have_error = True
                params['wrong_course_error'] = "At least one selected course doesn't belong to the curriculum's grade"
        
        if have_error:
            return render_template('admin/standard-curricula/edit.html', **params)
        else:
            standardcurriculum.name = name
            standardcurriculum.grade = grade
            standardcurriculum.description = description

            # editing multiple many-to-many relationships: http://stackoverflow.com/questions/7888900/how-to-remove-all-items-from-many-to-many-collection-in-sqlalchemy
            standardcurriculum.courses[:] = courses
            db.session.add(standardcurriculum)
            db.session.commit()
        return redirect("/admin/standard-curricula", code=302)

    else:# request.method == 'GET':  
        params["courses"] = db.session.query(Course).all()
        params["selected_courses"] = standardcurriculum.courses
        print 'params["selected_courses"]', params["selected_courses"]
        print 'params["courses"]', params["courses"]
        
        return render_template('admin/standard-curricula/edit.html', **params)

@app.route('/admin/standard-curricula/<int:standardcurriculum_id>/delete', methods=['GET'])
def delete_standard_curriculum(standardcurriculum_id):
    standardcurriculum = db.session.query(StandardCurriculum).filter_by(id = standardcurriculum_id).one()
    db.session.delete(standardcurriculum)
    db.session.commit()
    return redirect("/admin/standard-curricula", code=302)


###############################################################
########################## SCHOOLS ############################
###############################################################

@app.route('/admin/schools', methods=['GET'])
def schools():
    # try:  
    schools = db.session.query(School).all()
    print "schools", repr(schools)
    return render_template('admin/schools/all.html', schools = schools)
    # except:
    #     return "ooops, what happened here?"
    #     # Deal with it


@app.route('/admin/schools/new', methods=['GET', 'POST'])
def new_school():
    if request.method == 'GET':
        return render_template('admin/schools/new.html')
        # a list of countries/regions/cities http://stackoverflow.com/questions/6659269/api-or-database-to-load-data-for-country-state-province-region-and-city-select
        # http://www.freeformatter.com/iso-country-list-html-select.html
    
    if request.method == 'POST':
        name = request.form['school_name'].strip()
        street = request.form['school_street'].strip()
        city = request.form['school_city'].strip()
        postcode = request.form['school_postcode'].strip()
        state = request.form['school_region'].strip()
        country = request.form['school_country'].strip()
        web = request.form['school_web'].strip()
        phone = request.form['school_phone'].strip()

        if name and street and city and postcode and state and country:
            school = School(name = name, street = street, city = city, postcode = postcode, state = state, country = country, web = web, phone = phone)
            db.session.add(school)
            db.session.commit()
            return redirect("/admin/schools", code=302)
        else:
            return render_template('admin/schools/all.html', error = True, school_name = name, school_street = street, school_city = city, school_postcode = postcode, school_region = state, school_country = country, school_web = web, school_phone = phone)            


@app.route('/admin/schools/<int:school_id>/edit', methods=['GET', 'POST'])
def edit_school(school_id):
    print "school_id", school_id
    school = db.session.query(School).filter_by(id = school_id).one()

    if request.method == 'GET': 
        return render_template('admin/schools/edit.html', school = school)
    if request.method == 'POST':
        name = request.form['school_name'].strip()
        street = request.form['school_street'].strip()
        city = request.form['school_city'].strip()
        postcode = request.form['school_postcode'].strip()
        state = request.form['school_region'].strip()
        country = request.form['school_country'].strip()
        web = request.form['school_web'].strip()
        phone = request.form['school_phone'].strip()

        if name and street and city and postcode and state and country:
            school.name = name
            school.street = street
            school.city = city
            school.postcode = postcode
            school.state = state
            school.country = country
            school.web = web
            school.phone = phone

            db.session.add(school)
            db.session.commit()
            return redirect("/admin/schools", code=302)
        else:
            return render_template('admin/schools/all.html', error = True, school_name = name, school_street = street, school_city = city, school_postcode = postcode, school_region = state, school_country = country, school_web = web, school_phone = phone)            

@app.route('/admin/schools/<int:school_id>/', methods=['GET'])
def view_school(school_id):
    school = db.session.query(School).filter_by(id = school_id).one()
    return render_template('admin/schools/view.html', school = school)

@app.route('/admin/schools/<int:school_id>/delete', methods=['GET'])
def delete_school(school_id):
    school = db.session.query(School).filter_by(id = school_id).one()
    db.session.delete(school)
    db.session.commit()
    return redirect("/admin/schools", code=302)




###############################################################
##################### SCHOOL CURRICULA ########################
###############################################################

# @app.route('/admin/', methods=['GET'])
# def schools():
    # json = {standardcurriculum.id : {}}

    #     {"standardcurriculum_id" : {
    #         "course_id_1" : {
    #             "topic_id_1" : {
    #                 "subtopic_id_1" : {
    #                     "order" : 1,
    #                     "year" : 1
    #                 },
    #                 "subtopic_id_2" : {
    #                     "order" : 1,
    #                     "year" : 1
    #                 }
    #             }
    #         },
    #         "course_id_1" : {}
    #     }}

    #     curriculum.customization_table[standardcurriculum.id][course.id][topic.id][subtopic.id]['order']
    #     curriculum.customization_table[standardcurriculum.id][course.id][topic.id][subtopic.id]['year']
    #     for course in standardcurriculum.courses: 
    #         json[standardcurriculum.id] = {course.id : {}}
    #         for topic in course.topics:
    #             json[standardcurriculum.id][course.id] = {topic.id : {}}
    #             for subtopic in topic.subtopics:
    #                 json[standardcurriculum.id][course.id][topic.id] = {subtopic.id : {"order" : custom_order, "year" : custom_year}}
    #                 ordered_subtopics[custom_year][course.id][custom_order] = subtopic.id
    #                 # json[standardcurriculum.id] = {course.id : {topic.id : {subtopic.id : {"order" : custom_order, "year" : custom_year}}}}
    #     json[standardcurriculum.id][course.id][topic.id][subtopic.id]["order"] = custom_order
    #     json[standardcurriculum.id][course.id][topic.id][subtopic.id]["order"] = custom_year
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