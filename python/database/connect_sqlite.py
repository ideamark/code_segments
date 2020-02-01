import sqlite3

databaseDir =
cx = sqlite3.connect(databaseDir)
cu = cx.cursor()

cu.execute('select * from T_MEMORY')
print(cu.fetchall())
