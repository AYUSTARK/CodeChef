def omlette(n1, e1, h1, a1, b1, c1, req1, price1, itemsPrice1, items1):
    if e1 // 2 >= req1:
        price1 += a1 * req1
        return price1
    else:
        price1 += a1 * (e1 // 2)
        req1 -= e1 // 2
        e1 -= (e1 // 2) * 2
        if b1 == min(itemsPrice1) and items.__contains__('b'):
            itemsPrice1.discard(b1)
            items.discard('b')
            price1 = milkshake(n1, e1, h1, a1, b1, c1, req1, price1, itemsPrice1, items1)
            return price1
        elif c1 == min(itemsPrice1) and items.__contains__('c'):
            itemsPrice1.discard(c1)
            items.discard('c')
            price1 = cake(n1, e1, h1, a1, b1, c1, req1, price1, itemsPrice1, items1)
            return price1


def milkshake(n1, e1, h1, a1, b1, c1, req1, price1, itemsPrice1, items1):
    if h1 // 3 >= req1:
        price1 += b1 * req1
        return price1
    else:
        price1 += b1 * (h1 // 3)
        req1 -= h1 // 3
        h1 -= (h1 // 3) * 3
        if a1 == min(itemsPrice1) and items.__contains__('a'):
            itemsPrice1.discard(a1)
            items.discard('a')
            price1 = omlette(n1, e1, h1, a1, b1, c1, req1, price1, itemsPrice1, items1)
            return price1
        elif c1 == min(itemsPrice1) and items.__contains__('c'):
            itemsPrice1.discard(c1)
            items.discard('c')
            price1 = cake(n1, e1, h1, a1, b1, c1, req1, price1, itemsPrice1, items1)
            return price1


def cake(n1, e1, h1, a1, b1, c1, req1, price1, itemsPrice1, items1):
    if min(e1, h1) >= req1:
        price1 += c1 * req1
        return price1
    else:
        price1 += c1 * min(e1, h1)
        req1 -= min(e1, h1)
        if e1 == min(e1, h1):
            e1 = 0
            h1 -= e1
        elif h1 == min(e1, h1):
            h1 = 0
            e1 -= h1
        if a1 == min(itemsPrice1) and items.__contains__('a'):
            itemsPrice1.discard(a1)
            items.discard('a')
            price1 = omlette(n1, e1, h1, a1, b1, c1, req1, price1, itemsPrice1, items1)
            return price1
        elif b1 == min(itemsPrice1) and items.__contains__('b'):
            itemsPrice1.discard(b1)
            items.discard('b')
            price1 = cake(n1, e1, h1, a1, b1, c1, req1, price1, itemsPrice1, items1)
            return price1


for _ in range(int(input())):
    o = 0
    n, e, h, a, b, c = list(map(int, input().strip().split()))
    itemsPrice = {a, b, c}
    items = {'a', 'b', 'c'}
    if e > h:
        o = h + (e - h) // 2
    else:
        o = e + (h - e) // 3
    if o < n:
        print("-1")
    else:
        # print(int(o))
        req = n
        price = 0
        mini = min(itemsPrice)
        if a == mini and items.__contains__('a'):
            itemsPrice.discard(a)
            items.discard('a')
            price = omlette(n, e, h, a, b, c, req, price, itemsPrice, items)
        elif b == mini and items.__contains__('b'):
            itemsPrice.discard(b)
            items.discard('b')
            price = milkshake(n, e, h, a, b, c, req, price, itemsPrice, items)
        elif c == mini and items.__contains__('c'):
            itemsPrice.discard(c)
            items.discard('c')
            price = cake(n, e, h, a, b, c, req, price, itemsPrice, items)
        print(price)
