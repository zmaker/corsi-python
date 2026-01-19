import sqlite3

conn = sqlite3.connect("pythondb.db")
cur = conn.cursor()

sql = f"create table coffee ("\
    "id int primary key,"\
    "nome varchar(20) not null,"\
    "peso float default 0 "\
    ")"

cur.execute(sql)
conn.commit()

conn.close()

