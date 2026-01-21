import numpy as np  
from numpy import * # không cần phải bổ sung tên thư viện numpy (np.) ở phía trước các câu lệnh.
# vec1 = np.array([1., 3., 5.])
# print(vec1 * 2)  # Kết quả: [2. 6. 10.]

# print(vec1 * vec1)  # Kết quả: [ 1.  9. 25.]

# print(vec1 /2) # Kết quả: [0.5 1.5 2.5]

# print(vec1 + vec1)  # Kết quả: [ 2.  6. 10.]

# vec2 = np.array([2., 4.])
# print(vec1 + vec2) # lỗi vì kích thước không khớp

# vec3 = np.array([2., 4., 6.])
# print(vec1 + vec3) # Kết quả: [ 3.  7. 11.]

# print(vec1 / vec3 ) # Kết quả: [0.5        0.75       0.83333333]

# print(2* vec1 + 5* vec3) # Kết quả: [12. 26. 40.]

# print(vec1 * vec3) # Kết quả: [ 2. 12. 30.]

# print(vec3[2]) # Kết quả: 6.0

# vec4 = np.linspace(0, 20, 5)
# print(vec4) # Kết quả: [ 0.  5. 10. 15. 20.]

# Tạo các vector toàn 0:
# vec5 = np.zeros(5) 
# print(vec5) # Kết quả: [0. 0. 0. 0. 0.]

# Tạo các vector toàn 1:
# vec6 = np.ones(5)
# print(vec6) # Kết quả: [1. 1. 1. 1. 1.]

# Tạo vector ảo (giá trị rỗng): 
# vec7 = np.empty(5)
# print(vec7) # Kết quả: [1. 1. 1. 1. 1.] (giá trị rỗng, không xác định)

# Tạo vector các giá trị ngẫu nhiên từ 0 đến 1:
# import numpy as np
# print(np.random.rand(5)) # Kết quả: [0.5488135  0.71518937 0.60276338 0.54488318 0.4236548 ] (giá trị ngẫu nhiên)

v = np.array([1., 3., 5.]) 

# Lệnh lấy tổng các thành phần của vector:
print(np.sum(v))  # Kết quả: 9.0

# Lệnh xem số chiều của một vector:
print(v.shape)  # Kết quả: (3,)

# Thử nghiệm “chuyển vị” vector:
print(v.transpose())  # Kết quả: [1. 3. 5.] (không thay đổi gì vì v là vector hàng)

# Lệnh lấy một phần của vector:
v1 = v[:2]
print(v1)  # Kết quả: [1. 3.]

v[0] = 5
print(v)  # Kết quả: [5. 3. 5.]

print(v1)  # Kết quả: [5. 3.]

# v1[:2] = [1., 2., 3.] 
# print(v1) # lỗi vì kích thước không khớp

v1[:2] = [1., 2] 

print(v1) # Kết quả: [1. 2.]

v3 = 2 * v[:2] + v1 * 3
print(v3)  # Kết quả: [ 5. 10.]

# v1 = [4, 6]
print(v3) # Kết quả: [ 5. 10.]

print(v)  # Kết quả: [1. 2. 5.]

print(v + 10.0 ) # Kết quả: [11. 12. 15.]

print(np.sqrt(v) )  # Kết quả: [1.         1.41421356 2.23606798]

print(np.cos(v) )  # Kết quả: [ 0.54030231 -0.41614684  0.28366219]

print(np.sin(v) )  # Kết quả: [ 0.84147098  0.90929743 -0.95892427]

# Tích vô hướng của hai vector (kết quả là một số): 
print(np.dot(v1, v3) )  # Kết quả: 25.0 # np.dot(v1, v3) chỉ dùng được khi v1, v3 là list hoặc numpy array

print(v1.dot(v3)) # Kết quả: 25.0 # v1.dot(v3) chỉ dùng được khi v1, v3 là numpy array

print( v3.dot(v1) ) # Kết quả: 25.0 # v3.dot(v1) chỉ dùng được khi v1, v3 là numpy array
