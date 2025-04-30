#Example of using HTML templates
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

#Create a route decorator
@app.route('/')

def index():
    return render_template('index.html')

@app.route('/<name>')
def user(name):
    return f"<h1>Hello {name}!</h1>"

if __name__ == '__main__':
    app.run(debug=True)