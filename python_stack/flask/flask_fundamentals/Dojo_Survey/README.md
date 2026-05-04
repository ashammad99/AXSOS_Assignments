# Flask Form Project

## 📌 Description

This is a simple Flask web application that demonstrates how to:

* Create a form
* Send data using POST method
* Receive and process form data in Flask
* Display submitted data on another page

---

## 🚀 Features

* User submits:

  * Name
  * Location
  * Favorite programming language
  * Comment
  * Gender
  * Favorite sports (multiple selection)
* Data is processed and displayed on a result page

---

## 🛠️ Technologies Used

* Python
* Flask
* HTML (Jinja2 templates)
* Bootstrap (optional for styling)

---

## 📂 Project Structure

```
project/
│
├── app.py
├── templates/
│   ├── index.html
│   └── show.html
```

---

## ▶️ How to Run

1. Install Flask:

```
pip install flask
```

2. Run the application:

```
python app.py
```

3. Open your browser and go to:

```
http://127.0.0.1:5000/
```

---

## ⚠️ Notes

* `request.form[]` is used for required fields
* `request.form.get()` is safer for optional fields
* `request.form.getlist()` is used for checkboxes (multiple values)

---

## 💡 Future Improvements

* Add form validation
* Improve UI with Bootstrap
* Store data in a database
* Add redirect after POST (POST-Redirect-GET pattern)

---
