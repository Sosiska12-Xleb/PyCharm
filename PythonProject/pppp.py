import sqlite3

# Подключение к базе данных (если файла нет, он будет создан)
conn = sqlite3.connect('example2.db')
cursor = conn.cursor()

# Создание таблицы (если она ещё не существует)
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    mail TEXT
)
''')

new_user = ""
new_age = ""
new_mail = ""
new = ""
while new != "0":
    new = input("Добавить нового пользователя? Для отмены 0: ")
    if new == "0":
        break
    else:
        new_user = input('Введите имя: ')
        new_age = input('Введите возраст: ')
        non_new_mail = input('Введите почту: ')
        if non_new_mail == "":
            cursor.execute('''
                INSERT INTO users (name, age)
                VALUES (?,?)
                ''', (new_user, new_age))
            conn.commit()
        else:
            cursor.execute('''
                INSERT INTO users (name, age, mail)
                VALUES (?,?,?)
                ''', (new_user, new_age, new_mail))
            conn.commit()

# Добавление строки в таблицу
cursor.execute('''
SELECT * FROM users
''')

rows = cursor.fetchall()
columns = [description[0] for description in cursor.description]

print(" | ".join(columns))
print("-" * (len(columns) * 15))

for row in rows:
    print(" | ".join(map(str, row)))

# Сохранение изменений
conn.commit()

# Закрытие соединения
conn.close()

print("Строка успешно добавлена!")