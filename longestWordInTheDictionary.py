import collections


class TrieNode(object):
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.isEnd = False


class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        result = []
        def dfs(root, path):
            mystack = []
            mystack.append((root, path))

            while mystack:
                curr, currp = mystack.pop()

                if not curr.children:
                    result.append(currp)
                    continue

                for key, value in curr.children.iteritems():
                    if value.isEnd == True:
                        mystack.append((value, currp + key))
                    else:
                        result.append(currp)

            return result



        root = TrieNode()
        for word in words:
            curr = root
            for w in word:
                curr = curr.children[w]
            curr.isEnd = True


        res = []
        for key, value in root.children.iteritems():
            tmp = dfs(value, key)
            res.append(tmp)

        finalres= []
        maxVal = 0
        for items in res:
            for item in items:
                if len(item) > maxVal:
                    maxVal = len(item)

        for items in res:
            for item in items:
                if len(item) == maxVal:
                    finalres.append(item)

        return sorted(finalres)[0]




words = ["m","mo","moc","moch","mocha","l","la","lat","latt","latte","c","ca","cat"]
print Solution().longestWord(words)