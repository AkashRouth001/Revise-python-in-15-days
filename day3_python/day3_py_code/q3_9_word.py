#9. Given a list of words, count the number of words with more than five characters.
# Given list of words
words = ["hello", "world", "Python", "is", "awesome", "programming", "fun"]

# Count words with more than five characters
count = sum(1 for word in words if len(word) > 5)

print("\nNumber of words with more than five characters:", count)
#.....................................................
'''
The line count = sum(1 for word in words if len(word) > 5) 
uses a generator expression to count the number of words in the list words that have more than five characters. 
Let’s break down how it works step by step:

Breakdown of the Code:
Generator Expression:

The expression inside the sum() function is a generator expression: 1 for word in words if len(word) > 5.
It iterates over each word in the list words.
Condition:

The condition if len(word) > 5 checks if the length of the current word is greater than 5.
If the condition is true, it produces 1 (indicating that this word meets the criteria).
Sum Function:

The sum() function takes the generated 1s and adds them up.
Since only words that satisfy the condition contribute a 1, 
the final result of sum() is the total count of words longer than five characters.
'''