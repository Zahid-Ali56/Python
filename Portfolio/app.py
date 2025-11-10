import os
import sqlite3
from flask import Flask, render_template, request, redirect, url_for, send_from_directory

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# --- Database ---
def init_db():
    conn = sqlite3.connect('portfolio.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS messages (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        email TEXT NOT NULL,
                        message TEXT NOT NULL
                      )''')
    conn.commit()
    conn.close()
init_db()

# --- Routes ---
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def projects():
    files = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template('projects.html', files=files)

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return redirect(url_for('projects'))
    file = request.files['file']
    if file.filename != '':
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
    return redirect(url_for('projects'))

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/contact', methods=['POST'])
def send_message():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    conn = sqlite3.connect('portfolio.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO messages (name, email, message) VALUES (?, ?, ?)', (name, email, message))
    conn.commit()
    conn.close()
    return redirect(url_for('contact'))

@app.route('/messages')
def view_messages():
    conn = sqlite3.connect('portfolio.db')
    cursor = conn.cursor()
    cursor.execute('SELECT name, email, message FROM messages ORDER BY id DESC')
    messages = cursor.fetchall()
    conn.close()
    return render_template('messages.html', messages=messages)

if __name__ == '__main__':
    app.run(debug=True)
