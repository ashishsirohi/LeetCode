class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        sortrev = sorted(nums, reverse=True)
        if sortrev == nums:
            return len(nums)

        mydict = {}

        for i in range(len(nums)):
            currSet = set()
            for j in range(i - 1, -1, -1):
                if nums[j] in currSet:
                    continue
                currSet.add(nums[j])
                if nums[j] < nums[i]:
                    try:
                        curr = mydict[nums[i]][0]
                        if curr == mydict[nums[j]][0] + 1:
                            mydict[nums[i]] = (curr, mydict[nums[i]][1] + mydict[nums[j]][1])
                        elif curr < mydict[nums[j]][0] + 1:
                            mydict[nums[i]] = (mydict[nums[j]][0] + 1, mydict[nums[j]][1])
                    except KeyError:
                        mydict[nums[i]] = (mydict[nums[j]][0] + 1, mydict[nums[j]][1])

            try:
                mydict[nums[i]]
            except KeyError:
                mydict[nums[i]] = (1, 1)

        sorteddict = sorted(mydict.iteritems(), key=lambda x: x[1][0], reverse=True)

        print sorteddict

        return sorteddict[0][1][1]

nums = [1,2,4,3,5,4,7,2]
print Solution().findNumberOfLIS(nums)