from flask import Flask, render_template

# Create a Flask application instance
app = Flask(__name__)


# Route 1: Default route
# URL: /play/
# Displays 3 red boxes by default
#
# Route 2: Dynamic route with number only
# URL: /play/<x>/
# Example: /play/5/
# Displays x number of red boxes
#
# Route 3: Dynamic route with number and color
# URL: /play/<x>/<color>
# Example: /play/5/blue
# Displays x number of boxes with the selected color
@app.route('/play/')
@app.route('/play/<int:x>/')
@app.route('/play/<int:x>/<color>')
def play(x=3, color="red"):
    # Send x and color values to the HTML template
    return render_template("boxes.html", x=x, color=color)


# Custom 404 error handler
# This runs when the user visits a page that does not exist
@app.errorhandler(404)
def page_not_found(e):
    return "Sorry! No response. Try again. 404 Error"


# Run the Flask application only when this file is executed directly
if __name__ == "__main__":
    app.run(debug=True)