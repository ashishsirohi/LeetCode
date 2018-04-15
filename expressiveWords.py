class Solution(object):
    def expressiveWords(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        if not S:
            return 0

        mydict = {}
        count = 1
        for i in range(1, len(S)):
            if S[i] == S[i - 1]:
                count += 1
            else:
                count = 1

            if count >= 3:
                mydict[(S[i], i - count + 1)] = count

        if len(mydict) == 0:
            return 0

        print mydict
        res = 0
        for word in words:
            tmp = ""
            i = 0
            j = 0
            while i < len(word):
                if word[i] == S[j]:
                    try:
                        count = mydict[(word[i], j)]
                        print count
                        tmp += word[i] * count
                        while i < len(word) and word[i] == S[j]:
                            i += 1
                        j += count
                        print i, j
                        print tmp
                    except KeyError:
                        tmp += word[i]
                        i += 1
                        j += 1
                else:
                    break

            if tmp == S:
                res += 1

        return res


s = "heeellooo"
l = ["heello", "hi", "helo"]
print Solution().expressiveWords(s, l)