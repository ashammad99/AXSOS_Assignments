from flask import Flask, render_template

# Create Flask application instance
app = Flask(__name__)

@app.route('/users')
def render_lists():
    """
    Route to display a list of users.

    This function creates a list of user dictionaries,
    where each dictionary contains:
    - first_name
    - last_name

    The data is passed to the 'users.html' template
    and rendered dynamically using Jinja2.
    """

    # Sample static data (can be replaced with database later)
    users = [
        {'first_name': 'Michael', 'last_name': 'Choi'},
        {'first_name': 'John', 'last_name': 'Supsupin'},
        {'first_name': 'Mark', 'last_name': 'Guillen'},
        {'first_name': 'KB', 'last_name': 'Tonel'}
    ]

    # Render template and pass users list
    return render_template("users.html", users=users)


# Run the application only if this file is executed directly
if __name__ == "__main__":
    app.run(debug=True)