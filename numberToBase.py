def answer(n, b):
    # your code here
    numList = [n]
    while True:
        asc = ''.join(sorted(str(n)))
        desc = ''.join(sorted(str(n), reverse=True))
        
        y = int(asc, b)
        x = int(desc, b)
        
        z = x-y
        
        z_baseb = numberToBase(z, b)
        
        len_z = len(z_baseb)
        len_n = len(str(n))
        if len_z < len_n:
            z_baseb = "0"*(len_n-len_z) + str(z_baseb)

        if z_baseb in numList:
            break
        else:
            numList.append(z_baseb)
            n =  z_baseb

    return len(numList) - numList.index(z_baseb)
    
        
  
def numberToBase(n, b):
    if n == 0:
        return str(0)
    digits = []
    while n:
        digits.append(str(n % b))
        n /= b
    digits.reverse()
    rebasedVal = ''.join(digits)
    return rebasedVal

n = "999"
b = 10
print answer(n,b)
#print numberToBase(8991, 10)

