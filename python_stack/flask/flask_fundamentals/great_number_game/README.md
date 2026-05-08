# Number Guessing Game 🎯

A simple web-based Number Guessing Game built using Flask and Python.  
The player has **5 attempts** to guess a random number between **1 and 100**.

---

## Features

- Random number generated between 1 and 100
- Maximum of 5 attempts
- Displays hints:
  - Too High
  - Too Low
  - Correct
- Session-based game state
- Automatic game reset after win/loss

---

## Technologies Used

- Python
- Flask
- HTML
- Sessions

---

## Project Structure

```bash
project/
│
├── app.py
├── templates/
│   └── index.html
└── README.md
```

---

## Installation

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd project
```

### 2. Create virtual environment (optional)

```bash
python -m venv venv
```

Activate environment:

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / Mac

```bash
source venv/bin/activate
```

### 3. Install Flask

```bash
pip install flask
```

---

## Run the Application

```bash
python app.py
```

The app will run on:

```bash
http://127.0.0.1:5000/
```

---

## Game Rules

1. The system generates a random number between 1 and 100.
2. The player enters a guess.
3. The app provides feedback:
   - Too high
   - Too low
   - Correct guess
4. The player has only 5 attempts.
5. If the player guesses correctly, they win.
6. If all attempts are used, the player loses and the game ends.

---

## Main Routes

| Route | Method | Description |
|------|--------|-------------|
| `/` | GET | Display game page |
| `/guess` | POST | Handle user guesses |

---

## Example Logic

```python
if user_guess > number:
    session['result'] = "high"
elif user_guess < number:
    session['result'] = "low"
else:
    session['result'] = "correct"
```

---

## Future Improvements

- Add score system
- Add difficulty levels
- Add timer
- Store high scores in database
- Improve UI design

---

## Author

Ahmed Hammad