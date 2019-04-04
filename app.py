from flask import Flask
import datetime
app = Flask(__name__)

@app.route("/")
def hello():
    now = datetime.datetime.now()
    return ("Hello World! %s" %(now))
