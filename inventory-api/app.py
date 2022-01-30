from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv
import json
from dataclasses import dataclass


load_dotenv()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


@dataclass
class Todo(db.Model):
    id: int
    title: str
    complete: bool

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    complete = db.Column(db.Boolean)


@app.route("/todos", methods=["GET"])
def all():
    todos = Todo.query.all()
    return jsonify(todos), 200


@app.route("/todos/<int:todo_id>", methods=["GET"])
def single(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    return jsonify(todo), 200


@app.route("/todos/add", methods=["POST"])
def add():
    title = request.form.get("title")
    new_todo = Todo(title=title, complete=False)
    db.session.add(new_todo)
    db.session.commit()
    return jsonify(new_todo), 201


@app.route("/todos/update/<int:todo_id>", methods=["PUT"])
def update(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    todo.complete = not todo.complete
    db.session.commit()
    return jsonify(todo), 201


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

    app.run(host='0.0.0.0', port=5000)