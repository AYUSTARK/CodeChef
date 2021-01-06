if __name__ == '__main__':
    d1 = int(input())
    v1 = int(input())
    d2 = int(input())
    v2 = int(input())
    p = int(input())
    if d1 < d2:
        result = ((p - ((d2 - d1) * v1)) / (v1 + v2)) + d2 - 1
        resultAbs = ((p - ((d2 - d1) * v1)) // (v1 + v2)) + d2 - 1
    elif d1 == d2:
        result = p / (v1 + v2) + d1 - 1
        resultAbs = p // (v1 + v2) + d1 - 1
    else:
        result = ((p - ((d1 - d2) * v2)) / (v1 + v2)) + d1 - 1
        resultAbs = ((p - ((d1 - d2) * v2)) // (v1 + v2)) + d1 - 1
    if result > resultAbs:
        print(resultAbs + 1)
    else:
        print(resultAbs)
