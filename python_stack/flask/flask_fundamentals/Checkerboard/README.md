# 🧩 Flask Checkerboard App

A simple Flask web application that dynamically generates a checkerboard pattern based on URL parameters. You can customize the number of rows, columns, and colors directly from the browser.

---

## 🚀 Features

* Generate an 8x8 checkerboard (default)
* Customize number of rows
* Customize rows and columns
* Customize rows, columns, and colors
* Dynamic rendering using Flask templates

---

## 📁 Project Structure

```
project/
│── app.py
│── templates/
│   └── checkerboard.html
```

---

## ⚙️ Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/flask-checkerboard.git
cd flask-checkerboard
```

2. Create a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install flask
```

---

## ▶️ Running the App

```bash
python app.py
```

Then open your browser and go to:

```
http://127.0.0.1:5000/
```

---

## 🌐 Routes

### 1. Default Checkerboard

```
/
```

* 8 rows × 8 columns
* Colors: white & black

---

### 2. Custom Rows

```
/<x>
```

Example:

```
/5
```

* x rows × 8 columns
* Colors: blue & gray

---

### 3. Custom Rows & Columns

```
/<x>/<y>
```

Example:

```
/5/10
```

* x rows × y columns
* Colors: black & white

---

### 4. Fully Custom Checkerboard

```
/<x>/<y>/<color1>/<color2>
```

Example:

```
/5/10/red/blue
```

* x rows × y columns
* Custom colors

---

## 🧠 How It Works

* Flask routes capture URL parameters.
* These parameters are passed to the `checkerboard.html` template.
* The template dynamically builds the checkerboard using loops and styling.

---

## 📌 Example

Visiting:

```
http://127.0.0.1:5000/6/6/green/yellow
```

Will render:

* 6x6 checkerboard
* Alternating green and yellow squares

---

## 🛠️ Technologies Used

* Python
* Flask
* HTML (Jinja2 Templates)

---

## 📄 License

This project is open-source and available for educational purposes.
