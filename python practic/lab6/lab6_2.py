class A:
    def __init__(self, a):
        self._a = a

    def show(self):
        print(self._a)


class B(A):
    def __init__(self, a, b):
        super(B, self).__init__(a)
        self._b = b

    def show(self):
        print(self._a, self._b)


class C(B):
    def __init__(self, a, b, c):
        super(C, self).__init__(a, b)
        self._c = c

    def show(self):
        print(self._a, self._b, self._c)


a = A(3)
b = B(5, 5)
c = C(3, 5, 7)
a.show()
b.show()
c.show()
