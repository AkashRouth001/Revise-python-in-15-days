#5. Write a function to check if a number is even or odd and return "Even" or "Odd" accordingly.
def check_even_or_odd(n):
    return "Even" if n % 2 == 0 else "Odd"

# Example usage
num = 7
print(f"{num} is {check_even_or_odd(num)}")
