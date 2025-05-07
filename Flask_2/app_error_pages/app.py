from flask import Flask, render_template, abort

app = Flask(__name__)

#Example 1: Basic 403 Error Page
@app.errorhandler(403)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route('/error403')
def trigger_403():
    #This will trigger a 404 error
    abort(403)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route('/error404')
def trigger_404():
    #This will trigger a 404 error
    abort(404)

@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 404

@app.route('/error500')
def trigger_500():
    #This will trigger a 404 error
    abort(500)

# Routes to demonstrate the error pages
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)