from flask_sqlalchemy import SQLAlchemy
 
db = SQLAlchemy()
 
class TodoModel(db.Model):
    __tablename__ = 'todos'
 
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String())
    completed = db.Column(db.Boolean())
 
    def __init__(self, task):
        self.task = task
        self.completed = False
 
    def __repr__(self):
        return f"{self.task} (COMPLETED: {self.completed})"