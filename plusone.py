def plusone(lists):
    dummy = ""
    for i in lists:
        dummy = dummy + str(i)
    dres = int(dummy) + 1
    res = []
    for i in str(dres):
        res.append(i)
    return res

print(plusone([1,2,3]))