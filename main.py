import os
from flask import Flask, request, redirect, url_for

app = Flask(__name__)

# Real-world mock data
tasks = [
    {"id": 1, "task": "Integrate Cloud Infrastructure", "status": "Done"},
    {"id": 2, "task": "Refactor UI for User Experience", "status": "Pending"}
]
next_id = 3

def get_html_content():
    """Expert UI/UX with Professional Content Text"""
    task_rows = ""
    for t in tasks:
        is_done = t['status'] == 'Done'
        task_rows += f'''
        <div class="task-item d-flex align-items-center justify-content-between p-3 mb-2">
            <div class="d-flex align-items-center">
                <div class="status-indicator {"bg-success" if is_done else "bg-light border"} me-3"></div>
                <span class="task-text {"text-muted text-decoration-line-through" if is_done else "text-dark fw-medium"}">
                    {t['task']}
                </span>
            </div>
            <div class="actions">
                <a href="/update/{t['id']}" class="btn btn-link text-decoration-none text-secondary p-1 me-2">
                    { "↺ Reopen" if is_done else "✓ Complete" }
                </a>
                <a href="/delete/{t['id']}" class="btn btn-link text-danger text-decoration-none p-1">Delete</a>
            </div>
        </div>
        '''

    return f'''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Focus Flow | Modern Task Management</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
        <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&display=swap" rel="stylesheet">
        <style>
            :root {{ --primary: #2563eb; --bg: #f8fafc; }}
            body {{ font-family: 'Inter', sans-serif; background-color: var(--bg); color: #1e293b; }}
            .app-container {{ max-width: 650px; margin: 80px auto; }}
            .glass-card {{ background: white; border-radius: 24px; border: 1px solid rgba(226, 232, 240, 0.8); box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.04); padding: 40px; }}
            .header-title {{ font-weight: 600; letter-spacing: -0.025em; color: #0f172a; }}
            .task-item {{ background: #ffffff; border: 1px solid #f1f5f9; border-radius: 12px; transition: all 0.2s ease; }}
            .task-item:hover {{ border-color: #cbd5e1; transform: translateY(-1px); }}
            .status-indicator {{ width: 12px; height: 12px; border-radius: 50%; }}
            .form-control {{ border-radius: 12px; padding: 12px 16px; border: 1px solid #e2e8f0; }}
            .form-control:focus {{ box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.1); border-color: var(--primary); }}
            .btn-primary {{ border-radius: 12px; padding: 12px 24px; font-weight: 600; background: var(--primary); border: none; }}
            .footer-meta {{ font-size: 0.75rem; color: #94a3b8; margin-top: 40px; }}
        </style>
    </head>
    <body>
        <div class="app-container px-3">
            <div class="glass-card">
                <header class="mb-5">
                    <h2 class="header-title mb-1">Focus Flow</h2>
                    <p class="text-secondary small">Streamline your daily productivity</p>
                </header>

                <form action="/add" method="POST" class="d-flex gap-2 mb-4">
                    <input type="text" name="task_name" class="form-control" placeholder="What needs to be done?" required autocomplete="off">
                    <button class="btn btn-primary" type="submit">Add</button>
                </form>

                <div class="task-list">
                    {task_rows if tasks else '<p class="text-center text-muted py-4">All clear. Enjoy your day!</p>'}
                </div>

                <footer class="footer-meta text-center">
                    <p class="mb-0">System Node: GAE-Standard | Build v1.0.4</p>
                    <p class="text-uppercase letter-spacing-1 fw-bold mt-2" style="font-size: 10px;">
                        {os.environ.get('USER_NAME', 'Pratham Amritkar')} — {os.environ.get('ROLL_NO', '23CO009')}
                    </p>
                </footer>
            </div>
        </div>
    </body>
    </html>
    '''

@app.route('/')
def hello():
    return get_html_content()

@app.route('/add', methods=['POST'])
def add():
    global next_id
    content = request.form.get('task_name')
    if content:
        tasks.append({"id": next_id, "task": content, "status": "Pending"})
        next_id += 1
    return redirect(url_for('hello'))

@app.route('/update/<int:task_id>')
def update(task_id):
    for t in tasks:
        if t['id'] == task_id:
            t['status'] = "Done" if t['status'] == "Pending" else "Pending"
    return redirect(url_for('hello'))

@app.route('/delete/<int:task_id>')
def delete(task_id):
    global tasks
    tasks = [t for t in tasks if t['id'] != task_id]
    return redirect(url_for('hello'))

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
