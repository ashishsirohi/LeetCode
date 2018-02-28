def findpath(n, src, dest, graph):
    mystack = []
    mystack.append((src, [src], 0))
    while mystack:
        curr, path, count = mystack.pop()

        if curr == dest:
            return path

        if count > n:
            continue

        for item in graph[curr]:
            if count + 1 <= n:
                newpath = list(path)
                newpath.append(item)
                mystack.append((item, newpath, count + 1))

    return []


#graph = processInput(grid)
res = findpath(3, "PHX", "SEA", {'PHX': ['SEA', 'ABC'], 'RAR': ['PHX', 'SEA'], 'ABC': ['RAR']})

if res:
    print res[0]
else:
    print "NOT POSSIBLE"