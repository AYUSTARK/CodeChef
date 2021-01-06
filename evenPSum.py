if __name__ == '__main__':
    T = int(input())
    for i in range(1, T+1):
        A, B = list(map(int, input().split()))
        '''for j in range(1, a+1):
            for k in range(1, B+1):
                if (j + k) % 2 == 0:
                    count = count + 1'''
        count = ((A // 2) * (B // 2)) + (A - (A // 2)) * (B - (B // 2))
        print(count)
