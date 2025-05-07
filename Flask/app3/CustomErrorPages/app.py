from flask import Flask, render_template, abort, redirect, url_for

app = Flask(__name__)

# Example 1: Basic 404 Error Page
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Example 2: Custom 500 Error Page with Error Details
@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html', error=e), 500

# Example 3: Custom 403 Forbidden Page
@app.errorhandler(403)
def forbidden(e):
    return render_template('403.html'), 403

# Routes to demonstrate the error pages
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/error500')
def trigger_500():
    # This will trigger a 500 error
    return render_template('500.html')

@app.route('/error403')
def trigger_403():
    # This will trigger a 403 error
    abort(403)

@app.route('/error404')
def trigger_404():
    # This will trigger a 404 error
    abort(404)

if __name__ == '__main__':
    app.run(debug=True) 