from flask import Flask, render_template, request
from flask_migrate import Migrate
from models import db, TodoModel
from flask_restful import reqparse, abort, Api, Resource
from flask_sqlalchemy import get_or_404, first_or_404

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:1148@localhost:5432/flask"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
migrate = Migrate(app, db)
api = Api(app)

TODOS = {
    '1': {'task': 'Task 1'},
    '2': {'task': 'Task 2'},
    '3': {'task': 'Task 3'},
}


def abort_if_todo_doesnt_exist(todo_id):
    if todo_id not in TODOS:
        abort(404, message="Todo {} doesn't exist".format(todo_id))

parser = reqparse.RequestParser()
parser.add_argument('task')


# class Todo(Resource):
#     def get(self, todo_id):
#         abort_if_todo_doesnt_exist(todo_id)
#         return TODOS[todo_id]

#     def delete(self, todo_id):
#         abort_if_todo_doesnt_exist(todo_id)
#         del TODOS[todo_id]
#         return '', 204

#     def put(self, todo_id):
#         args = parser.parse_args()
#         task = {'task': args['task']}
#         TODOS[todo_id] = {'task': args['task']}
#         return task, 201


# class TodoList(Resource):
#     def get(self):
#         return TODOS

#     def post(self):
#         args = parser.parse_args()
#         todo_id = int(max(TODOS.keys()).lstrip('todo')) + 1
#         todo_id = 'todo%i' % todo_id
#         TODOS[todo_id] = {'task': args['task']}
#         return TODOS[todo_id], 201


class Todo(Resource):
    def get(self, todo_id):
        item = TodoModel.query.filter_by(id=todo_id).get_or_404()
        return item, 200

    def delete(self, todo_id):
        item = TodoModel.query.filter_by(id=todo_id).get_or_404()
        db.session.delete(item)
        db.session.commit()
        return '', 204

    def put(self, todo_id):
        item = TodoModel.query.filter_by(id=todo_id).get_or_404()
        args = parser.parse_args()
        task = args['task']
        item.task = task
        db.session.commit()
        return task, 201


class TodoList(Resource):
    def get(self):
        todos = TodoModel.query.all().get_or_404()
        return todos, 200

    def post(self):
        args = parser.parse_args()
        todo = TodoModel(task=args['task'])
        db.session.add(todo)
        db.session.commit()
        return todo, 201


api.add_resource(TodoList, '/todos')
api.add_resource(Todo, '/todos/<todo_id>')


if __name__ == '__main__':
    app.run(debug=True)