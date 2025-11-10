from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Initialize database
def init_db():
    conn = sqlite3.connect('database.db')
    conn.execute('CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, description TEXT)')
    conn.close()

@app.route('/')
def index():
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM items')
    items = cur.fetchall()
    conn.close()
    return render_template('index.html', items=items)

@app.route('/add', methods=['POST'])
def add_item():
    name = request.form['name']
    description = request.form['description']
    conn = sqlite3.connect('database.db')
    conn.execute('INSERT INTO items (name, description) VALUES (?, ?)', (name, description))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete_item(id):
    conn = sqlite3.connect('database.db')
    conn.execute('DELETE FROM items WHERE id=?', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_item(id):
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        cur.execute('UPDATE items SET name=?, description=? WHERE id=?', (name, description, id))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    
    cur.execute('SELECT * FROM items WHERE id=?', (id,))
    item = cur.fetchone()
    conn.close()
    return render_template('edit.html', item=item)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
