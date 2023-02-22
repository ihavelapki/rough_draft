from flask import Flask, render_template, request, url_for, flash, redirect
import sqlite3 as sql
from werkzeug.exceptions import abort

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Orion123'


def get_db_connection():
    conn = sql.connect(r'/Users/kot/Education/PycharmProjects/kek/education/test_sqlite/data/testsqlite.db')
    conn.row_factory = sql.Row
    return conn


def get_comment(comment_id):
    conn = get_db_connection()
    comment = conn.execute('SELECT * FROM comments WHERE comment_id = ?',
                        (comment_id,)).fetchone()
    conn.close()
    if comment is None:
        abort(404)
    return comment


@app.route('/')
def index():
    conn = get_db_connection()
    comments = conn.execute('SELECT * FROM comments').fetchall()
    conn.close()
    return render_template('index.html', comments=comments)


@app.route('/<int:comment_id>')
def view_comment(comment_id):
    comment = get_comment(comment_id)
    return render_template('comment.html', comment=comment)


@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO comments (title, content, user_id) VALUES (?, ?, ?)',
                         (title, content, 1))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('create.html')


@app.route('/<int:comment_id>/edit', methods=('GET', 'POST'))
def edit(comment_id):
    comment = get_comment(comment_id)

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        else:
            conn = get_db_connection()
            conn.execute('UPDATE comments SET title = ?, content = ?'
                         ' WHERE comment_id = ?',
                         (title, content, comment_id))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('edit.html', comment=comment)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000)