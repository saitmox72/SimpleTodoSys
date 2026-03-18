from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from config import Config
from models import Todo

app = Flask(__name__)

# @app.route("/")
# def index():
#     return "Hello Flask!"


db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    with app.app_context():
        from models import Todo
        db.create_all()

    return app

app = create_app()



@app.route("/")
def index():
    todos = Todo.query.order_by(Todo.created_at.desc()).all()
    return render_template("index.html", todos=todos)


if __name__ == "__main__":
    app.run(debug=True)
