def jump(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    import math
    if nums[1:] == nums[:-1]:
        return math.floor((len(nums)) / nums[0])

    goal = nums[len(nums) - 1]
    print goal
    node = (nums[0], 0, [])
    toVisit = []
    toVisit.append(node)

    while len(toVisit) > 0:
        currState, index, path = toVisit.pop(0)
        if currState == goal and index == len(nums) - 1:
            return len(path)

        successors = getSucc(currState, index, path, nums)

        print successors

        for child in successors:
            if child[0] == goal and child[1] == len(nums) - 1:
                return len(child[2])
            toVisit.append(child)


def getSucc(node, index, path, nums):
    succ = []
    farthestIndex = 0
    currPath = list(path)
    nextNode = 0
    nextIndex = 0
    currPath.append(node)
    tmp = (nextNode, nextIndex, currPath)
    succ.append(tmp)
    for x in range(node):
        if index + x + 1 < len(nums):
            currPath = list(path)
            nextNode = nums[index + x + 1]
            nextIndex = index + x + 1
            currPath.append(node)
            tmp = (nextNode, nextIndex, currPath)
            if nextIndex + nextNode >= farthestIndex:
                farthestIndex = nextIndex + nextNode
                succ.pop(0)
                succ.append(tmp)

    return succ

print jump([2,2,2,2,2,2,2,2,2])