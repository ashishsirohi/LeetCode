# Can use only digits available. no repition of digits allowed

def nextClosestTime(time):
    digits = [int(y) for x in time.split(':') for y in x]
    h, m = time.split(':')
    while True:
        currDigit = list(digits)
        h, m = (str(int(h) + 1), '00') if int(m) == 59 else (h, str(int(m) + 1))
        h = '00' if int(h) > 23 else h
        h = '0' + h if len(h) == 1 else h
        m = '0' + m if len(m) == 1 else m
        for x in h + m:
            if int(x) in currDigit:
                currDigit.remove(int(x))
        if len(currDigit) == 0:
            return h + ':' + m

print nextClosestTime("04:55")