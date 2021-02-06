if __name__ == '__main__':
    for i in range(int(input())):
        p = input()
        ph = 10 * int(p[0]) + int(p[1])
        pm = 10 * int(p[3]) + int(p[4])
        if p[6] == 'P' and ph != 12:
            ph += 12
        if p[6] == 'A' and ph == 12:
            ph = 0
        # print(ph, ":", pm)
        for _ in range(int(input())):
            t = input()
            sh = 10 * int(t[0]) + int(t[1])
            sm = 10 * int(t[3]) + int(t[4])
            if t[6] == 'P' and sh != 12:
                sh += 12
            if t[6] == 'A' and sh == 12:
                sh = 0
            eh = 10 * int(t[9]) + int(t[10])
            em = 10 * int(t[12]) + int(t[13])
            if t[15] == 'P' and eh != 12:
                eh += 12
            if t[15] == 'A' and eh == 12:
                eh = 0
            # print(sh, ":", sm, ",", eh, ":", em)
            if sh < ph < eh:
                print(1, end="")
            elif ph == sh and pm >= sm:
                print(1, end="")
            elif ph == eh and pm <= em:
                print(1, end="")
            else:
                print(0, end="")
        print()
