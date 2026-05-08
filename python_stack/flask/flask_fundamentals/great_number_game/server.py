from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = "12345678"

@app.route('/')
def index():
    if 'number' not in session:
        session['number'] = random.randint(1, 100)
        session['attempts'] = 0
        session['result'] = None
        session['game_over'] = False

    return render_template(
        "index.html",
        result=session.get('result'),
        attempts=session.get('attempts'),
        number=session.get('number'),
        game_over=session.get('game_over')
    )


@app.route('/guess', methods=['POST'])
def guess():
    if session.get('game_over'):
        session.clear()
        return redirect('/')

    user_guess = int(request.form['guess'])
    number = session['number']

    session['attempts'] += 1

    if session['attempts'] >= 5 and user_guess != number:
        session['result'] = "lose"
        session['game_over'] = True
        return redirect('/')

    if user_guess > number:
        session['result'] = "high"
    elif user_guess < number:
        session['result'] = "low"
    else:
        session['result'] = "correct"
        session['game_over'] = True

    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)