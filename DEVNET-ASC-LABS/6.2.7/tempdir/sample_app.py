# Add to this file for the sample app lab

from flask import Flask
from flask import request
from flask import render_template

sample = Flask(__name__)

@sample.route("/")
def main():
    print("Started from Flask")
    print( "Python: You are calling me from " + request.remote_addr )
    return render_template("index.html")

if __name__ == "__main__":
    print("Started from Python shell")
    sample.run(host="0.0.0.0", port=8080)

