

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    print("Visited the hello page")
    return 'Hello, World!'

@app.route('/about')
def about():
    print("VISITED THE ABOUT PAGE")
    return 'About me!'