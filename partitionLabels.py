class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        result = []
        pos = 0
        while pos < len(S):
            currSet = set()
            lastIndex = 0
            currList = [S[pos]]
            for item in currList:
                if item not in currSet:
                    currSet.add(item)
                    index = S.rfind(item)
                    tmpSet = set(list(S[pos:index]))
                    currList += list(tmpSet)
                    if index > lastIndex:
                        lastIndex = index
            result.append(lastIndex - pos + 1)
            pos = lastIndex + 1
            currSet.clear()

        return result

S = "ababcbacadefegdehijhklij"
print Solution().partitionLabels(S)