#Hive: Introduction Creation of Database and Table, Hive Partition, Hive Built in Function and Operators, Hive View and Index.
import sqlite3
import pandas as pd

conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

print("Database Created Successfully\n")

cursor.execute('''
CREATE TABLE students (
    id INTEGER,
    name TEXT,
    age INTEGER,
    course TEXT
)
''')

print("Table Created\n")

cursor.executemany('''
INSERT INTO students VALUES (?, ?, ?, ?)
''', [
    (1, 'Rahul', 21, 'BCA'),
    (2, 'Amit', 22, 'BBA'),
    (3, 'Sneha', 20, 'BSc'),
    (4, 'Priya', 23, 'BCom')
])

conn.commit()
print("Data Inserted\n")

print("All Students:")
df = pd.read_sql_query("SELECT * FROM students", conn)
print(df, "\n")

print("Partition (course = BCA):")
df_partition = pd.read_sql_query(
    "SELECT * FROM students WHERE course='BCA'", conn)
print(df_partition, "\n")

print("COUNT:", cursor.execute(
    "SELECT COUNT(*) FROM students").fetchone()[0])
print("AVG AGE:", cursor.execute(
    "SELECT AVG(age) FROM students").fetchone()[0])
print("MAX AGE:", cursor.execute(
    "SELECT MAX(age) FROM students").fetchone()[0], "\n")

print("Students with age > 21:")
df_filter = pd.read_sql_query(
    "SELECT * FROM students WHERE age > 21", conn)
print(df_filter, "\n")

# FIXED VIEW CREATION
cursor.execute('''
CREATE VIEW student_view AS
SELECT name, age FROM students
''')

print("View Created\n")

print("View Data:")
df_view = pd.read_sql_query(
    "SELECT * FROM student_view", conn)
print(df_view, "\n")

print("Execution Completed Successfully!")
