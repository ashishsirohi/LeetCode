import collections
class TrieNode(object):
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.isEnd = False


class WordDictionary(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        curr = self.root
        for w in word:
            curr = curr.children[w]

        curr.isEnd = True

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        curr = self.root

        def backtrack(word):
            mystack = []
            state = (curr, word)
            mystack.append(state)

            res = []
            while mystack:
                w, remaining = mystack.pop()

                if not remaining:
                    res.append(w.isEnd)
                    continue

                if remaining[0] == ".":
                    for key, value in w.children.iteritems():
                        mystack.append((value, remaining[1:]))
                else:
                    for key, value in w.children.iteritems():
                        if key == remaining[0]:
                            mystack.append((value, remaining[1:]))
                        else:
                            continue

            if True in res:
                return True

            return False

        if "." in word:
            return backtrack(word)

        for w in word:
            curr = curr.children[w]
            if curr is None:
                return False
        return curr.isEnd





# Your WordDictionary object will be instantiated and called as such:
obj = WordDictionary()
obj.addWord("ran")
obj.addWord("ran")
obj.addWord("runner")
obj.addWord("runs")
obj.addWord("add")
obj.addWord("adds")
obj.addWord("adder")
obj.addWord("addee")
param_2 = obj.search("r.n")
print param_2