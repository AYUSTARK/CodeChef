if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        arr = list(map(int, input().split()))
        counter = 0
        flag = 0
        arr.sort()
        for i in range(n):
            if arr[i] > i+1:
                print("Second")
                flag=1
                break
            else:
                counter += i + 1 - arr[i]
        if flag == 0:
            if counter & 1:
                print("First")
            else:
                print("Second")
