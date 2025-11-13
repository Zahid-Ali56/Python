from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Simple in-memory list of tasks
tasks = []

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add():
    task_content = request.form.get('task')
    if task_content:
        tasks.append({'content': task_content})
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>')
def delete(task_id):
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
    return redirect(url_for('index'))

@app.route('/edit/<int:task_id>')
def edit(task_id):
    if 0 <= task_id < len(tasks):
        task_to_edit = tasks[task_id]
        return render_template('index.html', tasks=tasks, edit_task=task_to_edit, edit_id=task_id)
    return redirect(url_for('index'))

@app.route('/update/<int:task_id>', methods=['POST'])
def update(task_id):
    new_content = request.form.get('task')
    if 0 <= task_id < len(tasks) and new_content:
        tasks[task_id]['content'] = new_content
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
