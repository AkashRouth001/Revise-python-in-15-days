#4. Create a program that generates the Fibonacci sequence up to a given number of terms.
def fibonacci(n):
    if(n<=1): 
     return n
    last = fibonacci(n-1)
    last2 = fibonacci(n-2)

    return last+last2

num =int(input("enter the range"))
for i in range(num):
        print(fibonacci(i), end=" ")