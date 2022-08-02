# MRO - Method Resolution Order
class A:
    num = 10


class B(A):
    pass


class C(A):
    pass


class D(B, C):
    pass


print(D.mro())
print(D.num)


# D
#     B
#         A
#     C
#         A

class X:
    pass


class Y:
    pass


class Z:
    pass


class A(X, Y):
    pass


class B(Z, Y):
    pass


class M(B, A, Z):
    pass


# M
#     B
#         A
#         Z
#     A
#         X
#         Y
#     Z
#         Y
#         Z
