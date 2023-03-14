def anagram(s, t):
    if len(s) != len(t):
        return False
    else:
        for i in range(len(i)):
            for j in range(i):
                if s[i] == t[j]:
                    return True
        return False

print(anagram("a", "ab"))
