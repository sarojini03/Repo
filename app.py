
"""Flask application module"""
from datetime import datetime
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class Todo(db.Model):
    """Todo model"""
    id = db.Column(db.Integer(), primary_key=True, nullable=False)
    content = db.Column(db.String(length=200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, content):
        self.content = content

    def __repr__(self):
        return f'<Task {self.id}>'

@app.route('/', methods=['POST', 'GET'])
def index():
    """Index route"""
    if request.method == 'POST':
        task_content = request.form['content']
        new_task = Todo(content=task_content)
        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except db.IntegrityError as e:
            return f'There was an issue adding your task: {e}'
    else:
        tasks = Todo.query.order_by(Todo.date_created).all()
        return render_template('index.html', tasks=tasks)

@app.route('/delete/<int:task_id>')
def delete(task_id):
    """Delete route"""
    task_to_delete = Todo.query.get_or_404(task_id)
    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except db.SQLAlchemyError as e:
        return f'There was a problem deleting that task: {e}'

@app.route('/update/<int:task_id>', methods=['GET', 'POST'])
def update(task_id):
    """Update route"""
    task = Todo.query.get_or_404(task_id)
    if request.method == 'POST':
        task.content = request.form['content']
        try:
            db.session.commit()
            return redirect('/')
        except db.SQLAlchemyError as e:
            return f'There was an issue updating your task: {e}'
    else:
        return render_template('update.html', task=task)

if __name__ == "__main__":
    app.run(debug=True)