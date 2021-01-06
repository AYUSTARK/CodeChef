if __name__ == '__main__':
    for _ in range(int(input())):
        m, n = list(map(int, input().split()))
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        count = 0
        if sum(a) > sum(b):
            print(count)
            exit(0)
        else:
            for i in a if m < n else b:
                a.sort()
                b.sort()
                temp = a[0]
                a[0] = b[-1]
                b[-1] = temp
                count += 1
                if sum(a) > sum(b):
                    break
        if sum(a) > sum(b):
            print(count)
        else:
            print(-1)
