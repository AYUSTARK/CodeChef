if __name__ == '__main__':
    for i in range(int(input())):
        p = input()
        ph = 10 * int(p[0]) + int(p[1])  # Extracting Hour
        if p[6] == 'P' and ph != 12:
            ph += 12
        if p[6] == 'A' and ph == 12:
            ph = 0
        pm = (10 * int(p[3]) + int(p[4])) + 60 * ph  # Extracting minute and converting hour in minute
        # print(pm)
        for _ in range(int(input())):
            t = input()
            sh = 10 * int(t[0]) + int(t[1])
            if t[6] == 'P' and sh != 12:
                sh += 12
            if t[6] == 'A' and sh == 12:
                sh = 0
            sm = (10 * int(t[3]) + int(t[4])) + 60 * sh  # sm is starting friend free time in minutes
            eh = 10 * int(t[9]) + int(t[10])
            if t[15] == 'P' and eh != 12:
                eh += 12
            if t[15] == 'A' and eh == 12:
                eh = 0
            em = (10 * int(t[12]) + int(t[13])) + 60 * eh  # em is ending friend free time in minutes
            # print(sm, ",", em)
            if sm <= pm <= em:
                print(1, end="")
            else:
                print(0, end="")
        print()
