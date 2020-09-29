class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        self.min = []
    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.data.append(x)
        if len(self.min) == 0 or x <= self.min[-1]:
            self.min.append(x)

    def pop(self):
        """
        :rtype: None
        """
        pop = self.data.pop()
        if pop == self.min[-1]:
            self.min.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.data[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min[-1]

if __name__ == "__main__":
    minStack = MinStack()
    assert minStack.push(-2) == None
    assert minStack.push(0) == None
    assert minStack.push(-3) == None
    assert minStack.getMin() == -3
    assert minStack.pop() == None
    assert minStack.top() == 0
    assert minStack.getMin() == -2