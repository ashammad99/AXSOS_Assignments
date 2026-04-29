from flask import Flask, render_template

# Create a Flask application instance
app = Flask(__name__)


@app.route('/')
def home():
    """
    Default route.

    Displays an 8x8 checkerboard using default colors:
    white and black.
    """
    return render_template(
        "checkerboard.html",
        x=8,
        y=8,
        color1="white",
        color2="black"
    )


@app.route('/<int:x>')
def rows(x):
    """
    Route with custom number of rows.

    Example:
    /5

    Displays a checkerboard with:
    - x rows
    - 8 columns
    - blue and gray colors
    """
    return render_template(
        "checkerboard.html",
        x=x,
        y=8,
        color1="blue",
        color2="gray"
    )


@app.route('/<int:x>/<int:y>')
def custom_rows_columns(x, y):
    """
    Route with custom rows and columns.

    Example:
    /5/10

    Displays a checkerboard with:
    - x rows
    - y columns
    - black and white colors
    """
    return render_template(
        "checkerboard.html",
        x=x,
        y=y,
        color1="black",
        color2="white"
    )


@app.route('/<int:x>/<int:y>/<color1>/<color2>')
def custom_rows_columns_colors(x, y, color1, color2):
    """
    Route with custom rows, columns, and colors.

    Example:
    /5/10/red/blue

    Displays a checkerboard with:
    - x rows
    - y columns
    - color1
    - color2
    """
    return render_template(
        "checkerboard.html",
        x=x,
        y=y,
        color1=color1,
        color2=color2
    )


# Run the Flask application only when this file is executed directly
if __name__ == "__main__":
    app.run(debug=True)