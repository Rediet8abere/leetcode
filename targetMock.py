def complement(arr, target):
    # 0 1 2 3 4 5 7
    # 9-0= 9 bin search for 9
    # 9-1= 8 bin search for 8
    # 9-2=7
    # 9-7= 2 bin search for 2
    for i in range(len(arr)):
        comp=target-arr[i]
        low = 0
        high = len(arr)-1
        mid = len(arr)//2
        while low<high:
            if comp == arr[mid]:
                return arr[mid], arr[i]
            elif comp > arr[mid]:
                low = mid + 1
                mid = (low + high) // 2
            elif comp < arr[mid]:
                high = mid - 1
                mid = (low + high) // 2
                # comp = 2 mid = 1 high = 2
                # low = 2 high = 2 mid = 2
    return 'not found'
print(complement([2, 5, 1, 7, 0, 3, 4], 13))
# 7, 2
