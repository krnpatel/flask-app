#Simplest app.py code for demo
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<img src=https://cataas.com/cat>"

@app.route("/hello")
def greetings():
    return "<html> <h1 style='color:red;'> <b> Good Morning - V4 </b></h1></html>"

@app.route("/kiran")
def greeHello():
    return "<html><h1 style='color:blue;'> Hello Kiran </h1></html>"

@app.route("/greet/<string:name>")
def getName(name):
    return f"<html><h1> Hello {name}</h1></html>"
    
if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8081)  #host="0.0.0.0",port=8081