class SuperString:
    def __init__(self, p1: str):
        self.p1 = p1

    def __add__(self, other):
        return self.p1 + str(other)

    def __radd__(self, other):
        return str(other) + self.p1

a = 'Привет мир!'
b = 123

a = SuperString(a)
print(a + b)
print(b + a)

print(globals())