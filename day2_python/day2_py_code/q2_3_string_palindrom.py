#Q>3. Implement a program that checks if a given string is a palindrome.
# Function to check if a string is a palindrome
def is_palindrome(s):
    # Converting the string to lowercase and removing spaces for consistency
    s = s.replace(" ", "").lower()
    
    # Checking if the string is equal to its reverse
    return s == s[::-1]

# Example usage
string = "A man a plan a canal Panama"
if is_palindrome(string):
    print(f'"{string}" is a palindrome.')
else:
    print(f'"{string}" is not a palindrome.')