import sqlite3

conn = sqlite3.connect('data/binar_data_science.db')
print("Opened database successfully")

conn.execute("INSERT INTO users (username, email, umur, alamat) VALUES ('binaria', 'binaria@binar.com', 27, 'jakarta timur')")
conn.execute("INSERT INTO users VALUES ('bintang', 'bintang@binar.com', 30, 'Bandung')")

conn.commit()
print("Records created successfully")
conn.close()

