import sqlite3

# SQLite veritabanı dosyasının yolu
sqlite_db_path = "my_toy_altersvorsorgeDB.db"  # Veritabanı dosya adını burada belirleyin

# Veritabanına bağlanma (dosya yoksa oluşturulur)
connection = sqlite3.connect(sqlite_db_path)

# Bir imleç oluşturma
cursor = connection.cursor()

# 'employees' adlı tabloyu oluşturma
cursor.execute('''
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    age INTEGER,
    department TEXT
);
''')

# Örnek verileri ekleme
employees_data = [
    ("John", "Doe", 28, "Engineering"),
    ("Jane", "Smith", 34, "Marketing"),
    ("Emily", "Davis", 22, "Sales"),
    ("Michael", "Brown", 45, "Management"),
    ("Sarah", "Wilson", 30, "Engineering"),
]

cursor.executemany('''
INSERT INTO employees (first_name, last_name, age, department)
VALUES (?, ?, ?, ?);
''', employees_data)

# Değişiklikleri kaydetme
connection.commit()

# Bağlantıyı kapatma
connection.close()

print(f"Veritabanı '{sqlite_db_path}' oluşturuldu ve 'employees' tablosuna örnek veriler eklendi.")

