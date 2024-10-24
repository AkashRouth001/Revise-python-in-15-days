#3. Implement a function that returns the factorial of a given number using recursion.
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Example usage
num = 5
print(f"Factorial of {num} is {factorial(num)}")
