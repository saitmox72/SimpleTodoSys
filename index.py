from flask import render_template
from models import Todo

@app.route("/")
def index():
    todos = Todo.query.order_by(Todo.created_at.desc()).all()
    return render_template("index.html", todos=todos)
