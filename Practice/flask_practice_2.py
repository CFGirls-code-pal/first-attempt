from flask import Flask
from flask import render_template
from flask import request

app = Flask("MyApp")

@app.route("/")
def hello():
	return render_template("hello.html")

# @app.route("/<name>")
# def hello_again(name):
# 	return render_template("hello.html", name = name.title())

@app.route("/signup", methods=['GET'])
def hello_again():
	return "This is the get method being called"

@app.route("/signup", methods=['POST'])
def sign_up():
	form_data = request.form
	print (form_data['name'])
	print (form_data['email'])
	return "All OK"
	


app.run()