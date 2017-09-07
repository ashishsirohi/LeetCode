def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """        
        from struct import pack
        s = str(x)
        ll = []
        ll1 = []
        for x in s:
            ll.append(x)
        
        if ll[0] == "-":
            str1 = "-"
            for x in range(len(ll) - 1):
                str1 = str1 + ll[len(ll) - x - 1]
            if abs(int(str1)) > 2**31:
                return 0
            else:
                return int(str1)
        else:
            str1 = ""
            for x in range(len(ll)):
                str1 = str1 + ll[len(ll) - x - 1]
            if abs(int(str1)) > 2**31:
                return 0
            else:
                return int(str1)