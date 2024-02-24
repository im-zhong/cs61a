# try this on pythontutor


class A:
    x, y = 0, 0


class B(A):
    pass


class C(A):
    pass


print(A.x, B.x, C.x)

B.x = 2
print(A.x, B.x, C.x)

A.x += 1
print(A.x, B.x, C.x)

obj = C()
obj.y = 1
print(C.y == obj.y)

A.y = obj.y
print(A.y, B.y, C.y, obj.y)

# modify to reference is in-place, such A.x =1 or list[0] = 1
