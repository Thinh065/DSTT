import numpy as np
# Ma trận Markov - Markov matrix:
# M = np.array([ [0.8, 0.3], [0.2, 0.7]])
# MM = M.dot(M) # tính M2, nghĩa là M^2
# print("Ma trận MM^2:\n", MM)

# MM = M.dot(M) # tính M3
# print("Ma trận MM^3:\n", MM)
# for i in range(100): # tính các M^ khác.
#     MM = MM.dot(M)
# print (MM) # kết luận xu hướng của M^n khi n tiến tới vô cùng

M = np.array([ [0.5, 0.5], [0.5, 0.5]])
MM = M.dot(M) # tính M2, nghĩa là M^2
print("Ma trận MM^2:\n", MM)

MM = M.dot(M) # tính M3
print("Ma trận MM^3:\n", MM)
for i in range(100): # tính các M^ khác.
    MM = MM.dot(M)
print (MM) # kết luận xu hướng của M^n khi n tiến tới vô cùng