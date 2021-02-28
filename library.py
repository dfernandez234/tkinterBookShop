import sqlite3

##Create table

def connect():
    connection = sqlite3.connect('books.db')
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS book(id integer PRIMARY KEY, title TEXT NOT NULL, author TEXT, year INTEGER, isbn INTEGER)")
    connection.commit()
    connection.close()

def view_all():
    connection = sqlite3.connect('books.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM book")
    rows = cursor.fetchall()
    connection.close()
    return rows

def search_entry(title, author, year, ISBN):
    connection = sqlite3.connect('books.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR ISBN=?",(title,author,year,ISBN))
    rows = cursor.fetchall()
    connection.close()
    return rows

def add_entry(title, author, year, ISBN):
    connection = sqlite3.connect('books.db')
    cursor = connection.cursor()
    cursor.execute("INSERT INTO book (title, author, year, isbn) VALUES (?,?,?,?)",(title,author,year,ISBN))
    connection.commit()
    connection.close()
    
def update_selected(title, author, year, ISBN,id):
    connection = sqlite3.connect('books.db')
    cursor = connection.cursor()
    cursor.execute("UPDATE book SET title=?, author=?, year=?, ISBN=? WHERE id=?", (title,author,year,ISBN,id))
    connection.commit()
    connection.close()

def delete_selected(id):
    connection = sqlite3.connect('books.db')
    cursor = connection.cursor()
    cursor.execute("DELETE FROM book where id = ?",(id,))
    connection.commit()
    connection.close()


def delete_all():
    connection = sqlite3.connect('books.db')
    cursor = connection.cursor()
    cursor.execute("DELETE FROM book")
    connection.commit()
    connection.close()


if __name__ == "__main__":
    add_entry('My Book', 'Me', 1997, 340578)


    








