class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        myStack = []

        for p in prices:
            if not myStack:
                myStack.append(p)
            else:
                if myStack[-1] >= p:
                    top = myStack.pop()
                    item = top
                    while myStack:
                        item = myStack.pop()
                    myStack.append(p)
                    profit += top - item
                else:
                    myStack.append(p)

        if myStack:
            top = myStack.pop()
            item = top
            while myStack and myStack[-1] <= top:
                item = myStack.pop()

            profit += top - item

        return profit

s = Solution()
p = [2,4,5,1,6,7,9,0,4]
p = [1,4,2,1]
p = [1,9,6,9,1,7,1,1,5,9,9,9]
print s.maxProfit(p)