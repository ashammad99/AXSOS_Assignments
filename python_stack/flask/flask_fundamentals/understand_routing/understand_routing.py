from flask import Flask

# Create a Flask application instance
app = Flask(__name__)


# Home route
# URL: http://127.0.0.1:5000/
@app.route('/')
def home():
    return "Hello World!"


# Champion route
# URL: http://127.0.0.1:5000/Champion%20!
@app.route('/Champion !')
def sayChampion():
    return "Champion"


# Dynamic route that takes a name from the URL
# Example: http://127.0.0.1:5000/say/Ahmed
@app.route('/say/<name>')
def sayMyName(name):
    return "Hello " + name


# Dynamic route that repeats a message multiple times
# Example: http://127.0.0.1:5000/repeat/3/Hello
@app.route('/repeat/<int:number>/<msg>')
def hello(number, msg):
	# number = int(number)
    return msg * number


# Custom 404 error handler
# This runs when the user visits a page that does not exist
@app.errorhandler(404)
def page_not_found(e):
    return "Sorry! No response. Try again. 404 Error"


# Run the Flask app only when this file is executed directly
if __name__ == "__main__":
    app.run(debug=True)