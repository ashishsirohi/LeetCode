def maxArea(height):
    """
    :type height: List[int]
    :rtype: int
    """
    maxAr = 0
    x = 0
    while x < len(height):
        y = x + 1
        while y < len(height):
            area = 0
            if height[x] < height[y]:
                area = (y - x) * (height[x])
            else:
                area = (y - x) * (height[y])

            if area > maxAr:
                maxAr = area

            y = y + 1
        x = x + 1

    return maxAr

print maxArea([1,2,4,3])