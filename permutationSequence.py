class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        if not k:
            return ""

        num = range(1, n + 1)
        num = [str(x) for x in num]
        fact = 0
        i = 0
        tmp = self.fact(len(num) - 1)
        path = ""
        while num and fact < k:
            fact += tmp
            i += 1

            if fact >= k:
                i -= 1
                fact -= self.fact(len(num) -  1)
                path += str(num[i])
                num.remove(num[i])
                i = 0
                tmp = self.fact(len(num) - 1)

        print num
        path += "".join(num)
        return path

    def fact(self, n):
        result = 1
        for i in range(1, n + 1):
            result *= i

        return result

n = 9
k = 1354

print Solution().getPermutation(n, k)