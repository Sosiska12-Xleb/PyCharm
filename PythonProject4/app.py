from flask import Flask, render_template, request, redirect, url_for
import sqlite3

conn = sqlite3.connect('app.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    message TEXT
    )
''')

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form['name']
        message = request.form['message']
        print(f"Ура! Тебе написал {name}, он что то хотел тебе сказать: {message}")
        cursor.execute('''
                                        INSERT INTO users (name, message)
                                        VALUES (?,?)
                                        ''', (name, message))
        conn.commit()
        return redirect(url_for('home'))
    return render_template('index.html')

@app.route('/about_me', methods=['GET', 'POST'])
def about_me():
    return render_template('about_me.html')

@app.route('/survey', methods=['GET', 'POST'])
def survey():
    if request.method == 'POST':
        free_time = request.form['free_time']
        country = request.form['country']
        childhood = request.form['childhood']
        pink_glasses = request.form['pink_glasses']
        print(f"А вот ответы на вопрос от пользователя: {free_time},{country},{childhood},{pink_glasses}")
        return redirect(url_for('home'))
    return render_template('survey.html')

@app.route('/users_web', methods=['GET', 'POST'])
def users_web():
    cursor.execute('''
                              SELECT * FROM users
                              ''')
    rows = cursor.fetchall()
    columns = [description[0] for description in cursor.description]
    print(" | ".join(columns))
    print("-" * (len(columns) * 15))
    for row in rows:
        print(" | ".join(map(str, row)))
    conn.commit()
    return render_template('users_web.html', rows = rows)

if __name__ == '__main__':
    app.run(debug=True)