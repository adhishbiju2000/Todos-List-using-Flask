from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

# Initialize Flask app
app = Flask(__name__)

# Configure SQLite database
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + os.path.join(basedir, "todo.db")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Inject datetime globally into templates (for footer)
@app.context_processor
def inject_datetime():
    return {'datetime': datetime}

# Define Todo model
class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    des = db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Todo {self.sno} - {self.title}>"

# Home route - display and add todos
@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        title = request.form.get('title')
        des = request.form.get('des')
        if title and des:
            new_todo = Todo(title=title, des=des)
            db.session.add(new_todo)
            db.session.commit()

    todos = Todo.query.order_by(Todo.date_created.desc()).all()
    return render_template("index.html", allTodo=todos)

# Delete route
@app.route("/delete/<int:sno>")
def delete(sno):
    todo = Todo.query.get_or_404(sno)
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("home"))

# Update route
@app.route("/update/<int:sno>", methods=["GET", "POST"])
def update(sno):
    todo = Todo.query.get_or_404(sno)

    if request.method == "POST":
        todo.title = request.form.get("title")
        todo.des = request.form.get("des")

        if todo.title and todo.des:
            db.session.commit()
            return redirect(url_for("home"))
        else:
            return "Error: Fields cannot be empty", 400

    return render_template("update.html", todo=todo)

# Developer route
@app.route("/developer")
def developer():
    return render_template("developer.html")


# Features route
@app.route("/features")
def features():
    return render_template("features.html", datetime=datetime)


# Main
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
