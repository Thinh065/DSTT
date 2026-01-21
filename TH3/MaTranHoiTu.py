# Ma trận phân kỳ:
import numpy as np
# Tính ma trận A: 
A = np.array([ [0,1], [1,0]]) 
print("Ma trận A:\n", A) 
temp = A.dot(A) # tính toán lần thứ 1
print("Ma trận A^2:\n", temp) 
k= 6
for i in range(k-1):
    temp = temp.dot(A)
    print (temp)
    print('---') 

# Tính ma trận B: 
B = np.array([ [0,-1], [-1,0]])
print("Ma trận B:\n", B)
temp = B.dot(B) # tính toán lần thứ 1
print("Ma trận B^2:\n", temp)
k= 5
for i in range(k-1):
    temp = temp.dot(B)
    print (temp)
    print('---') 

# Ma trận hội tụ - Convergent matrix: 
C = np.array([ [1, 0, 0], [0, 0.5, 1], [0, 0, 0.5] ]) 
print("Ma trận C:\n", C)
temp = C.dot(C)
print("Ma trận C^2:\n", temp)
k= 1000 
for i in range(k-1):
    temp = temp.dot(C)
print (temp)
# Sau đó, thực hiện thêm 1 lần tích 1000 lần nữa:
k= 1000
for i in range(k-1):
    temp = temp.dot(C)
print(temp) 