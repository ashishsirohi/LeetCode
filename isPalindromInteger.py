def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        ll = []
        while x > 0:
            ll.append(x%10)
            x = x/10
        
        ll1 = ll[::-1]
        if ll1 == ll:
            return True
        else:
            return False