from numpy import sin, cos


class RPCalc:
    def __init__(self):
        self.stack = []

    def push(self, n):
        print(n)
        if n == "+":
            second = self.pop()
            first = self.pop()
            self.push(first + second)
        elif n == "-":
            second = self.pop()
            first = self.pop()
            self.push(first - second)
        elif n == "*":
            second = self.pop()
            first = self.pop()
            self.push(first * second)
        elif n == "/":
            second = self.pop()
            first = self.pop()
            self.push(first / second)
        elif n == "sin":
            first = self.pop()
            self.push(sin(first))
        elif n == "cos":
            first = self.pop()
            self.push(cos(first))
        else:
            print(self.stack)
            self.stack.append(n)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def __len__(self):
        return len(self.stack)
