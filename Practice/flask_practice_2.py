#November 2016 Deborah Leem for CFG project
#Flask DB

from flask import Flask
from flask import render_template
from flask import request
import os
import sqlite3

app = Flask("MyApp")

def connect_db():
    """Connects to the specific database."""
    rv = sqlite3.connect("CFG_DB")
    rv.row_factory = sqlite3.Row
    return rv

@app.route("/")
def hello():
    sqlite_db = connect_db()
    users = sqlite_db.execute('select name, email, language from users order by name').fetchall()
    #the following line to be reviewed 
    sqlite_db.close()

    return render_template("hello.html", users=users)

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


