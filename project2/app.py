#Simplest app.py code for demo
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<html> <h1 style='color:yellow;'> <b> Good Morning - Project2 - V6 </b></h1></html>"

@app.route("/kiran")
def greeHello():
    return "<html><h1 style='color:blue;'> Hello Kiran, This is Project2 </h1></html>"
    
if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8081)  #host="0.0.0.0",port=8081