#1. Given a list of numbers, create a function to find the sum of all positive numbers.
def sum_of_positive_numbers(numbers):
    return sum(num for num in numbers if num > 0)

# Example usage
numbers = [-5, 3, -2, 7, 8, -10]
print("Sum of positive numbers:", sum_of_positive_numbers(numbers))
