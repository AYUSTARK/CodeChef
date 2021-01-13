if __name__ == '__main__':
    d1, v1, d2, v2, p = list(map(int, input().split()))
    days = 0
    while p > 0:
        days += 1
        if d1 <= days:
            p -= v1
        if d2 <= days:
            p -= v2
    print(days)
