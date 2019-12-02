import sqlite3 as sql
import os

ROOT = os.path.dirname(os.path.relpath(__file__))

def create_LR(experience):
    con = sql.connect(os.path.join(ROOT, 'database.db'))
    cur = con.cursor()
    cur.execute("insert into salary (experience) values(?, ?)", (experience))
    con.commit()
    cur.close()

def get_salary():
    con = sql.connect(os.path.join(ROOT, 'database.db'))
    cur = con.cursor()
    cur.execute("select * from salary")
    salary = cur.fetchall()
    return salary
