#2. Write a Python function to check if a given string is a palindrome.
def is_palindrome(s):
    s = s.lower()  # Case insensitive
    return s == s[::-1]  # Reverse the string and compare

# Example usage
word = "Radar"
print(f"{word} is a palindrome?" , is_palindrome(word))
