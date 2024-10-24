#10. Calculate the sum of digits of a given number.
# Input: A given number
number = int(input("Enter a number: "))

# Calculate the sum of digits
sum_of_digits = sum(int(digit) for digit in str(number))

print("Sum of digits:", sum_of_digits)
#............................
'''
The expression sum(int(digit) for digit in str(number)) is called a generator expression in Python.

Key Features of Generator Expressions:
Conciseness:

It allows you to write compact and readable code by generating
values on the fly rather than creating a full list in memory.
Memory Efficiency:

Since it generates items one at a time and only as needed, 
it is more memory-efficient than list comprehensions, especially when dealing with large data sets.
Syntax:

The syntax is similar to a list comprehension but uses parentheses () instead of square brackets [].
This distinction indicates that it is a generator expression rather than a list comprehension.
Comparison with List Comprehension:
A generator expression produces a generator object, while a list comprehension creates a list. 
Here’s a quick comparison:
'''