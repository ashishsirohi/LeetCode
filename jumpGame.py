class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        import Queue
        myQueue = Queue.Queue()
        myQueue.put(0)
        visited = [0]

        while not myQueue.empty():
            index = myQueue.get()
            print index

            if index == len(nums) - 1:
                return True

            for i in range(index + 1, index + nums[index] + 1):
                if i < len(nums) and i not in visited:
                    visited.append(i)
                    myQueue.put(i)

        return False

n = [3,2,2,0,4]
s = Solution()
print s.canJump(n)