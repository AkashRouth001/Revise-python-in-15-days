#9. Create a program that takes a sentence as input and counts the number of words in it.

def count_words(sentence):
    words = sentence.split()  # Split the sentence into words
    return len(words)

# Example usage
sentence = "Python is an amazing programming language."
word_count = count_words(sentence)

print(f"The number of words in the sentence is: {word_count}")
