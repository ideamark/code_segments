import MySQLdb as mdb

con = mdb.connect('localhost', 'UserName', 'PassWord', 'databaseName');

with con: 

    cur = con.cursor()
    cur.execute("SELECT * FROM xxxx")
	#    cur.execute("SHOW TABLES")
	#    cur.execute("SHOW DATABASES")

    rows = cur.fetchall()

    for row in rows:
        print row
