if __name__ == '__main__':
    for _ in range(int(input())):
        n, k = list(map(int, input().split()))
        h = list(map(int, input().split()))
        h.sort(reverse=True)
        count = 0
        b = 0
        s = 0
        a = 0
        if sum(h) < (2 * k):
            print(-1)
            continue
        while s < len(h):
            count += 1
            a += h[s]
            if a >= k:
                a = 0
                b += 1
                s += 1
                break
            s += 1
        if b == 1:
            while s < len(h):
                count += 1
                a += h[s]
                if a >= k:
                    b += 1
                    break
                s += 1
        if b == 2:
            print(count)
        else:
            print(-1)
