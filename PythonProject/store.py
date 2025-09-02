import sqlite3

conn = sqlite3.connect('store.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT,
    created_at DATETIME
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS categories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    description TEXT,
    price REAL,
    category_id INTEGER,
    FOREIGN KEY (category_id) REFERENCES category(id)
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    users_id INTEGER,
    order_date DATETIME,
    status TEXT,
    FOREIGN KEY (users_id) REFERENCES users(id)
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS order_items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    orders_id INTEGER,
    products_id INTEGER,
    quantity INTEGER,
    FOREIGN KEY (orders_id) REFERENCES orders(id),
    FOREIGN KEY (products_id) REFERENCES products(id)
)
''')

main = ""
print("Добро пожаловать в магазин!")
print("1. Регистрация нового пользователя")
print("2. Добавить новую категорию")
print("3. Добавить новый продукт")
print("4. Создать новый заказ")
print("5. Добавить товар в заказ")
print("6. Посмотреть пользователей")
print("7. Посмотреть продукты")
print("8. Посмотреть все заказы")
print("0. Выход")
print("")

while main != "0":
    main = input("Выберите опцию: ")

    if main == "1":
        new_user = input("Введите имя пользователя: ")
        new_email = input("Введите электронную почту пользователя: ")
        cursor.execute('''
                                INSERT INTO users (name, email)
                                VALUES (?,?)
                                ''', (new_user, new_email))
        conn.commit()
        print("Покупатель добавлен в таблицу!")
        print("")
        print("")
        print("")

    if main == "2":
        new_category = input("Введите название категории: ")
        cursor.execute('''
                                INSERT INTO categories (name)
                                VALUES (?)
                                ''', (new_category,))
        conn.commit()
        print("Категория добавлена в таблицу!")
        print("")
        print("")
        print("")

    if main == "3":
        new_product = input("Введите название продукта: ")
        new_description = input("Введите описание продукта: ")
        new_price = input("Введите цену продукта: ")
        print("Катологи:")
        cursor.execute('''
                                  SELECT * FROM categories
                                  ''')
        rows = cursor.fetchall()
        columns = [description[0] for description in cursor.description]
        print(" | ".join(columns))
        print("-" * (len(columns) * 15))
        for row in rows:
            print(" | ".join(map(str, row)))
        cursor.execute('''
                   SELECT id FROM categories
                   ''')
        categor_id = int(input("Введите id католога продукта: "))
        cursor.execute('''
                                INSERT INTO products (name, description, price, category_id)
                                VALUES (?, ?, ?, ?)
                                ''', (new_product, new_description, new_price, categor_id))
        conn.commit()
        print("Продукт добавлен в таблицу!")
        print("")
        print("")
        print("")

    if main == "4":
        print("Таблица пользователей:")
        cursor.execute('''
                                                   SELECT * FROM users
                                                   ''')
        rows = cursor.fetchall()
        columns = [description[0] for description in cursor.description]
        print(" | ".join(columns))
        print("-" * (len(columns) * 15))
        for row in rows:
            print(" | ".join(map(str, row)))
        use_id = input("Введите id пользователя, создающий заказ: ")
        cursor.execute('''
                                        INSERT INTO orders (users_id)
                                        VALUES (?)
                                        ''', (use_id,))
        conn.commit()
        print("Заказ создан!")
        print("")
        print("")
        print("")
        conn.commit()

    elif main == "5":
        print("Католог заказов:")
        cursor.execute('''
                              SELECT * FROM orders
                              ''')
        rows = cursor.fetchall()
        columns = [description[0] for description in cursor.description]
        print(" | ".join(columns))
        print("-" * (len(columns) * 15))
        for row in rows:
            print(" | ".join(map(str, row)))
        cursor.execute('''
               SELECT id FROM orders
               ''')
        orde_id = int(input("Введите id заказа: "))
        print("Католог продуктов:")
        cursor.execute('''
                                           SELECT * FROM products
                                           ''')
        rows = cursor.fetchall()
        columns = [description[0] for description in cursor.description]
        print(" | ".join(columns))
        print("-" * (len(columns) * 15))
        for row in rows:
            print(" | ".join(map(str, row)))
        produc_id = input("Введите id продукта: ")
        quantit = int(input("Введите кол-во продуктов: "))
        status_order = "В обработке"
        cursor.execute('''
                                                    INSERT INTO order_items (quantity)
                                                    VALUES (?)
                                                    ''', (quantit,))
        conn.commit()

    elif main == "6":
        print("Таблица пользователей:")
        cursor.execute('''
                          SELECT * FROM users
                          ''')
        rows = cursor.fetchall()
        columns = [description[0] for description in cursor.description]
        print(" | ".join(columns))
        print("-" * (len(columns) * 15))
        for row in rows:
            print(" | ".join(map(str, row)))

    elif main == "7":
        print("Таблица продуктов:")
        cursor.execute('''
                    SELECT p.name, p.description, p.price, c.name
                    FROM products p
                    JOIN categories c ON p.category_id = c.id
                ''')
        rows = cursor.fetchall()
        columns = ["Название", "описание", "Цена", "Категория"]
        print(" | ".join(columns))
        print("-" * (len(" | ".join(columns))))
        for row in rows:
            print(" | ".join(map(str, row)))

    elif main == "8":
        print("Таблица заказов:")
        cursor.execute('''
                    SELECT o.status, o.order_date, u.name
                    FROM orders o
                    JOIN users u ON o.users_id = m.id
                ''')
        rows = cursor.fetchall()
        columns = ["Cтатус", "Время создания", "Имя пользователя"]
        print(" | ".join(columns))
        print("-" * (len(" | ".join(columns))))
        for row in rows:
            print(" | ".join(map(str, row)))