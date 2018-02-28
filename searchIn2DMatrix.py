import numpy as np

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        return self.binarySearch2D(matrix, 0, len(matrix) - 1, 0, len(matrix[0]) - 1, target)

    def binarySearch(self, nums, left, right, target):
        if left > right:
            return False

        mid = (left + right) // 2

        if nums[mid] == target:
            return True

        elif nums[mid] < target:
            return self.binarySearch(nums, mid + 1, right, target)
        else:
            return self.binarySearch(nums, left, mid - 1, target)

    def binarySearch2D(self, matrix, t, b, l, r, target):
        mid_x = (t + b) / 2
        mid_y = (l + r) / 2

        if matrix[mid_x][mid_y] == target:
            return True

        if matrix[mid_x][mid_y] > target:
            nums = matrix[mid_x]
            res = self.binarySearch(nums, 0, len(nums) - 1, target)
            if not res:
                tmp = np.array(matrix)
                nums = list(tmp[:,mid_y])
                res2 = self.binarySearch(nums, 0, len(nums) - 1, target)
                if not res2:
                    return self.binarySearch2D(matrix, t, mid_x - 1, l, mid_y - 1, target)
                else:
                    return res2

            else:
                return res


        else:
            nums = matrix[mid_x]
            res = self.binarySearch(nums, 0, r, target)
            if not res:
                tmp = np.array(matrix)
                nums = list(tmp[:, mid_y])
                res2 = self.binarySearch(nums, 0, b, target)
                if not res2:
                    return self.binarySearch2D(matrix, mid_x + 1, b, mid_y + 1, r, target)
                else:
                    return res2


            else:
                return res



m = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
s = Solution()
print s.searchMatrix(m, 15)