for _ in range(int(input())):
    n = int(input())
    ants = []
    dist = {}
    ans = 0
    for i in range(n):
        mi = list(map(int, input().split()))
        m = mi.pop(0)
        pos, neg = [], []

        for j in range(m):
            d = mi[j]
            if abs(d) in dist:
                dist[abs(d)] += 1
            else:
                dist[abs(d)] = 1

            if d > 0:
                pos.append(d)
            else:
                neg.append(d)

        pos.sort(reverse=True)
        neg.sort()
        ants.append([pos, neg])

    for i in dist:
        if dist[i] > 1:
            ans += 1

    for i in range(n):
        pos, neg = ants[i]

        while len(pos) > 0 and len(neg) > 0:
            if pos[-1] < abs(neg[-1]):
                a = pos.pop()
                if dist[a] > 1:
                    ans += len(pos)
                else:
                    ans += len(neg)
            else:
                a = neg.pop()
                if dist[abs(a)] > 1:
                    ans += len(neg)
                else:
                    ans += len(pos)

        while len(pos) > 0:
            a = pos.pop()
            if dist[a] > 1:
                ans += len(pos)

        while len(neg) > 0:
            a = neg.pop()
            if dist[abs(a)] > 1:
                ans += len(neg)

    print(ans)
