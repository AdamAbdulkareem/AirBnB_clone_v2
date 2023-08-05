#!/usr/bin/python3
#Imoprt the Flask class from the flask module
from flask import Flask

#Create an instance of the Flask class with the name of
#the current module as the argument
app = Flask(__name__)

#Define a route for the root URL ("/") of the web application
@app.route('/', strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB!'

#Check if the script is being run as the main program
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
