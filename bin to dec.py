def bintodec(num):
    res = 0
    idx = 0
    while num > 0:
        dig = num % 10
        res += (2 ** idx) * dig
        idx += 1
        num = num // 10
    print(res)
bintodec(111111)