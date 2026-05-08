class MinStack:

    def __init__(self):
        self.ordered = []
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if (len(self.ordered) == 0):
            self.ordered.append(val)
        else:
            if (self.ordered[-1] >= val):
                self.ordered.append(val)

    def pop(self) -> None:
        if (self.stack[-1] == self.ordered[-1]):
            self.ordered.pop(-1)
        self.stack.pop(-1)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.ordered[-1]
