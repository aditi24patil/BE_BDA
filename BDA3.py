#Develop a MapReduce program to find the grades of students.

from collections import defaultdict

data = [
    ("Vibha", 85),
    ("Archit", 75),
    ("Astuti", 67),
    ("Vivan", 73),
    ("Rohan", 92),
    ("Rahul", 74),
    ("Tarini", 58),
    ("Ajay", 45)
]

# Mapper
def mapper(record):
    name, marks = record
    return (name, marks)

# Shuffle
def shuffle(mapped_data):
    grouped = defaultdict(list)
    for name, marks in mapped_data:
        grouped[name].append(marks)
    return grouped

# Reducer
def reducer(grouped_data):
    result = {}

    for name, marks_list in grouped_data.items():
        avg = sum(marks_list) / len(marks_list)

        if avg >= 90:
            grade = 'A'
        elif avg >= 75:
            grade = 'B'
        elif avg >= 60:
            grade = 'C'
        elif avg >= 50:
            grade = 'D'
        else:
            grade = 'F'

        result[name] = grade

    return result


# Execution
mapped = list(map(mapper, data))
grouped = shuffle(mapped)
reduced = reducer(grouped)

print("Student grades:")
for student, grade in reduced.items():
    print(f"{student}: {grade}")

#################################################################################################################################################

from collections import defaultdict

# ---------------- MAPPER ----------------
def mapper(record):
    name, marks = record
    return (name, marks)

# ---------------- SHUFFLE ----------------
def shuffle(mapped_data):
    grouped = defaultdict(list)
    for name, marks in mapped_data:
        grouped[name].append(marks)
    return grouped

# ---------------- REDUCER ----------------
def assign_grade(avg):
    if avg >= 90:
        return 'A'
    elif avg >= 75:
        return 'B'
    elif avg >= 60:
        return 'C'
    elif avg >= 50:
        return 'D'
    else:
        return 'F'

def reducer(grouped_data):
    result = {}
    for name, marks_list in grouped_data.items():
        avg = sum(marks_list) / len(marks_list)
        grade = assign_grade(avg)
        result[name] = (avg, grade)
    return result


# ---------------- INPUT ----------------
n = int(input("Enter number of records: "))
print("Enter data (Name Marks):")

data = []
for _ in range(n):
    name, marks = input().split()
    data.append((name, int(marks)))


# ---------------- MAPREDUCE ----------------
mapped = list(map(mapper, data))
grouped = shuffle(mapped)
result = reducer(grouped)


# ---------------- OUTPUT ----------------
print("\nStudent Grades:")
for name, (avg, grade) in result.items():
    print(f"{name}: Avg = {avg:.2f}, Grade = {grade}")

