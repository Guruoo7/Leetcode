def palindrome(num):
    count = 0
    temp = num
    while num > 0:
        dig = num % 10
        count = count * 10 + dig
        num = num // 10
    if temp == count:
        print("Palindrome")
    else:
        print("Not palindrome")

palindrome(174)