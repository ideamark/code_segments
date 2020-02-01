# coding: utf8

# Python2.6.2

import sqlite3

db = sqlite3.connect('test.db')
cur = db.cursor()

cur.execute("CREATE TABLE if not exists t (b BLOB);")

with open('test.gif', 'rb') as f:
    cur.execute("insert into t values(?)", (sqlite3.Binary(f.read()), ))
    db.commit()

cur.execute('select b from t limit 1')
b = cur.fetchone()[0]

print b

with open('2.gif', 'wb') as f:
    f.write(b)

db.close()
