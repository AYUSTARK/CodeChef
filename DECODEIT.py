if __name__ == '__main__':
    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']
    for _ in range(int(input())):
        a = 0
        n = int(input())
        s = input()
        i = -1
        for _ in range(n // 4):
            high = 16
            low = 0
            for j in range(4):
                i += 1
                if s[i] == '0':
                    high = (high+low)//2
                elif s[i] == '1':
                    low = low + (high-low)//2
            print(alpha[low], end='')
        print()
