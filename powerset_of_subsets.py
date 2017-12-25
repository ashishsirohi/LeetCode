def subsets(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    result = []
    result.append([])

    for i in range(len(nums)):
        path = [nums[i]]
        state = (i, path)
        myStack = [state]
        while len(myStack) > 0:
            currIndex, currPath = myStack.pop()
            result.append(currPath)

            for j in range(currIndex+1, len(nums)):
                childPath = list(currPath)
                childPath.append(nums[j])
                myStack.append((j, childPath))

    return result





nums = [1, 2, 3]
print subsets(nums)