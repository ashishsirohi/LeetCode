class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        max_len = 0
        ll = []
        x = 0

        while x < len(s):
            if s[x] not in ll:
                ll.append(s[x])
                x = x + 1
            else:
                if len(ll) >= max_len:
                    max_len = len(ll)
                i = ll.index(s[x])
                del ll[0:i + 1]
                ll.append(s[x])
                x = x + 1

        if len(ll) > max_len:
            max_len = len(ll)

        return max_len

    def is_palindrom(s):
        l = len(s)
        if l%2 == 0:
            x=0
            count = 0
            while x < l/2:
                if s[x] == s[l-x-1]:
                    count += 1
                x = x + 1

            if count == l/2:
                return True

        else:
            x = 0
            count = 0
            while x < (l-1) / 2:
                if s[x] == s[l - x - 1]:
                    count += 1
                x = x+1

            if count == (l-1) / 2:
                return True

        return False

    print is_palindrom("abcbba")