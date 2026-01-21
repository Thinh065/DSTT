# Bài tập 1: Giải phương trình với Sympy
from sympy import Symbol, solve
x = Symbol('x')
bieuthuc = x + 3 - 5
print(solve(bieuthuc)) # Kết quả: [2]

bieuthuc = x**2 + 3 - 5
nghiemx = solve(bieuthuc)
print(nghiemx) # Kết quả: [-sqrt(2), sqrt(2)]
print(nghiemx[1]) # Kết quả: sqrt(2)

# Bài tập 2: Giải phương trình bậc 2 
from sympy import solve
x = Symbol('x')
ptb2 = x**2 + 9*x +8
print(solve(ptb2, dict = True)) # Kết quả: [{x: -8}, {x: -1}]

ptb2 = x**2 + 1*x + 10
nghiemx = solve(ptb2, dict = True)
print(nghiemx) # Kết quả: [{x: -1/2 - I*sqrt(39)/2}, {x: -1/2 + I*sqrt(39)/2}]

# Bài tập 3: Giải phương trình 1 biến biểu diễn đại số các biến còn lại 
x = Symbol('x')
a = Symbol('a')
b = Symbol('b')
c = Symbol('c')
ptb2 = a*x*x + b*x + c
nghiem = solve(ptb2, x, dict=True)
print(nghiem) # Kết quả: [{x: (-b - sqrt(b**2 - 4*a*c))/(2*a)}, {x: (-b + sqrt(b**2 - 4*a*c))/(2*a)}]

# Bài tập 4: Giải hệ phương trình 
from sympy import Symbol, solve
x = Symbol('x')
y = Symbol('y')
pt1 = 2*x+3*y-12
pt2 = 3*x-2*y-5 
print(solve((pt1, pt2), dict=True)) # Kết quả: [{x: 3, y: 2}]

nghiem = solve((pt1, pt2), dict=True)
nghiem = nghiem[0]
print(pt1.subs({x:nghiem[x], y:nghiem[y]})) # Kết quả: 0
print(pt2.subs({x:nghiem[x], y:nghiem[y]})) # Kết quả: 0

# Bài tập 5: Thể hiện ma trận bằng numpy 
import numpy as np
from numpy import *
M1 = np.array([ [9, 12], [23,30] ])
print(M1) # Kết quả: [[ 9 12]
          #          [23 30]]
        
u = np.array([ 2, 1])
tichM1u = M1.dot(u)
print(tichM1u) # Kết quả: [30 76]

tichuM1 = u.dot(M1)
print(tichuM1) # Kết quả: [41 54]

print(np.dot(M1, u) ) # Kết quả: [30 76]

print(np.dot(u, M1) ) # Kết quả: [41 54]

# Thực hành và cho biết kết quả các lệnh sau: 
mat1 = np.zeros( [5,5]) 
print(mat1) # Kết quả: ma trận 5x5 toàn số 0
mat2 = np.ones( [5,5]) 
print(mat2) # Kết quả: ma trận 5x5 toàn số 1
mat3 = mat1 + 2* mat2   
print(mat3) # Kết quả: ma trận 5x5 toàn số 2
mat4 = mat3 
mat3[3][2] = 10 
print(mat4) # Kết quả: ma trận 5x5 với phần tử hàng 4 cột 3 là 10
print(mat3) # Kết quả: ma trận 5x5 với phần tử hàng 4 cột 3 là 10
mat5 = np.copy(mat3) 
mat3[3][2] = 10 
print(mat3) # Kết quả: ma trận 5x5 với phần tử hàng 4 cột 3 là 10
print(mat4) # Kết quả: ma trận 5x5 với phần tử hàng 4 cột 3 là 10
print(mat5) # Kết quả: ma trận 5x5 với phần tử hàng 4 cột 3 là 10
mat6 = np.empty([4, 5]) 
print(mat6) # Kết quả: ma trận 4x5 với các phần tử rỗng (giá trị không xác định)
mat7 = np.identity(4) 
print(mat7) # Kết quả: ma trận I4x4 (ma trận đơn vị cấp 4)
mat8 = np.random.random([4,5])
print(mat8) # Kết quả: ma trận 4x5 với các phần tử ngẫu nhiên từ 0 đến 1

# Bài tập 6: Tìm chỗ đóng quân:
# a/ An toàn trong chiến dịch ngắn hạn 1-2 ngày (có yếu tố tránh lộ bí mật; không quan tâm đến các yếu tố khác);
from numpy import *
import numpy as np
MTE = np.array([[0, 0, 0, 10, 0],                           # [T, T, T, F, T]
                [0, 0, 0, 10, 0], # vậy các vị trí an toàn    [T, T, T, F, T]
                [0, 5, 15, 5, 0],                           # [T, T, F, T, T]
                [0, 20, 5, 0, 0]])                          # [T, F, T, T, T]
# b/ An toàn trong tập luyện thời bình (không cần xét yếu tố tránh lộ bí mật và bệnh dịch)
