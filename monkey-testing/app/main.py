import os
from flask import Flask, render_template, request, redirect, url_for, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///tasks.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, default='')
    priority = db.Column(db.String(10), default='medium')
    status = db.Column(db.String(20), default='todo')
    due_date = db.Column(db.String(20), default='')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'priority': self.priority,
            'status': self.status,
            'due_date': self.due_date,
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M'),
        }


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task_id = db.Column(db.Integer, db.ForeignKey('task.id'), nullable=False)
    text = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


with app.app_context():
    db.create_all()


@app.route('/')
def index():
    priority = request.args.get('priority', '')
    status = request.args.get('status', '')
    query = Task.query
    if priority:
        query = query.filter_by(priority=priority)
    if status:
        query = query.filter_by(status=status)
    tasks = query.order_by(Task.created_at.desc()).all()
    return render_template('index.html', tasks=tasks, priority=priority, status=status)


@app.route('/task/new', methods=['GET', 'POST'])
def new_task():
    error = None
    if request.method == 'POST':
        title = request.form.get('title', '').strip()
        if not title:
            error = 'Название задачи обязательно'
        else:
            task = Task(
                title=title,
                description=request.form.get('description', ''),
                priority=request.form.get('priority', 'medium'),
                due_date=request.form.get('due_date', ''),
            )
            db.session.add(task)
            db.session.commit()
            return redirect(url_for('index'))
    return render_template('task_form.html', task=None, error=error)


@app.route('/task/<int:task_id>', methods=['GET'])
def task_detail(task_id):
    task = Task.query.get_or_404(task_id)
    comments = Comment.query.filter_by(task_id=task_id).order_by(Comment.created_at).all()
    return render_template('task_detail.html', task=task, comments=comments)


@app.route('/task/<int:task_id>/edit', methods=['GET', 'POST'])
def edit_task(task_id):
    task = Task.query.get_or_404(task_id)
    error = None
    if request.method == 'POST':
        title = request.form.get('title', '').strip()
        if not title:
            error = 'Название задачи обязательно'
        else:
            task.title = title
            task.description = request.form.get('description', '')
            task.priority = request.form.get('priority', 'medium')
            task.due_date = request.form.get('due_date', '')
            db.session.commit()
            return redirect(url_for('task_detail', task_id=task.id))
    return render_template('task_form.html', task=task, error=error)


@app.route('/task/<int:task_id>/delete', methods=['POST'])
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    Comment.query.filter_by(task_id=task_id).delete()
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/task/<int:task_id>/status', methods=['POST'])
def change_status(task_id):
    task = Task.query.get_or_404(task_id)
    new_status = request.form.get('status')
    if new_status in ('todo', 'in_progress', 'done'):
        task.status = new_status
        db.session.commit()
    return redirect(request.referrer or url_for('index'))


@app.route('/task/<int:task_id>/comment', methods=['POST'])
def add_comment(task_id):
    Task.query.get_or_404(task_id)
    text = request.form.get('text', '').strip()
    if text:
        comment = Comment(task_id=task_id, text=text)
        db.session.add(comment)
        db.session.commit()
    return redirect(url_for('task_detail', task_id=task_id))


@app.route('/api/tasks', methods=['GET'])
def api_tasks():
    tasks = Task.query.all()
    return jsonify([t.to_dict() for t in tasks])


@app.route('/api/tasks/<int:task_id>', methods=['DELETE'])
def api_delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    Comment.query.filter_by(task_id=task_id).delete()
    db.session.delete(task)
    db.session.commit()
    return jsonify({'ok': True})


@app.route('/search')
def search():
    q = request.args.get('q', '').strip()
    tasks = []
    if q:
        tasks = Task.query.filter(
            Task.title.ilike(f'%{q}%') | Task.description.ilike(f'%{q}%')
        ).all()
    return render_template('search.html', tasks=tasks, q=q)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
