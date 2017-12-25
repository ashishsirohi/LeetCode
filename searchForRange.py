def searchRange(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    if target not in nums:
        return [-1, -1]
    result = []
    j = len(nums)
    i = 0
    while (1):
        mid = (i + j) / 2
        print mid
        if nums[mid] == target:
            tmpi = mid
            while (tmpi >= 0 and nums[tmpi] == target):
                tmpi -= 1
            result.append(tmpi + 1)

            tmpi = mid
            while (tmpi< len(nums) and nums[tmpi] == target):
                tmpi += 1
            result.append(tmpi - 1)

            return result

        else:
            if nums[mid] > target:
                j = mid - 1
                i = i
            else:
                i = mid + 1
                j = j

    print result
    return result


#nums = [5,7,8,8,8,8,8,8,8,8,8,8,8,10]
#t = 2
nums = [1]
t = 1

print searchRange(nums, t)