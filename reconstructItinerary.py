class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        mygraph = {}
        for s, d in tickets:
            try:
                mygraph[s].append(d)
                mygraph[s].sort()
            except:
                mygraph[s] = [d]

        result = []
        result.append("JFK")
        mystack = []
        mystack.append(("JFK", ["JFK"], mygraph))
        while mystack:
            curr, path, myg = mystack.pop()
            #print curr, path, myg

            if len(myg) == 0:
                return path

            try:
                for i in range(len(myg[curr])):
                    newmyg = dict(myg)
                    if len(newmyg[curr]) == 1:
                        newmyg.pop(curr)
                    else:
                        tmp = list(newmyg[curr])
                        tmp.pop(i)
                        newmyg[curr] = tmp
                    newpath = list(path)
                    newpath.append(myg[curr][i])
                    mystack.append((myg[curr][i], newpath, newmyg))
            except:
                continue

        return result

it = [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]

print Solution().findItinerary(it)