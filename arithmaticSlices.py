class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A) < 3:
            return 0

        diffDict = {}

        count = 0
        currDiff = A[0] - A[1]
        tmp = 0
        for i in range(1, len(A) - 1):
            if A[i] - A[i + 1] == currDiff:
                tmp += 1
            else:
                if tmp:
                    try:
                        diffDict[currDiff].append(tmp + 1)
                    except:
                        diffDict[currDiff] = [tmp + 1]
                tmp = 0
                currDiff = A[i] - A[i + 1]

        if tmp:
            try:
                diffDict[currDiff].append(tmp + 1)
            except:
                diffDict[currDiff] = [tmp + 1]

                # print diffDict
        for key, value in diffDict.iteritems():
            for num in value:
                for i in range(num):
                    count += i
        return count


n = [1,2,5,6]
s = Solution()
print s.numberOfArithmeticSlices(n)