import sqlite3

# Подключение к базе данных (если файла нет, он будет создан)
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# Создание таблицы (если она ещё не существует)
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    email TEXT
)
''')

# Данные для добавления
new_user = ('Алексей', 30, 'alexey@example.com')
new_user2 = ('Олег', 102, "olegavylkan@example.com")

cursor.execute('''
INSERT INTO users (name, age, email)
VALUES (?, ?, ?)
''', new_user2)

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