def twoSum(arr, target):
    tmpDict = {}
    for x in range(len(arr)):
        tmpDict[arr[x]] = x
    
    for x in range(len(arr)):
        if target-arr[x] in tmpDict and tmpDict[target-arr[x]] != x:
            return [x, tmpDict[target-arr[x]]]

        
if __name__=="__main__":
    ll = [2, 7, 11, 15]
    t = 18
    ll1 = [1,3,3]
    t1 = 6
    result = twoSum(ll1, t1)
    print (result)