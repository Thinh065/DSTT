from sympy import Symbol, simplify        
# x = Symbol('x') 
# f = x + x + x + 2
# print(f)

# a = Symbol('Noi')
# b = Symbol('Chim')
# print(3*b + 7*a)

# a = Symbol('Noi')
# b = Symbol('Chim')
# print(a.name)
# print(b.name)

# from sympy import Symbol
# x = Symbol('x')
# y = Symbol('y')
# # s = x*y + y*x
# # print(s)

# # p = x*(x+2*x)
# # print(p)    

# # p = (x+2)*(y+3) + (x+2)*(x-3)
# # print(p)

# # p = x*(-x+2*x-x)
# # print(p)

# p = (x+2)*(y+3)
# print(p.expand())

from sympy import factor
# bieuthuc = x**3 - y**3
# print(factor(bieuthuc))

from sympy import expand
# bieuthuc = (x - y)*(x**2 + x*y + y**2)
# print(expand(bieuthuc))

from sympy import Symbol
# x = Symbol('x')
# y = Symbol('y')
# bieuthuc = x*x - x*y + y*y
# print(bieuthuc)

# giatri = bieuthuc.subs({x:3, y:2})
# print(giatri)

# print(x)

# print(y)

# giatri = bieuthuc.subs({x:3, y:x}) 
# print(giatri)

# giatri = bieuthuc.subs({x:y, y:3})
# print(giatri)

# giatri = bieuthuc.subs({y:x}).subs({x:3})
# print(giatri)

from sympy import Symbol
# x = Symbol('x')
# y = Symbol('y') 
# bieuthuc = x*x - x*y + y*y
# # print(bieuthuc)
# bieuthuc_moi = bieuthuc.subs({x:1-y}) # x được thay thế bằng (1-y)
# print(bieuthuc_moi)

from sympy import simplify
# dongian = simplify(bieuthuc_moi)
# print(dongian)

from sympy import Symbol
from sympy import sin, cos
x = Symbol('x')
y = Symbol('y')
bt = sin(x)*cos(y) + cos(x)*sin(y)
bt_moi = simplify(bt)
print(bt_moi)