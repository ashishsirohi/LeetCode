class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.right = None
        self.left = None

class heap(object):
    def __init__(self, nums):
        self.nums = nums
        self.sortResult = []

    def buildTree(self, index):
        root = TreeNode(self.nums[index])
        left = 2 * index + 1
        right = 2 * index + 2
        if left < len(self.nums):
            root.left = self.buildTree(left)
        if right < len(self.nums):
            root.right = self.buildTree(right)
        return root


    def buildMaxHeap(self):
        for i in range(len(self.nums)/2, -1, -1):
            self.maxHeapify(i)

        return self.nums

    def maxHeapify(self, index):
        left = 2 * index + 1
        right = 2 * index + 2
        largest = index
        if left < len(self.nums) and self.nums[left] > self.nums[largest]:
            largest = left
        if right < len(self.nums) and self.nums[right] > self.nums[largest]:
            largest = right
        if largest != index:
            self.nums[index], self.nums[largest] = self.nums[largest], self.nums[index]
            self.maxHeapify(largest)

    def heapSortMaxHeap(self):
        if self.nums:
            self.sortResult.append(self.nums[0])
            self.nums[0], self.nums[-1] = self.nums[-1], self.nums[0]
            self.nums = self.nums[:-1]
            self.maxHeapify(0)
            self.heapSortMaxHeap()

        return self.sortResult

    def insertMaxHeap(self, val, index, flag):
        if index > len(self.nums) - 1:
            return "Invalid index"
        currParent = (index)/2
        if flag:
            self.nums.append(val)
        while currParent >= 0:
            if val < self.nums[currParent]:
                break
            self.maxHeapify(currParent)
            if currParent == 0:
                break
            currParent = currParent/2

        return self.nums


    def deleteMaxHeap(self, index):
        if index > len(self.nums) - 1:
            return "Invalid index"
        val = self.nums[index]
        currParent = (index)/2
        self.nums[index], self.nums[-1] = self.nums[-1], self.nums[index]
        self.nums = self.nums[:-1]
        self.maxHeapify(currParent)
        self.insertMaxHeap(val, index, False)

        return self.nums

    def buildMinHeap(self):
        for i in range(len(self.nums)/2, -1, -1):
            self.minHeapify(i)

        return self.nums

    def minHeapify(self, index):
        left = 2 * index + 1
        right = 2 * index + 2
        smallest = index
        if left < len(self.nums) and self.nums[left] < self.nums[smallest]:
            smallest = left
        if right < len(self.nums) and self.nums[right] < self.nums[smallest]:
            smallest = right
        if smallest != index:
            self.nums[index], self.nums[smallest] = self.nums[smallest], self.nums[index]
            self.minHeapify(smallest)

    def heapSortMinHeap(self):
        if self.nums:
            self.sortResult.append(self.nums[0])
            self.nums[0], self.nums[-1] = self.nums[-1], self.nums[0]
            self.nums = self.nums[:-1]
            self.minHeapify(0)
            self.heapSortMinHeap()

        return self.sortResult

    def insertMinHeap(self, val, index, flag):
        if index > len(self.nums) - 1:
            return "Invalid index"
        currParent = (index)/2
        if flag:
            self.nums.append(val)
        while currParent >= 0:
            if val > self.nums[currParent]:
                break
            self.minHeapify(currParent)
            if currParent == 0:
                break
            currParent = currParent / 2

        return self.nums

    def deleteMinHeap(self, index):
        if index > len(self.nums) - 1:
            return "Invalid index"
        val = self.nums[index]
        currParent = (index)/2
        self.nums[index], self.nums[-1] = self.nums[-1], self.nums[index]
        self.nums = self.nums[:-1]
        self.minHeapify(currParent)
        self.insertMinHeap(val, index, False)

        return self.nums


nums = [16,22,24,4,12,8,3,7,2,1,20]
h = heap(nums)

print "Tree Represention"
print h.buildTree(0)

print "Input"
print nums
print "Max Heap"
print h.buildMaxHeap()
print "Inserting"
print h.insertMaxHeap(50, len(h.nums)-1, True)
print "Deleting"
print h.deleteMaxHeap(11)
print "Sorting"
print h.heapSortMaxHeap()

print "============="
nums2 = [16,22,24,4,12,8,3,7,2,1,20]
print "Input"
print nums2
print "Min Heap"
h = heap(nums2)
print h.buildMinHeap()
print "Inserting"
print h.insertMinHeap(5, len(h.nums)-1, True)
print "Deleting"
print h.deleteMinHeap(0)
print "Sorting"
print h.heapSortMinHeap()

