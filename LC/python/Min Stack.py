class MinStack:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    
    # @param x, an integer
    # @return an integer
    def push(self, x):
        self.stack1.append(x) 
        if self.stack2 == [] or x <= self.stack2[-1]:
            self.stack2.append(x)
        return x

    # @return nothing
    def pop(self):
        minimum = self.stack1.pop()
        if minimum == self.stack2[-1]:
            self.stack2.pop()
        
    # @return an integer
    def top(self):
        return self.stack1[-1]

    # @return an integer
    def getMin(self):
        return self.stack2[-1]
        
