#6. Write a Python program to check if a given string is a pangram (contains all letters of the alphabet).

import string
def pangram(sent):
    latter = set(string.ascii_lowercase)
    lowersen = set(sent.lower())
    return latter<= lowersen

sent=" I am king"
#sent="my age is 20"
# sent = "The quick brown fox jumps over the lazy dog"
if pangram(sent):
    print("This is pamgram")
else:
    print("this is not a pamgram")
