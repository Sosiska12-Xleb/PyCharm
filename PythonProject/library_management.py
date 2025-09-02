import sqlite3
import datetime

conn = sqlite3.connect('library2.db')
cursor = conn.cursor()


cursor.execute('''
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    author TEXT,
    published_year INTEGER,
    available INTEGER
)
''')


cursor.execute('''
CREATE TABLE IF NOT EXISTS readers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT
)
''')


cursor.execute('''
CREATE TABLE IF NOT EXISTS readers_books_time (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    book_id INTEGER,
    reader_id INTEGER,
    time TEXT,
    FOREIGN KEY (book_id) REFERENCES books(id),
    FOREIGN KEY (reader_id) REFERENCES readers(id))
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS review (
    reader_id INTEGER,
    textreview TEXT,
    time TEXT,
    FOREIGN KEY (reader_id) REFERENCES readers(id))
''')

main_library = ""
print("Добро пожаловать в библиотеку!")
print("1. Добавить книгу")
print("2. Добавить читателя")
print("3. Выдать книгу")
print("4. Вернуть книгу")
print("5. Просмотреть все книги")
print("6. Просмотреть всех читателей")
print("7. Посмотреть таблицу выданых книг")
print("8. Написать отзыв")
print("9. Посмотреть отзывы")
print("0. Выход")
print("")
while main_library != "0":
    main_library = input("Выберите действие: ")

    if main_library == "1":
        new_title = input("Введите название книги: ")
        new_author = input("Введите полное имя автора: ")
        new_published_year = input("Введите год публикации книги: ")
        new_book_available = 1
        cursor.execute('''
                        INSERT INTO books (title, author, published_year, available)
                        VALUES (?,?,?,?)
                        ''', (new_title, new_author, new_published_year, new_book_available))
        conn.commit()
        print("Книга добавлена в библиотеку!")

    elif main_library == "2":
        new_name = input("Введите полное имя читателя: ")
        new_email = input("Введите адрес электронной почты читателя: ")
        cursor.execute('''
                                INSERT INTO readers (name, email)
                                VALUES (?,?)
                                ''', (new_name, new_email))
        conn.commit()
        print("Читатель добавлен в базу данных библиотеки!")

    elif main_library == "3":
        print("Католог книг:")
        cursor.execute('''
                       SELECT * FROM books
                       ''')
        rows = cursor.fetchall()
        columns = [description[0] for description in cursor.description]
        print(" | ".join(columns))
        print("-" * (len(columns) * 15))
        for row in rows:
            print(" | ".join(map(str, row)))
        cursor.execute('''
        SELECT id FROM books
        ''')
        extradition_id = int(input("Введите id выдаваемой книги: "))
        print("Таблица читателей библеотеки:")
        cursor.execute('''
                               SELECT * FROM readers
                               ''')
        rows = cursor.fetchall()
        columns = [description[0] for description in cursor.description]
        print(" | ".join(columns))
        print("-" * (len(columns) * 15))
        for row in rows:
            print(" | ".join(map(str, row)))
        extradition_name = input("Введите id чтателя выдоваемой книги: ")
        cursor.execute(f"SELECT title, author, published_year FROM books WHERE id = {extradition_id}")
        title, author, published_year = cursor.fetchone()
        cursor.execute('''
        UPDATE books
        SET available = 0
        WHERE id = ? 
        ''', (extradition_id,))
        print(f"Title: {title} Author: {author} published_year: {published_year} книга выдана")
        conn.commit()
        cursor.execute('''
                                        INSERT INTO readers_books_time (book_id, reader_id, time)
                                        VALUES (?,?,?)
                                        ''', (extradition_id, extradition_name, datetime.datetime.now()))
        conn.commit()

    elif main_library == "4":
        print("Католог книг:")
        cursor.execute('''
                               SELECT * FROM books
                               ''')
        rows = cursor.fetchall()
        columns = [description[0] for description in cursor.description]
        print(" | ".join(columns))
        print("-" * (len(columns) * 15))
        for row in rows:
            print(" | ".join(map(str, row)))
        cursor.execute('''
                SELECT id FROM books
                ''')
        vozrat_id = int(input("Введите id возвращаемой книги: "))
        cursor.execute(f"SELECT title, author, published_year FROM books WHERE id = {vozrat_id}")
        title, author, published_year = cursor.fetchone()
        cursor.execute('''
                UPDATE books
                SET available = 1
                WHERE id = ? 
                ''', (vozrat_id,))
        print(f"Title: {title} Author: {author} published_year: {published_year} книга была возвращена")
        conn.commit()

    elif main_library == "5":
        print("Католог книг:")
        cursor.execute('''
                SELECT * FROM books
                ''')
        rows = cursor.fetchall()
        columns = [description[0] for description in cursor.description]
        print(" | ".join(columns))
        print("-" * (len(columns) * 15))
        for row in rows:
            print(" | ".join(map(str, row)))

    elif main_library == "6":
        print("Таблица читателей библиотеки:")
        cursor.execute('''
                SELECT * FROM readers
                ''')
        rows = cursor.fetchall()
        columns = [description[0] for description in cursor.description]
        print(" | ".join(columns))
        print("-" * (len(columns) * 15))
        for row in rows:
            print(" | ".join(map(str, row)))

    elif main_library == "7":
        print("Таблица выданных книг:")
        cursor.execute('''
                SELECT rbt.time, b.title, r.name 
                FROM readers_books_time rbt
                JOIN books b ON rbt.book_id = b.id
                JOIN readers r ON rbt.reader_id = r.id
            ''')
        rows = cursor.fetchall()
        columns = ["Дата выдачи", "Название книги", "Имя читателя"]
        print(" | ".join(columns))
        print("-" * (len(" | ".join(columns))))
        for row in rows:
            print(" | ".join(map(str, row)))

    elif main_library == "8":
        print("Таблица читателей библиотеки:")
        cursor.execute('''
                        SELECT * FROM readers
                        ''')
        rows = cursor.fetchall()
        columns = [description[0] for description in cursor.description]
        print(" | ".join(columns))
        print("-" * (len(columns) * 15))
        for row in rows:
            print(" | ".join(map(str, row)))
        reader_reveiw = input("Введите id читателя, вводящий отзыв: ")
        new_reveiw = input("Введите свой отзыв: ")
        cursor.execute('''
                                INSERT INTO review (reader_id,textreview, time)
                                VALUES (?,?,?)
                                ''', (reader_reveiw, new_reveiw, datetime.datetime.now()))
        conn.commit()
        print("Спасибо за отзыв!")

    elif main_library == "9":
        print("Таблица отзывов:")
        cursor.execute('''
                        SELECT re.name, r.textreview, r.time 
                        FROM review r
                        JOIN readers re ON r.reader_id = re.id
                    ''')
        rows = cursor.fetchall()
        columns = ["Имя читателя", "Отзыв", "Время отправления"]
        print(" | ".join(columns))
        print("-" * (len(" | ".join(columns))))
        for row in rows:
            print(" | ".join(map(str, row)))