def pascals(rowIndex):
    ans = [[1]]
    for i in range(1,rowIndex):
        ans.append([1])
        for j in range(1,i):
            ans[i].append(ans[i-1][j] + ans[i-1][j-1])
        ans[i].append(1)
    return ans


print(pascals(3))