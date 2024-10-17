#8. Given a list of integers, find the sum of all positive numbers.
# Function to calculate the sum of positive numbers
def sum_of_positive_numbers(numbers):
    return sum(num for num in numbers if num > 0)

# Example usage
numbers = [10, -5, 20, -3, 7, -8, 15]
positive_sum = sum_of_positive_numbers(numbers)

print(f"The sum of all positive numbers is: {positive_sum}")
