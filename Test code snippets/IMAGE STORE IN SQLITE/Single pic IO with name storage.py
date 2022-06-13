import sqlite3
from time import strftime

#=======================================================================
# CREATES OR OPENS DB

a=strftime("%d-%m-%Y--%H#%M#%S")
conn = sqlite3.connect(a+'.db')

cursor = conn.cursor()

conn.execute('''CREATE TABLE EXP(ID INTEGER PRIMARY KEY AUTOINCREMENT,NAME TEXT,IMG BLOB);''')
print "Table created successfully";

conn.commit()


#=======================================================================
#STORE IMG
  
path='B:\\BLACK BOX\\IMAGE STORE IN SQLITE\\5 cmps.jpg'

na= path.lstrip('B:\\BLACK BOX\\IMAGE STORE IN SQLITE\\')
print(na)


with open(path, "rb") as input_file:
    ablob = input_file.read()
    cursor.execute("INSERT INTO EXP(NAME,IMG) VALUES(?,?)", [na,sqlite3.Binary(ablob)])
    conn.commit()

#=======================================================================
    #RETRIEVE BACK IMG


cursor.execute("SELECT NAME FROM EXP WHERE id = 1")
nm=cursor.fetchone()
print("op_"+nm[0])
with open("op_"+nm[0], "wb") as output_file:
    
    cursor.execute("SELECT IMG FROM EXP WHERE id = 1")
    ablob = cursor.fetchone()
    output_file.write(ablob[0])

cursor.close()
conn.close()
