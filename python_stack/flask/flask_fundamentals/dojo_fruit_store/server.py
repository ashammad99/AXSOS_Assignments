import datetime

from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/checkout', methods=['POST'])
def checkout():
    strawberry = request.form.get('strawberry', 0)
    raspberry = request.form.get('raspberry', 0)
    apple = request.form.get('apple', 0)
    fname = request.form.get('first_name', '')
    lname = request.form.get('last_name', '')
    student_id = request.form.get('student_id', '')

    total = int(strawberry) + int(raspberry) + int(apple)
    now = datetime.datetime.now()

    print(f"Charging {fname} {lname} for {total} fruits.")

    return render_template("checkout.html",
                           strawberry=strawberry,
                           raspberry=raspberry,
                           apple=apple,
                           fname=fname,
                           lname=lname,
                           student_id=student_id,
                           total=total,
                           now=now
                           )


@app.route('/checkout/result')
def checkout_result():
    return render_template("checkout.html")


@app.route('/fruits')
def fruits():
    return render_template("fruits.html")


if __name__ == "__main__":
    app.run(debug=True)
