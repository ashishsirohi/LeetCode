class Solution(object):
    def racecar(self, target):
        """
        :type target: int
        :rtype: int
        """
        if target == 0:
            return 0
        return self.bfs(1, 2, target)

    def bfs(self, start, S, t):
        import heapq
        myheap = []
        state = (1, start, S)
        heapq.heappush(myheap, (state))

        myset = set()
        myset.add(state)

        while myheap:
            path, pos, s = heapq.heappop(myheap)
            # pos, S, path = mystack.pop()

            if pos == t:
                return path

            if pos < 0:
                continue

            if pos > t * 2:
                continue

            if s > 0:
                if (pos, -1, path + 1) not in myset:
                    myset.add((path + 1, pos, -1))
                    state = (path + 1, pos, -1)
                    heapq.heappush(myheap, (state))
                    # mystack.append((pos, - 1, path + 1))
            else:
                if (pos, 1, path + 1) not in myset:
                    myset.add((path + 1, pos, 1))
                    state = (path + 1, pos, 1)
                    heapq.heappush(myheap, (state))
                    # mystack.append((pos, 1, path + 1))

            newP1 = pos + s
            if (newP1, s * 2, path + 1) not in myset:
                myset.add((path + 1, newP1, s * 2))
                state = (path + 1, newP1, s * 2)
                heapq.heappush(myheap, (state))
                # mystack.append((newP1, S * 2, path + 1))


print Solution().racecar(3)