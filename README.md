# 📝 MyTodo - Flask Based Todo List App

A simple and elegant Todo list web application built with **Flask** and **SQLAlchemy**, designed to help users create, update, and manage their daily tasks efficiently.

---

## 🚀 Features

- Add new todos with title and description  
- Update existing todos via modal  
- Delete todos  
- Auto timestamp on task creation  
- Responsive UI using Bootstrap  
- Developer info page  
- Footer sticks to the bottom  
- Fully functional SQLite database with SQLAlchemy ORM  

---

## ⚙️ Tech Stack

- **Backend:** Python, Flask, SQLAlchemy  
- **Frontend:** HTML, CSS, Bootstrap  
- **Database:** SQLite  

---

## 🛠️ Installation Steps

### 1. Clone the repository

```bash
git clone https://github.com/your-username/mytodo-flask.git
cd mytodo-flask
2. Create and activate a virtual environment
bash
Copy
Edit
python -m venv env

# On Windows
env\Scripts\activate

# On macOS/Linux
source env/bin/activate
3. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Run the app
bash
Copy
Edit
python app.py
Then open your browser and visit:
📍 http://127.0.0.1:5000

📂 Project Structure
graphql
Copy
Edit
mytodo/
│
├── static/
│   └── Adhish.jpg             # Profile image for developer page
│
├── templates/
│   ├── base.html              # Base layout
│   ├── index.html             # Main page with todo form and task list
│   └── developer.html         # Developer profile page
│
├── app.py                     # Main Flask app
├── todo.db                    # SQLite database file (auto-generated)
├── requirements.txt           # Python dependencies
└── README.md                  # Project documentation
👨‍💻 Developer
Adhish Biju

🔗 LinkedIn

🐙 GitHub

✉️ Email: adhishbiju@example.com

📌 Notes for Recruiters
This project was built as part of my web development journey using Python and Flask. It demonstrates:

Basic CRUD operations

Web development structure

ORM (SQLAlchemy) usage

UI components and Bootstrap integration

Template inheritance with Jinja2

Screenshots are available in the repo if the site is not hosted.
Feel free to explore the code and structure.

💡 Tips for Starting a Similar Project
If you're starting a new Flask project:

Set up folder structure

Use templates/ for HTML files

Use static/ for images or CSS/JS files

Create a virtual environment

bash
Copy
Edit
python -m venv env
Activate the environment and install dependencies

bash
Copy
Edit
# Windows
env\Scripts\activate
# macOS/Linux
source env/bin/activate

pip install flask flask_sqlalchemy
Build and test incrementally

Start with a basic route

Add database model

Add HTML templates

Use Jinja2 for layout inheritance

Use Git regularly to track your progress

Write a clear README.md and maintain your requirements.txt


### Prerequisites

Make sure you have Python and pip installed. Then install a virtual environment:

```bash
pip install virtualenv
