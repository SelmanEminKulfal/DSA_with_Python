n = int(input("How many numbers? : "))
my_array = [int(input("Enter a number: ")) for _ in range(n)]
minVal = my_array[0]    

for i in my_array:
    if i < minVal:
        minVal = i
        
print("Lowest value: ", minVal)