if __name__ == '__main__':
    for _ in range(int(input())):
        n, k = list(map(int, input().split()))
        a = list(map(int, input().split()))
        add = sum(a)
        if add % k == 0:
            print(0)
        else:
            a.insert(0, (add % k) - a.pop())

        print(a, sum(a))
