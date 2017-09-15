def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    i = 0
    res = []
    while i < len(nums) - 2:
        j = i + 1
        while j < len(nums) - 1:
            k = j + 1
            while k < len(nums):
                ll = []
                if nums[i] + nums[j] + nums[k] == 0:
                    ll.append(nums[i])
                    ll.append(nums[j])
                    ll.append(nums[k])
                    ll.sort()
                    if ll not in res:
                        res.append(ll)
                k += 1
            j += 1
        i += 1
    return res

print threeSum([-1,0,1,2,-1,-4])