# Ninja Gold Game 🥷💰

A simple web application built using Flask where players can earn or lose gold by visiting different buildings.

---

## Features

- Earn gold from different locations
- Casino can either win or lose gold
- Activity log with timestamps
- Session-based storage
- Simple and interactive gameplay

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

## Buildings Rules

| Building | Gold Range |
|----------|------------|
| Farm | 10 - 20 gold |
| Cave | 5 - 10 gold |
| House | 2 - 5 gold |
| Casino | -50 to 50 gold |

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

Application will run on:

```bash
http://127.0.0.1:5000/
```

---

## How the Game Works

1. Player starts with 0 gold.
2. Choose a building to visit.
3. Gold is randomly earned or lost depending on the building.
4. Activities are stored with timestamps.
5. Total gold updates automatically.

---

## Example Activity Log

```text
Earned 15 gold from the farm! (2026/05/08 03:30 PM)

Entered a casino and lost 20 gold... Ouch. (2026/05/08 03:35 PM)
```

---

## Future Improvements

- Add reset button
- Add leaderboard
- Save scores in database
- Add user authentication
- Improve UI design

---

## Author

Ahmed Hammad