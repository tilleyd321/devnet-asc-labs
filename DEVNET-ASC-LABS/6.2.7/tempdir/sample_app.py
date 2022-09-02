# Add to this file for the sample app lab

from flask import Flask
from flask import request
from flask import render_template

sample = Flask(__name__)


@sample.route("/dave")
def myFunc1():
    f = open("Func1-app.log", "w")
    count = 10
    while (count): 
      f.write("Dave: Is running {}\n".format(count))
      count = count - 1
    f.close()
    return render_template("dave.html")

@sample.route("/joe")
def myFunc2():
    print("Joe: Run this instead")
    return render_template("joe.html")



@sample.route("/")
def main():
    print( "Python: You are calling me from " + request.remote_addr )
    return render_template("index.html")

if __name__ == "__main__":
    sample.run(host="0.0.0.0", port=8080)

