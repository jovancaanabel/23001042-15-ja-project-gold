import sqlite3

conn = sqlite3.connect('data/binar_data_science.db')
print("Opened database successfully")
print()

print("List of Users:")
cursorObj = conn.execute("SELECT * FROM users;")


#"SELECT * FROM users WHERE umur = 30;"
cursor = conn.execute("SELECT * FROM users WHERE umur = 30;")
#SELECT * FROM users WHERE  umur = '30'

for baris in cursorObj:
    print(baris)
    # print(baris[1])


print()
print("Operation done successfully")
conn.close()

