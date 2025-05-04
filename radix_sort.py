n = int(input("How many numbers? : "))
my_array = [int(input("Enter your numbers : ")) for _ in range(n)]
print("Original array : ", my_array)
radixArray = [[], [], [], [], [], [], [], [], [], []]
maxVal = max(my_array)
exp = 1

while maxVal // exp > 0:

    while len(my_array) > 0:
        val = my_array.pop()
        radixIndex = (val // exp) % 10
        radixArray[radixIndex].append(val)

    for bucket in radixArray:
        while len(bucket) > 0:
            val = bucket.pop()
            my_array.append(val)

    exp *= 10

print("Sorted array:", my_array)