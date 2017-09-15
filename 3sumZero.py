def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    """i = 0
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
return res"""

    i = 0
    res = []
    nums.sort()
    for i in range(len(nums) - 2):
        j = i + 1
        if nums[i] + nums[j] + nums[j + 1] > 0:
            return res
        k = len(nums) - 1
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        while j < k:
            if j > i + 1 and nums[j] == nums[j - 1]:
                j += 1
                continue
            if nums[i] + nums[j] + nums[k] == 0:
                res.append([nums[i], nums[j], nums[k]])
                j = j + 1
            elif nums[i] + nums[j] + nums[k] > 0:
                k = k - 1
            else:
                j = j + 1
        i += 1
    return res

print threeSum([-1,0,1,2,-1,-4])