#7. Write a program that calculates the factorial of a given number.
def factorial(n):
    # Base case: factorial of 0 is 1
    if n == 0:
        return 1
    return n * factorial(n - 1)

# Input from user
n = int(input("Enter the number: "))

# Print the factorial calculation process
for i in range(1, n+1):
    if i < n:
        print(i, "X", end=" ")  # Print with 'X' and space, without a newline
    else:
        print(i, end=" ")  # Last number without 'X'

# Print the final result
print("=", factorial(n))
