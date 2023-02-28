def sort(arr):
    count = 0
    for i in range(len(arr)):
        if arr[i] < arr[i-1]:
            count += 1
    if count > 1:
        return False 
    return True

print(sort([2,1,3,4]))
