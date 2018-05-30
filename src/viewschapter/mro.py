class A:
    def do(self):
        print("A")


class B:
    def do(self):
        print("B")


class BA(B, A):
    pass


class AB(A, B):
    pass


BA().do()  # Prints B
AB().do()  # Prints A


print(AB.__mro__)
