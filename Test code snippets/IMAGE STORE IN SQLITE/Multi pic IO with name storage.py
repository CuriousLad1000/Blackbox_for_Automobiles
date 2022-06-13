import sqlite3
from time import strftime
import glob

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

extns = ('*.png', '*.jpg', '*.gif')

for i in extns:
 for files in glob.glob(i):
  path='B:\\BLACK BOX\\IMAGE STORE IN SQLITE\\' + files
  print (path)
  with open(path, "rb") as input_file:
     ablob = input_file.read()
     cursor.execute("INSERT INTO EXP(NAME,IMG) VALUES(?,?)", [files,sqlite3.Binary(ablob)])
     conn.commit()

#=======================================================================
    #RETRIEVE BACK IMG


cursor.execute("SELECT COUNT(*) FROM EXP")
m=cursor.fetchone()
#print(m[0])     #  TELLS NO. OF ROWS OF DATA IN DB

OP_path='B:\\BLACK BOX\\IMAGE STORE IN SQLITE\\OUTPUT\\'

for i in range(m[0]):

 cursor.execute("SELECT NAME FROM EXP WHERE id ="+str(i+1))
 nm=cursor.fetchone()
 print("op_"+nm[0])

 with open(OP_path + "op_" + nm[0], "wb") as output_file:
     cursor.execute("SELECT IMG FROM EXP WHERE id =" + str(i+1))
     ablob = cursor.fetchone()
     output_file.write(ablob[0])

cursor.close()
conn.close()
