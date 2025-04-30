from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

#Create a route decorator
@app.route('/')

def index():
    return "<h1>Hello test!</h1>"

@app.route('/<fname>.<lname>')
def user(fname,lname):
    return f"<h1>Hello {fname} {lname}</h1>"

# if __name__ == '__main__':
#     app.run(debug=True)