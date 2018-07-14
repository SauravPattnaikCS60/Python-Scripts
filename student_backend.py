import sqlite3


def connect():
    conn = sqlite3.connect('student.db')
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS STD(id integer primary key,roll integer,sgpa real,sem text,year text)")
    conn.commit()
    conn.close()


def view():
    conn = sqlite3.connect('student.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM STD")
    rows = cur.fetchall()
    conn.close()
    return rows


def insert(roll, sgpa, sem, year):
    conn = sqlite3.connect('student.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO STD VALUES(NULL,?,?,?,?)", (roll, sgpa, sem, year))
    conn.commit()
    conn.close()


def delete(id):
    conn = sqlite3.connect('student.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM STD WHERE ID =?", (id,))
    conn.commit()
    conn.close()


def search(roll="", sgpa="", sem="", year=""):
    conn = sqlite3.connect('student.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM STD WHERE roll=? or sgpa=? or sem=? or year=?", (roll, sgpa, sem, year))
    rows = cur.fetchall()
    conn.close()
    return rows


def update(id, roll, sgpa, sem, year):
    conn = sqlite3.connect('student.db')
    cur = conn.cursor()
    cur.execute("UPDATE STD SET roll=?,sgpa=?,sem=?,year=? WHERE id=?", (roll, sgpa, sem, year, id))
    conn.commit()
    conn.close()


connect()




