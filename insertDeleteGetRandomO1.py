class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.myDict = {}
        self.myList = []
        

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.myDict:
            self.myList.append(val)
            self.myDict[val] = len(self.myList) - 1
            return True
        else:
            return False
        

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.myDict:
            index = self.myDict[val]
            last = self.myList[-1]
            self.myList[index], self.myDict[last] = last, index
            self.myList.pop(); self.myDict.pop(val, 0)
            return True
        else:
            return False
        

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return self.myList[random.randint(0, len(self.myList) - 1)]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
