#Implement Matrix Multiplication using Map-Reduce
from collections import defaultdict

def mapper(A, B):
    mapped = []
    rows_A, cols_A = len(A), len(A[0])
    rows_B, cols_B = len(B), len(B[0])

    # Emit A elements
    for i in range(rows_A):
        for k in range(cols_A):
            for j in range(cols_B):
                mapped.append(((i, j), ('A', k, A[i][k])))

    # Emit B elements
    for k in range(rows_B):
        for j in range(cols_B):
            for i in range(rows_A):
                mapped.append(((i, j), ('B', k, B[k][j])))

    return mapped


def shuffle_sort(mapped):
    grouped = defaultdict(list)
    for key, value in mapped:
        grouped[key].append(value)
    return grouped


def reducer(grouped):
    result = {}

    for (i, j), values in grouped.items():
        A_vals = {}
        B_vals = {}

        # Separate A and B values
        for tag, k, val in values:
            if tag == 'A':
                A_vals[k] = val
            else:
                B_vals[k] = val

        # Compute dot product
        total = 0
        for k in A_vals:
            if k in B_vals:
                total += A_vals[k] * B_vals[k]

        result[(i, j)] = total

    return result


# -------- INPUT --------
r1, c1 = map(int, input("Enter rows & cols of A: ").split())
print("Enter Matrix A:")
A = [list(map(int, input().split())) for _ in range(r1)]

r2, c2 = map(int, input("Enter rows & cols of B: ").split())

if c1 != r2:
    print("Multiplication not possible")
    exit()

print("Enter Matrix B:")
B = [list(map(int, input().split())) for _ in range(r2)]


# -------- MAPREDUCE --------
mapped = mapper(A, B)
grouped = shuffle_sort(mapped)
result = reducer(grouped)


# -------- OUTPUT --------
print("\nResult Matrix:")
for i in range(r1):
    for j in range(c2):
        print(result.get((i, j), 0), end=" ")
    print()
