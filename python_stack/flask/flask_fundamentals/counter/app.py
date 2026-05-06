from flask import Flask, render_template, session, redirect, request

app = Flask(__name__)
app.secret_key = "secret123"

@app.route('/')
def index():
    if 'visits' in session:
        session['visits'] += 1
    else:
        session['visits'] = 1


    if 'counter' not in session:
        session['counter'] = 0

    return render_template("index.html",
                           visits=session['visits'],
                           counter=session['counter'])


@app.route('/increment')
def increment():
    session['counter'] += 1
    return redirect('/')

@app.route('/double')
def doubleCounter():
    session['counter'] += 2
    return redirect('/')

@app.route('/increment_custom', methods=['POST'])
def increment_custom():
    amount = int(request.form['amount'])
    session['counter'] += amount
    return redirect('/')

@app.route('/reset')
def reset():
    session['counter'] = 0
    return redirect('/')

@app.route('/destroy_session')
def destroy():
    session.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)


# To Decode the cookie information
# 1. Install: pip install flask-unsign
# 2. Inspect code in browser -> Application -> Storage -> Cookies -> get cookie value
# 3. flask-unsign --decode --cookie "cookie_value"