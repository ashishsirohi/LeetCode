class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A) < 3:
            return 0

        diffSet = set()

        count = 0
        currDiff = abs(A[0] - A[1])
        tmp = 0
        for i in range(1, len(A) - 1):
            if abs(A[i] - A[i + 1]) == currDiff:
                tmp += 1
            else:
                if tmp:
                    count += tmp + 1
                tmp = 0
                currDiff = abs(A[i] - A[i + 1])

        if tmp:
            count += tmp + 1

        return count

n = [1,2,5,6]
s = Solution()
print s.numberOfArithmeticSlices(n)