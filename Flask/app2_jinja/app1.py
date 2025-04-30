#Jinja is a templating engine for Python
#For the reference you can visit https://jinja.palletsprojects.com/en/stable/

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

#Create a route decorator
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<name>')
def user(name):
    return render_template('user.html', thename=name)

if __name__ == '__main__':
    app.run(debug=True)
