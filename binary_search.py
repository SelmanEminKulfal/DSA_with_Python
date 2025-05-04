def binarySearch(arr, targetVal):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == targetVal:
            return mid
        
        if arr[mid] < targetVal:
            left = mid + 1
        else:
            right = mid - 1

    return -1

step = int(input("How many numbers? : "))
my_array = [int(input("Type your numbers : ")) for s in range(step)]
targetVal = int(input("Which number do you want to search? : "))

result = binarySearch(my_array, targetVal)
if result != -1:
    print("Value",targetVal,"found at index", result)
else:
    print("Target not found in array.")