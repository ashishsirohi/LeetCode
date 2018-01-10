class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        if not preorder:
            return False
        preorder = preorder.split(",")
        myStack = [preorder[0]]

        for i in range(1, len(preorder)):
            myStack.append(preorder[i])
            while len(myStack) > 2 and myStack[-1] == "#" and myStack[-2] == "#" and myStack[-3] != "#":
                myStack.pop()
                myStack.pop()
                myStack.pop()
                myStack.append("#")
        # print myStack
        if len(myStack) == 1 and myStack[-1] == "#":
            return True
        else:
            return False

