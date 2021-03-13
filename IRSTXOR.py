if __name__ == '__main__':
    for _ in range(int(input())):
        c = int(input())
        sum, d = 0, 1
        while c >= sum:
            sum = pow(2, d)
            d += 1
        j = pow(2, d - 2)
        temp = sum - c
        maxValue = (j - 1) * ((j - 1) + temp)
        print(int(maxValue))
