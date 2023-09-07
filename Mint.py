class Mint:

    def __init__(self, val=0, mod=int(1e9+7)):
        self.mod = mod
        self.val = val % self.mod

    def __str__(self): return str(self.val)

    def __int__(self): return self.val

    def __hash__(self): return self.val

    def __add__(self, other):
        if type(other) is Mint: other = other.val
        self.val = (self.val + other) % self.mod
        return self.val

    def __sub__(self, other):
        if type(other) is Mint: other = other.val
        self.val = (self.val - other + self.mod) % self.mod
        return self.val

    def __mul__(self, other):
        if type(other) is Mint: other = other.val
        self.val = self.val * other % self.mod
        return self.val

    def __mod__(self, other):
        if type(other) is Mint: other = other.val
        self.val = self.val % other
        return self.val

    def fst_pow(self, exp):
        if exp <= 1: return self.val ** exp
        return max(exp % 2 * self.val, 1) * self.fst_pow(exp // 2) ** 2 % self.mod

    def __pow__(self, other):
        if type(other) is Mint: other = other.val
        self.val = self.fst_pow(other)
        return self.val

    def __eq__(self, other):
        if type(other) is Mint: other = other.val
        return self.val == other

    def __neg__(self):
        self.val = -self.val
        return self.val