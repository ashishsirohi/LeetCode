class Solution(object):
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        if not nums:
            return 0

        import Queue
        myQueue = Queue.Queue()
        myQueue.put((0, len(nums)))
        visited = [(0, len(nums))]
        count = 0
        while not myQueue.empty():
            left, right = myQueue.get()

            if sum(nums[left:right]) >= lower and sum(nums[left:right]) <= upper:
                print left, right
                count += 1

            child1 = (left+1, right)
            child2 = (left, right-1)
            if child1[0] != child1[1] and child1 not in visited:
                myQueue.put(child1)
                visited.append(child1)
            if child2[0] != child2[1] and child2 not in visited:
                myQueue.put(child2)
                visited.append(child2)

        return count



s = Solution()
n = [2147483647,-2147483648,-1,0]
l = -1
u = 0
print s.countRangeSum(n, l, u)