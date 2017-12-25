import re


def firstOccurrence(s, x):
    if len(s) == 0 and len(x) == 0:
        return -1

    if len(x) > 1 and x[0] == "*" and len(s) == 0:
        return -1

    tmp_str = x.split("*")
    if len(tmp_str) == 1:
        occur = [m.start() for m in re.finditer(tmp_str[0], s)]

        if len(occur) == 0:
            return -1
        else:
            if occur[0] == 0:
                return 0
            else:
                return occur[0]
    else:
        occ_s1 = [m.start for m in re.finditer(tmp_str[0], s)]
        occ_s2 = [m.start for m in re.finditer(tmp_str[1], s)]

        for a in occ_s1:
            tmp = a + len(tmp_str[0])
            if tmp in occ_S2:
                return a
        return -1

    return -1


print firstOccurrence("juliasamanthantjulia", "ant")