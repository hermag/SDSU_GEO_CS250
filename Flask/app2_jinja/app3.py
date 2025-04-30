#Jinja is a templating engine for Python
#For the reference you can visit https://jinja.palletsprojects.com/en/stable/

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

#Create a route decorator
@app.route('/')
def index():
    some_names=["John", "Jane", "Jim", "Jill"]
    return render_template('index1.html', names=some_names)

@app.route('/<name><int:age>')
def user(name, age):
    return render_template('user2.html', name=name, age=age)

if __name__ == '__main__':
    app.run(debug=True)
