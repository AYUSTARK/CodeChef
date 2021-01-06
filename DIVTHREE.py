def add(p):
    d = 0
    for e in p:
        d += e
    return d


if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        N, K, D = list(map(int, input().split()))
        a = list(map(int, input().split()))
        s = add(a)
        if s // K <= D:
            print(s // K)
        else:
            print(D)
