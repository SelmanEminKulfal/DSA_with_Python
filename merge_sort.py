def mergeSort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    leftHalf = arr[:mid]
    rightHalf = arr[mid:]

    sortedLeft = mergeSort(leftHalf)
    sortedRight = mergeSort(rightHalf)

    return merge(sortedLeft, sortedRight)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result

n = int(input("How many numbers? : "))
my_array = [int(input("Enter your numbers : ")) for _ in range(n)]
print("Sorted array : ",mergeSort(my_array))

# no recursion version. if you want to try this one, please select lines from 38 to 76 and 
# press Ctrl + K + U to uncomment them. Then, you need to comment lines from 1 to 33 using Ctrl + K + C
# After that , you can run the code.
# def merge(left, right):
#     result = []
#     i = j = 0
    
#     while i < len(left) and j < len(right):
#         if left[i] < right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1
            
#     result.extend(left[i:])
#     result.extend(right[j:])
    
#     return result

# def mergeSort(arr):
#     step = 1  # Starting with sub-arrays of length 1
#     length = len(arr)
    
#     while step < length:
#         for i in range(0, length, 2 * step):
#             left = arr[i:i + step]
#             right = arr[i + step:i + 2 * step]
            
#             merged = merge(left, right)
            
#             # Place the merged array back into the original array
#             for j, val in enumerate(merged):
#                 arr[i + j] = val
                
#         step *= 2  # Double the sub-array length for the next iteration
        
#     return arr

# n = int(input("How many numbers? : "))
# my_array = [int(input("Enter your numbers : ")) for _ in range(n)]
# print("Sorted array : ",mergeSort(my_array))
