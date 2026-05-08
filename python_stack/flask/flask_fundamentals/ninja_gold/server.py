from flask import Flask, render_template, request, redirect, session
import random
from datetime import datetime

# Create Flask application
app = Flask(__name__)

# Secret key used for session management
app.secret_key = "secret_key"


# Home page route
@app.route('/')
def index():

    # Initialize gold amount if it does not exist in session
    if 'gold' not in session:
        session['gold'] = 0

    # Initialize activities list if it does not exist
    if 'activities' not in session:
        session['activities'] = []

    # Render main page
    return render_template("index.html")


# Route to process earning or losing gold
@app.route('/process_money', methods=['POST'])
def process_money():

    # Get selected building from form
    building = request.form['building']

    # Default gold value
    gold = 0

    # Farm gives 10 - 20 gold
    if building == "farm":
        gold = random.randint(10, 20)

    # Cave gives 5 - 10 gold
    elif building == "cave":
        gold = random.randint(5, 10)

    # House gives 2 - 5 gold
    elif building == "house":
        gold = random.randint(2, 5)

    # Casino may win or lose gold
    elif building == "casino":
        gold = random.randint(-50, 50)

    # Update total gold in session
    session['gold'] += gold

    # Get current date and time
    time = datetime.now().strftime("%Y/%m/%d %I:%M %p")

    # Create activity message
    if gold >= 0:
        message = f"Earned {gold} gold from the {building}! ({time})"
    else:
        message = f"Entered a casino and lost {abs(gold)} gold... Ouch. ({time})"

    # Add newest activity to beginning of list
    session['activities'].insert(0, message)

    # Redirect back to home page
    return redirect('/')


# Run application in debug mode
if __name__ == "__main__":
    app.run(debug=True)