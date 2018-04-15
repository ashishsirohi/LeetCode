class Solution(object):
    def minSwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        self.len = len(A)
        self.swaps = []
        self.recursive(A, B, 0, 0)
        self.dict = {}
        for i in range(len(A)):
            self.dict[i] = float('inf')
        print self.swaps
        return min(self.swaps)

    def recursive(self, A, B, i, swaps):

        try:
            return self.dict[i]
        except KeyError:
            pass

        if len(set(A)) == len(A) and sorted(A) == A and len(set(B)) == len(B) and sorted(B) == B:
            self.swaps.append(swaps)
            return

        if i >= self.len:
            return

        if A[i] == B[i]:
            res = self.recursive(A, B, i + 1, swaps)
            try:
                self.dict[i] = min(self.dict[i], res)
            except:
                self.dict[i] = res
        else:
            self.recursive(A, B, i + 1, swaps)
            A[i], B[i] = B[i], A[i]
            print A
            print B
            self.recursive(A, B, i + 1, swaps + 1)

A = [3,3,8,9,10]
B = [1,7,4,6,8]

print Solution().minSwap(A, B)