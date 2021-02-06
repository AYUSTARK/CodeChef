if __name__ == '__main__':
    for _ in range(int(input())):
        x, y = list(map(int, input().split()))
        if x <= y:
            print("Chef")
        else:
            print("Divyam")
