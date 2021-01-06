from math import ceil

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        N, D = list(map(int, input().split()))
        A = list(map(int, input().split()))
        risk = 0
        nRisk = 0
        for j in A:
            if j <= 9 or j >= 80:
                risk += 1
            else:
                nRisk += 1
        print(ceil(risk / D) + ceil(nRisk / D))
