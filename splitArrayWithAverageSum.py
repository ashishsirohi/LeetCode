class Solution(object):
    def splitArraySameAverage(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if len(A) <= 1:
            return False
        self.nums = A
        self.half = sum(A) / 2
        self.l = (len(A) / 2 ) + 1
        self.avg = sum(A) / self.l
        for i in range(len(A)):
            remaining = list(A)
            remaining.remove(A[i])
            res = self.bfs(A[i], sum(remaining), len(remaining), i + 1)
            if res:
                return True

            break

        return False

    def bfs(self, node, s, l, index):
        mys = []
        mys.append((node, 1, node, l, s, index))

        while mys:
            curr, l1, s1, l2, s2, index = mys.pop()

            if l1 > self.l:
                continue

            avg1 = s1 / float(l1)
            avg2 = s2 / float(l2)

            if avg1 > self.avg:
                continue

            if l1 and l2 and avg1 == avg2:
                return True

            for i in range(index, len(self.nums)):
                if l1 + 1 < self.l:
                    mys.append((self.nums[i], l1 + 1, s1 + self.nums[i], l2 - 1, s2 - self.nums[i], i + 1))

        return False

n = [5,3,11,19,2]

print Solution().splitArraySameAverage(n)