#Implement Matrix Multiplication using Map-Reduce
from collections import defaultdict

def mapper(A, B):
    mapped = []
    rows_A, cols_A, cols_B = len(A), len(A[0]), len(B[0])

    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                mapped.append((i, j), (A[i][k], B[k][j]))
    return mapped

def reducer(mapped):
    reduced = defaultdict(list)
    for key, (a, b) in mapped:
        result[key] += a * b
    return result

#Input
r1, c1 = map(int, input("Enter rows & cols of A: ").split())
print("Enter Matrx A:")
A = [list(map(int, input().split())) for _ in range(r1)]

r2, c2 = map(int, input("Enter rows & cols of B: ").split())
if c1 != r2:
    print("Multiplication not possible")
    exit()

print("Enter Matrix B:")
B = [list(map(int, input(). split())) for _ in range(r2)]

#Mapreduce
mapped = mapper(A, B)
result = reducer(mapped)

#Output
print("\nResult Matrix: ")
for i in range(r1):
    for j in range(c2):
        print(result[(i, j)], end=" ")
    print()
