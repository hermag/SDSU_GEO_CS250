from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

#Create a route decorator
@app.route('/')

def index():
    return "<h1>Hello test!</h1>"