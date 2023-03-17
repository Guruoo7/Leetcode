def twoSums(arr, target):
    dict = {}
    for i in range(len(arr)):
        if (target - arr[i]) in dict: return(i, dict[target - arr[i]])
        else:
            dict[arr[i]] = i

    arr = [-1 for x in range(len(arr))]
    return arr

print(twoSums([43,45,56,32,56,74,78,3,1],152))