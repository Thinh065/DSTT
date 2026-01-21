from scipy import linalg # Tải gói linalg của scipy vào bộ nhớ (để sử dụng)
import numpy as np # Tải gói numpy vào sử dụng với tên gọi là np
a = np.array([1, 2, 3])
b = np.array([(1+9j, 2j, 3j), (4j, 5j, 6j)]) # số phức
c = np.array([[ (0.5, 1.5, 10), (3,2,1) ] , [(6,5,4), (7,8,9)]]) # ma trận số thực 
# Các kiểu khai báo và khởi tạo ma trận: 
A = np.matrix(np.random.random( (2,2) ) )
B = np.asmatrix(b) # Chuyển b thành dạng ma trận
C = np.matrix(np.random.random( (10,5) ) )
D = np.matrix([ [4, 3], [2, 6] ])
F = np.eye(3, k=1) # tạo ma trận đường chéo. 3 là ma trận 3x3, k=1 là đường
# chéo nằm phía trên đường chéo chính (k = 0)

print("Ma trận A:\n", A)
print("Ma trận B:\n", B)
print("Ma trận C:\n", C)
print("Ma trận D:\n", D)
print("Ma trận F:\n", F)

# Các phép xử lý đơn giản 
# Xem hạng ma trận: 
print("Hạng của ma trận C:", np.linalg.matrix_rank(C))
# Tính ma trận nghịch đảo: 
print("Ma trận nghịch đảo của A:\n", A.I)
print("Ma trận nghịch đảo của A (sử dụng scipy.linalg.inv):\n", linalg.inv(A))
# Định thức ma trận: 
print("Định thức của A:", linalg.det(A))
# Chuyển đổi ma trận: 
print("Chuyển vị của A:\n", A.T)
print("Chuyển vị liên hợp của A:\n", A.H)

# Giải các loại phương trình tuyến tính: 
print("Nghiệm của phương trình Ax = b là:\n", linalg.solve(A, b))

E = np.matrix(a).T 
print(linalg.lstsq(F, E)) # Giải phương trình xấp xỉ F*x = E

# Các hàm trên ma trận 
print("Tổng của A và D:\n", np.add(A, D))

print("Hiệu của A và D:\n", np.subtract(A, D))

print("Thương của A và D:\n", np.divide(A, D))

print("Tích của A và D:\n", A @ D)

print("Tích của D và A:\n", np.multiply(D, A))

print("Tích của A và D:\n", np.dot(A, D))

print("Tích của A và D:\n", np.vdot(A, D))

# Hàm lũy thừa và logarith ma trận:
print("Ma trận lũy thừa của A:\n", linalg.expm(A))

print("Ma trận logarith của A:\n", linalg.logm(A))