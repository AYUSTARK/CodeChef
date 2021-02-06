import sys

if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        a = list(map(int, input().split()))
        ma = max(a)
        mi = min(a)
        print((ma-mi)*2)
