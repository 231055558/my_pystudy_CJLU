import sqlite3
conn = sqlite3.connect('student.db')
cur = conn.cursor()
cur.execute('''create table student
(id integer primary key ,
name text,
sex text,
age text,
phnum text,
pyscore text,
single text
)''')
cur.execute("insert into student (name,sex,age,phnum,pyscore,single) values ('Li_Haoyang','男性','19','123456','100','单身')")
conn.commit()
conn.close