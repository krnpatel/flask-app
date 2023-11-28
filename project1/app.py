#Simplest app.py code for demo
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<html> <h1 style='color:red;'> <b> Good Morning - Project1 - V5 </b></h1></html>"

@app.route("/kiran")
def greeHello():
    return "<html><h1 style='color:yellow;'> Hello Kiran, This is Project1 </h1></html>"
    
if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8081)  #host="0.0.0.0",port=8081