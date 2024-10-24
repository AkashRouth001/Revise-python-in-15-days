#4. Create a function to find the square of each element in a given list.
def square_elements(numbers):
    return [num ** 2 for num in numbers]

# Example usage
numbers = [1, 2, 3, 4]
print("Squares of the list:", square_elements(numbers))
