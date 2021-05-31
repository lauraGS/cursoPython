import mysql.connector

mydb = mysql.connector.connect(host="localhost", database="sqlexamples", user="jeffrey", password="")
mycursor = mydb.cursor()
mycursor.execute("SHOW tables")
l = []
for x in mycursor:
    l.append(x)
print(l)

print()

print("Lista datos tabla b")
mycursor.execute("select b1, b2 from b")
lista = []
for x in mycursor:
    print(x)
    lista.append(x)
print(lista)

mydb.close()
