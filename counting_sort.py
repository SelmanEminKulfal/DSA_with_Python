def countingSort(arr):
    max_val = max(arr)
    count = [0] * (max_val + 1)

    while len(arr) > 0:
        num = arr.pop(0)
        count[num] += 1

    for i in range(len(count)):
        while count[i] > 0:
            arr.append(i)
            count[i] -= 1

    return arr

n = int(input("How many numbers? : "))
my_array = [int(input("Enter your numbers : ")) for _ in range(n)]
print("Sorted array is : ", countingSort(my_array))