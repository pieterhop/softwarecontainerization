from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv
import json

load_dotenv()

app = Flask(__name__)

# /// = relative path, //// = absolute path
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://postgres:postgres@'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    complete = db.Column(db.Boolean)


@app.route("/todos", methods=["GET"])
def all():
    todos = Todo.query.all()
    return json.dumps([ob.__dict__ for ob in todos]), 200


@app.route("/todos/<int:todo_id>", methods=["GET"])
def single(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    return json.dumps(todo.__dict__), 200


@app.route("/todos/add", methods=["POST"])
def add():
    title = request.form.get("title")
    new_todo = Todo(title=title, complete=False)
    db.session.add(new_todo)
    db.session.commit()
    return json.dumps(new_todo.__dict__), 201


@app.route("/todos/update/<int:todo_id>", methods=["PUT"])
def update(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    todo.complete = not todo.complete
    db.session.commit()
    return json.dumps(todo.__dict__), 201


@app.route("/todos/delete/<int:todo_id>", methods=["DELETE"])
def delete(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    db.session.delete(todo)
    db.session.commit()
    return '', 204

if __name__ == "__main__":
    db.create_all()

    new_todo = Todo(title='test', complete=False)
    db.session.add(new_todo)
    db.session.commit()

    app.run(debug=True)