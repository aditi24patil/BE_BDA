A = [[1,2],
     [3,4]]

B = [[5,6],
     [7,8]]

rows_A = len(A)
cols_A = len(A[0])
cols_B = len(B[0])

def mapper(A,B):
    mapped=[]
    for i in range(rows_A):
        for j in range(cols_B):
           for k in range(cols_A):
               mapped.append(((i,j),(A[i][k],B[k][j])))
    return mapped

def shuffle(mapped):
    grouped={}
    for key,value in mapped:
        if key not in grouped:
            grouped[key]=[]
        grouped[key].append(value)
    return grouped

def reducer(grouped):
    result={}
    for key in grouped:
        sum_val=0
        for a,b in grouped[key]:
            sum_val+=a*b
        result[key]=sum_val
    return result

mapped=mapper(A,B)
grouped=shuffle(mapped)
result=reducer(grouped)

C=[[0 for _ in range(cols_B)] for _ in range(rows_A)]
for (i,j), value in result.items():
    C[i][j]=value
print('Result Matrix :')
for row in C:
    print(row)
     
