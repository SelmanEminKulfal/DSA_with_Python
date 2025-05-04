def fibo(n):
    if n <= 1:
        return n
    else:
        return fibo(n-2) + fibo(n-1)
    
step = int(input("How many steps : "))
print(fibo(step))