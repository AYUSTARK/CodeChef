if __name__ == '__main__':
    for t in range(int(input())):
        N, K, x, y = map(int, input().split())
        if x == y:
            print(N, N)
        else:
            poc = []
            if x < y:
                poc = [[x + N - y, N], [N, N - y + x], [y - x, 0], [0, y - x]]
            else:
                poc = [[N, y + N - x], [y + N - x, N], [0, x - y], [x - y, 0]]
            # print(poc)
            e = poc[(K - 1) % 4]
            print(e[0], e[1])
