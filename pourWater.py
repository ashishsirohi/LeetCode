class Solution(object):
    def pourWater(self, heights, V, K):
        """
        :type heights: List[int]
        :type V: int
        :type K: int
        :rtype: List[int]
        """
        i = 0
        while i < V:
            if K == 0:
                j = K
                flag = False
                lowPoint = max(heights)
                while j < len(heights) - 1:
                    if heights[j + 1] > heights[j]:
                        break

                    if heights[j + 1] < heights[j]:
                        if heights[j + 1] < lowPoint:
                            lowPoint = heights[j + 1]
                            lowIndex = j + 1
                        flag = True
                    j += 1

                if flag:
                    heights[lowIndex] += 1

                if not flag:
                    heights[K] +=1
            elif K == len(heights) - 1:
                j = K
                flag = False
                lowPoint = max(heights)
                while j > 0:
                    if heights[j - 1] > heights[j]:
                        break

                    if heights[j - 1] < heights[j]:
                        if heights[j - 1] < lowPoint:
                            lowPoint = heights[j - 1]
                            lowIndex = j - 1
                        flag = True
                    j -= 1

                if flag:
                    heights[lowIndex] += 1

                if not flag:
                    heights[K] += 1
            else:
                j = K
                flag1 = False
                lowPoint = max(heights)
                while j > 0:
                    if heights[j-1] > heights[j]:
                        break

                    if heights[j-1] < heights[j]:
                        if heights[j-1] < lowPoint:
                            lowPoint = heights[j - 1]
                            lowIndex = j - 1
                        flag1 = True
                    j -=1

                if flag1:
                    heights[lowIndex] += 1


                if not flag1:
                    j = K
                    flag2 = False
                    lowPoint = max(heights)
                    while j < len(heights)-1:
                        if heights[j + 1] > heights[j]:
                            break

                        if heights[j + 1] < heights[j]:
                            if heights[j + 1] < lowPoint:
                                lowPoint = heights[j + 1]
                                lowIndex = j + 1
                            flag2 = True
                        j += 1

                    if flag2:
                        heights[lowIndex] += 1

                if not flag1 and not flag2:
                    heights[K] += 1

            i += 1

        return heights

s = Solution()
heights = [14,9,10,9,7,9,7,5,3,2]
V = 7
K = 9
print s.pourWater(heights, V, K)
Expected = [4,4,4,4,3,3,3,3,3,4,3,2,1]
