class Solution(object):
    def monotoneIncreasingDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        n = list(str(N))

        for i in range(len(n) - 1, -1, -1):
            for j in range(int(n[i]), -1, -1):
                n[i] = str(j)
                flag = False
                for k in range(1, len(n)):
                    if n[k] >= n[k - 1]:
                        continue
                    else:
                        flag = True
                        break

                if not flag:
                    res = [str(x) for x in n]
                    res2 = int("".join(res))
                    if res2 <= N:
                        return res2

            n[i] = '9'

        res = [str(x) for x in n]
        return int("".join(res))


n = 332
print Solution().monotoneIncreasingDigits(n)