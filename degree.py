def degreeOfArray(arr):
    # Write your code here
    lenCount={}
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i]==arr[j]:
                if arr[i] not in lenCount:
                    lenCount[arr[i]] = (j-i)+1
                    # print(arr[i])
                    # print("j", j, "i", i)
                else:
                    print(arr[i])
                    print("j", j, "i", i)
                    if lenCount.get(arr[i]) < (j-i)+1:
                        lenCount[arr[i]] = (j-i)+1
    lenValue=list(lenCount.values())
    print("lenValue", lenValue)
    print("lenCount", lenCount)
    return sorted(lenValue)[0]
    # print(lenValue)

print(degreeOfArray([6, 1, 1, 2, 1, 2, 2]))
