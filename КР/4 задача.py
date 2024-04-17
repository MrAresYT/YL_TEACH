class Climate:
    def __init__(self, *ls, mode='XPC18-M'):
        self.ls = ls
        self.mode = mode

    def __mul__(self, other):
        ls = [max(self.ls[i], other.ls[i]) for i in range(len(self.ls))]
        mode = max(self.mode, other.mode)
        return Climate(*ls, mode=mode)

    def __isub__(self, other):
        self.ls = [min(self.ls[i], other.ls[i]) for i in range(len(self.ls))]
        return self

    def __call__(self, num: int):
        out = []
        for i in self.ls:
            if isinstance(i, str):
                if len(i) > num:
                    out.append(i)
            else:
                if i > num:
                    out.append(i)
        return out

    def __str__(self):
        return f'Climate(mode: {self.mode}, features: {", ".join(map(str, self.ls))})'


params1 = ['traditional', 'filtration', 35, 27, 35, 'outdoor', 2]
params2 = ['drip', 'static', 29, 50, 30, 'wall mounted', 3]
cl1 = Climate(*params1)
cl2 = Climate(*params2, mode='XPK13-m')
cl = cl1 * cl2
print(cl1, cl2, cl, sep='\n')