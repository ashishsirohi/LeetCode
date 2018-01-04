class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        if "." not in input:
            return 0
        import Queue
        myQueue = Queue.Queue()
        tmp = input.split("\n")
        myQueue.put((tmp[0], 1, tmp[0]))
        result = []
        while not myQueue.empty():
            currDir, i, last = myQueue.get()

            if "." in currDir:
                result.append(currDir)

            c = tmp.index(last) + 1
            while c < len(tmp):
                if "\t" in tmp[c]:
                    tc = tmp[c].count("\t")
                    if tc < i:
                        break
                    if tc == i:
                        tmpDir = tmp[c].replace("\t", "", i)
                        if "\t" not in tmpDir and "." not in currDir:
                            myQueue.put((currDir +"/"+ tmpDir, i+1, tmp[c]))
                else:
                    myQueue.put((tmp[c], i, tmp[c]))
                    break
                c += 1
        print result
        return max([len(x) for x in result])


s = Solution()
input = "rzzmf\nv\n\tix\n\t\tiklav\n\t\t\ttqse\n\t\t\t\ttppzf\n\t\t\t\t\tzav\n\t\t\t\t\t\tkktei\n\t\t\t\t\t\t\thhmav\n\t\t\t\t\t\t\t\tbzvwf.txt"
print s.lengthLongestPath(input)