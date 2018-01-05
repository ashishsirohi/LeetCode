class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        left = 0
        minList = []
        for i in range(len(nums)):
            minList.append(min(nums[:i+1]))
        #print minList
        myStack = []
        for i in range(len(nums)-1, -1, -1):
            if not myStack:
                myStack.append(nums[i])
                continue
                
            if nums[i] > minList[i]:
                if myStack[-1] < nums[i]:
                    while myStack and myStack[-1] <= minList[i]:
                        myStack.pop()
                    if myStack and myStack[-1] < nums[i]:
                        return True
                myStack.append(nums[i])
                    
            else:
                continue
        
        return False
            
                
        