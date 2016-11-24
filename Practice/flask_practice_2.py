#November 2016 Deborah Leem for CFG project
#Flask DB

from flask import Flask
from flask import render_template
from flask import request
from flask import g
import sqlite3

app = Flask("MyApp")

#to do: get the right path
DATABASE = '/path/to/database.db'

def connect_db():
    return sqlite3.connect("CFG_DB")

@app.before_request
def before_request():
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    if hasattr(g, 'db'):
        g.db.close()

#@app.route("/")
#def hello():
#    sqlite_db = connect_db()
#    users = sqlite_db.execute('select name, email, language from users order by name').fetchall()
    #the following line to be reviewed 
#    sqlite_db.close()

#    return render_template("hello.html", users=users)

# @app.route("/<name>")
# def hello_again(name):
#   return render_template("hello.html", name = name.title())

@app.route("/signup", methods=['GET'])
def hello_again():
    return "This is the get method being called"

@app.route("/signup", methods=['POST'])
def sign_up():
    form_data = request.form
    print (form_data['name'])
    print (form_data['email'])
    print (form_data['language'])
    return "All OK"
    
app.run()


