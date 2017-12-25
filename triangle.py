def getTriangleType(abc):
    print abc
    output = []
    for t in abc:
        t_tmp = t.split(" ")
        side1 = int(t_tmp[0])
        side2 = int(t_tmp[1])
        side3 = int(t_tmp[2])
        if (side1 + side2 <= side3) or (side2 + side3 <= side1) or (side1 + side3 <= side2):
            output.append("None of these")
        else:
            if side1 == side2 and side1 == side3:
                output.append("Equilateral")
            elif side1 == side2 or side2 == side3 or side3 == side1:
                output.append("Isosceles")
            else:
                output.append("None of these")

    return output


print getTriangleType(["30 30 35"])