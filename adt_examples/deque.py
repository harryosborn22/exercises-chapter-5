class Deque:
    def __init__(self, n):
        self.startpos = 0
        self.endpos = 0
        self.mydeque = [None] * n

    def append(self, x):
        self.mydeque[self.endpos] = x
        self.endpos += 1
        print(self.endpos, "2")

    def appendleft(self, x):
        self.mydeque[self.startpos - 1] = x
        self.startpos -= 1
    
    def pop(self):
        self.endpos -= 1
        return self.mydeque.pop(self.endpos)
    
    def popleft(self):
        self.startpos += 1
        return self.mydeque.pop(self.startpos - 1)
    
    def peek(self):
        return self.mydeque[self.endpos - 1]
    
    def peekleft(self):
        return self.mydeque[self.startpos]
    
    def __len__(self):
        return self.endpos - self.startpos
    
Q = Deque(1)
Q.append(1)
print(Q.pop())