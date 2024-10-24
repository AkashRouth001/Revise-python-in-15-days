#5. Given a list of names, print all names starting with the letter 'A'.
# Given list of names
names = ["Alice", "Bob", "Anna", "John", "Amanda", "Charles"]

# Loop through the list and print names that start with 'A'
for name in names:
    if name.startswith('A'):
        print(name)

'''
Explanation:
name.startswith('A'): This checks if the name starts with the letter 'A'.
The program loops through the list, checks each name, and prints the names that start with 'A'.
'''