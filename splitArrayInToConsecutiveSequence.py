class Solution(object):
    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        import heapq

        seqs = {num: [] for num in nums}
        for num in nums:
            shortest_seq = 0
            if num - 1 in seqs and len(seqs[num - 1]):
                shortest_seq = heapq.heappop(seqs[num - 1])
            heapq.heappush(seqs[num], shortest_seq + 1)
        return len([None for seq_lengths in seqs.values() if len(seq_lengths) and seq_lengths[0] < 3]) == 0

n = [1,2,3,3,4,4,5,5]
print Solution().isPossible(n)