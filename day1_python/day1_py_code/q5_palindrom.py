#5. Create a Python function to check if a given string is a palindrome.
'''only one word '''
def palindrome_word(s):
    s = s.lower()
    reversed_s = ""
    for char in s:
        reversed_s = char+reversed_s#reversed the word
    rev_s = reversed_s
    if(s == rev_s):
        return print(f"{s} is plalindrome")
    else:
        return print(f"{s} is not plalindrome")

st = input("enter the word:")
palindrome_word(st)

'''sentence '''
def reversed_str(stm):
    rev_st1 = ""
    for char in stm:
        rev_st1 = char +rev_st1
    return  rev_st1

def palindrome_sent(stm):
    st1 = stm.replace(" ","").lower()
    rev_st1 = reversed_str(st1)

    return st1 == rev_st1

#str = "Too hot to hoot"
str = "Abc def ghi jklm."

if palindrome_sent(str):
    print(f'"{str}" is a palindrome.')
else:
    print(f'"{str}" is not a palindrome.')

################################################################

'''TRY ANOTHER METHOD'''
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
