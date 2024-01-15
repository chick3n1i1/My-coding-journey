from flask import Blueprint

views = Blueprint('views', __name__)



@views.route('/')
def home():
    if request.method == 'POST':
        task_content = request.form['content']
        new_task = Todo(content=task_content)

@app.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
    pass

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    pass