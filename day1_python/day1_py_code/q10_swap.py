#10. Implement a program that swaps the values of two variables.

def swap_values(a, b):
    a, b = b, a
    return a, b

# Example usage
x = 5
y = 10
print(f"Before swap: x = {x}, y = {y}")
x, y = swap_values(x, y)
print(f"After swap: x = {x}, y = {y}")
