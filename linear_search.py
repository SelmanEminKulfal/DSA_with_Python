def linearSearch(arr, targetVal):
    for i in range(len(arr)):
        if arr[i] == targetVal:
            return i
    return -1

step = int(input("How many numbers : "))
my_array = [int(input("Type your numbers : ")) for s in range(step)]
targetVal = int(input("Which number do you want to search? : "))

result = linearSearch(arr=my_array, targetVal=targetVal)
if result != -1:
    print("Value",targetVal,"found at index",result)
else:
    print("Value",targetVal,"not found")