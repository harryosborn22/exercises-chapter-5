class Deque:
    def __init__(self, n):
        self.startpos = 0
        self.endpos = 0
        self.mydeque = [None] * n
        self.n = n
        self.items = 0

    def append(self, x):
        if self.mydeque[self.endpos] is not None:
            self.startpos = self.change(self.startpos, 1)
        else:
            self.items += 1
        self.mydeque[self.endpos] = x
        self.endpos = self.change(self.endpos, 1)

    def appendleft(self, x):
        if self.mydeque[self.startpos - 1] is not None:
            self.endpos = self.change(self.endpos, -1)
        else:
            self.items += 1
        self.mydeque[self.startpos - 1] = x
        self.startpos = self.change(self.startpos, -1)

    def pop(self):
        self.endpos = self.change(self.endpos, -1)
        element = self.mydeque[self.endpos]
        self.mydeque[self.endpos] = None
        self.items -= 1
        return element

    def popleft(self):
        self.startpos = self.change(self.startpos, 1)
        element = self.mydeque[self.startpos - 1]
        self.mydeque[self.startpos - 1] = None
        self.items -= 1
        return element

    def peek(self):
        return self.mydeque[self.endpos - 1]

    def peekleft(self):
        return self.mydeque[self.startpos]

    def __len__(self):
        return self.items

    def change(self, var, x):
        if var + x >= self.n:
            return var + (x - self.n)
        elif var + x < 0:
            return var + (x + self.n)
        else:
            return var + x

    def __iter__(self):
        self.index = self.change(self.startpos, -1)
        self.passed = False
        return self

    def __next__(self):
        if self.index == self.endpos - 1 and self.passed:
            raise StopIteration
        else:
            self.passed = True
            self.index = self.change(self.index, 1)
            return self.mydeque[self.index]
