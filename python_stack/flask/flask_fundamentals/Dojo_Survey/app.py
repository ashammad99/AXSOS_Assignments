from flask import Flask, render_template, redirect, request

# Create a Flask application instance
app = Flask(__name__)

# Home route - displays the form page
@app.route('/')
def home():
    return render_template('index.html')


# Route to handle form submission (POST request only)
@app.route('/result', methods=["POST"])
def show():
    # Retrieve form data using request.form (for required fields)
    name_from_temp = request.form['name']
    location_from_temp = request.form['location']
    language_from_temp = request.form['language']
    comment_from_temp = request.form['comment']

    # Use .get() for optional fields to avoid errors if not provided
    gender_from_temp = request.form.get('gender', 'Not specified')

    # Use .getlist() when multiple values are expected (e.g., checkboxes)
    fav_sports_from_temp = request.form.getlist('fav_sport')

    # Pass the collected data to the template for rendering
    return render_template(
        "show.html",
        name_on_template=name_from_temp,
        language_on_template=language_from_temp,
        location_on_template=location_from_temp,
        comment_on_template=comment_from_temp,
        gender_on_template=gender_from_temp,
        fav_sport_on_template=fav_sports_from_temp
    )


# Run the application in debug mode
if __name__ == '__main__':
    app.run(debug=True)