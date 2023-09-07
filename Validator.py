import sys
from collections import deque

INT_MAX, INT_MIN, LONG_MAX, LONG_MIN = 2147483647, -2147483648, 9223372036854775807, -9223372036854775808
MOD = 1e9 + 7


class Reader:

    def __init__(self): self.read_line = None

    def read(self):
        if not self.read_line: self.read_line = sys.stdin.readline().split()[::-1]
        return self.read_line.pop()


class Validator:

    def __init__(self):
        self.read_lines, self.begin, self.spaces, self.end, self.cur, self.actual = None, None, None, None, None, None

    def read(self):
        if not self.read_lines and not self.end and not self.spaces and not self.begin:
            self.read_lines, self.begin, self.spaces, self.end, self.cur = sys.stdin.readline(), [], [], -1, 0
            self.actual, pre = self.read_lines, " "
            for i in range(len(self.read_lines)):
                if pre == " " and self.read_lines[i] not in " \n": self.begin.append(i)
                if self.read_lines[i] == " ": self.spaces.append(i)
                elif self.read_lines[i] == "\n": self.end = i
                pre = self.read_lines[i]
            self.read_lines, self.spaces, self.begin = self.read_lines.split()[::-1], self.spaces[::-1], self.begin[::-1]

    def read_int(self, low=None, high=None):
        self.read()
        assert self.begin[-1] == self.cur
        self.begin.pop()
        self.cur += len(self.read_lines[-1])
        get = int(self.read_lines.pop())
        if low is not None: assert low <= get
        if high is not None: assert get <= high
        return get

    def read_int_array(self, count, low=None, high=None):
        arr = []
        for element in range(count):
            arr.append(self.read_int(low, high))
            if element == count-1: self.read_new_line()
            else: self.read_space()
        return arr

    def read_double(self, low=None, high=None):
        self.read()
        assert self.begin[-1] == self.cur
        self.begin.pop()
        self.cur += len(self.read_lines[-1])
        get = float(self.read_lines.pop())
        if low is not None: assert low <= get
        if high is not None: assert get <= high
        return get

    def read_char(self, available=None):
        self.read()
        assert self.begin[-1] == self.cur
        self.begin.pop()
        self.cur += 1
        if available is not None: assert self.read_lines[-1] in available
        assert len(self.read_lines[-1]) == 1
        return self.read_lines.pop()

    def read_string(self, low=None, high=None, available=None):
        self.read()
        get = self.read_lines.pop()
        assert self.begin[-1] == self.cur
        self.begin.pop()
        self.cur += len(get)
        if low is not None: assert low <= len(get)
        if high is not None: assert len(get) <= high
        if available:
            for i in range(len(get)): assert get[i] in available
        return get

    def read_line(self):
        # includes new line
        self.read()
        self.read_lines, self.spaces, self.end = None, None, None
        return self.actual[self.cur:]

    def read_space(self):
        self.read()
        assert self.spaces[-1] == self.cur
        self.cur += 1
        return self.spaces.pop()

    def read_new_line(self):
        self.read()
        assert self.end == self.cur
        self.cur += 1
        self.end = None
        return "\n"

    def read_end_of_line(self):
        self.read()
        assert (len(self.read_lines) == 0)
