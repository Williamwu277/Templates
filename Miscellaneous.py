INT_MAX, INT_MIN, LONG_MAX, LONG_MIN = 2147483647, -2147483648, 9223372036854775807, -9223372036854775808
MOD = 1e9 + 7

def gcd(a, b):
    if a == 0: return b
    return gcd(b % a, a)


def lcm(a, b): return a // gcd(a, b) * b


def power(base, exponent, mod=int(1e9 + 7)):
    if exponent <= 1: return base ** exponent
    return max(exponent % 2 * base, 1) * power(base, exponent // 2, mod) ** 2 % mod


def make(n, a=0): return [a for _ in range(n)]


def fill(arr, left=0, right=INT_MAX, a=0):
    for i in range(left, min(right, len(arr))): arr[i] = a


def psa(arr):
    for i in range(1, len(arr)): arr[i] += arr[i - 1]


def psa2d(arr):
    for i in range(1, len(arr)):
        for j in range(1, len(arr[i])): arr[i][j] += arr[i - 1][j] + arr[i][j - 1] - arr[i - 1][j - 1]