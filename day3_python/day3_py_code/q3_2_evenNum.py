#2. Given a list of integers, find all the even numbers and store them in a new list.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_num = []
for num in numbers:
    if(num%2==0):
        even_num.append(num)
print(even_num)

#other method
# Given list of integers
numbers1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# List comprehension to find even numbers
even_numbers = [num1 for num1 in numbers1 if num1 % 2 == 0]

# Print the new list with even numbers
print("Even numbers:", even_numbers)
