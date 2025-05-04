n = int(input("How many numbers? : "))
my_array = [int(input("Enter your number : ")) for _ in range(n)] 

for i in range(n):
    min_index = i
    for j in range(i+1, n):
        if my_array[j] < my_array[min_index]:
            min_index = j   
    my_array[i], my_array[min_index] = my_array[min_index], my_array[i]

print("Sorted array:", my_array)  