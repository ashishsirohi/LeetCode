class MyStack(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        import Queue
        self.myStack = Queue.Queue()
        self.topEle = None

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.topEle = x
        self.myStack.put(x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        import Queue
        tmpQueue = Queue.Queue()
        res = None
        while True:
            item = self.myStack.get()
            if self.myStack.empty():
                res = item
                break
            else:
                tmpQueue.put(item)

        self.topEle = None
        while not tmpQueue.empty():
            item = tmpQueue.get()
            if tmpQueue.empty:
                self.topEle = item

            self.myStack.put(item)

        return res

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.topEle

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        if self.myStack.empty():
            return True
        else:
            return False



# Your MyStack object will be instantiated and called as such:
obj = MyStack()
obj.push(5)
param_2 = obj.pop()
param_3 = obj.top()
param_4 = obj.empty()
print param_2, param_3, param_4