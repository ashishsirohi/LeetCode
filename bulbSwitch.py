class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        # O(n2) Solution
        """if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 1
        else:
            bulbs = [1]*n
            for i in range(2, n+1):
                for j in range(i, len(bulbs)+1, i):
                    if bulbs[j-1] == 1:
                        bulbs[j-1] = 0
                    else:
                        bulbs[j-1] = 1
        return bulbs.count(1)"""
        return int((n)**0.5)
        
        