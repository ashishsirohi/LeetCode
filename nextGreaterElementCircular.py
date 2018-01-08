class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = [-1]*len(nums)
        myStack = []
        j = 0
        while j < 2:
            for i in range(len(nums)):
                while myStack and nums[myStack[-1]] < nums[i]:
                    index = myStack.pop()
                    result[index] = nums[i]
                myStack.append(i)
            j += 1
        return result

s =  Solution()
nums = [1,4,1,2,1]
print s.nextGreaterElements(nums)