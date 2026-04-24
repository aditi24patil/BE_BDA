#Develop a MapReduce program to find the grades of students.

data = [
    ("Asha", 85),
    ("Krishna", 67),
    ("Khushi", 92),
    ("Soham", 74),
    ("Esha", 58),
    ("Ajay", 45)
]

def mapper(record):
    name, marks = record

    if marks >= 90:
        grade = 'A'
    elif marks >= 75:
        grade = "B"
    elif marks >= 60:
        grade = "C"
    elif marks >= 50:
        grade = "D"
    else:
        grade = "F"

    return (name, grade)

def reducer(mapped_data):
    result = {}
    for name, grade in mapped_data:
        result[name] = grade
    return result

mapped = list(map(mapper, data))
reduced = reducer(mapped)

print("Student grades:")
for student, grade in reduced.items():
    print(f"{student}: {grade}")
 
