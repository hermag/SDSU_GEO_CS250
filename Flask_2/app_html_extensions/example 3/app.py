from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<name>')
def name(name):
    return render_template('name.html',first_name = name)

if __name__ == '__main__':
    app.run(debug=True) 