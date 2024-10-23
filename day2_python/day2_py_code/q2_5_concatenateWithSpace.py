#5. Given a list of names, concatenate them into a single string separated by spaces,
name = ["akash","rima","tanu","dalal","avro"]

re_w = ' '.join(name)
print(re_w)
'''
 NOTE:
The expression ' '.join(names) in Python is used to concatenate the elements
 of the names list into a single string, with each element separated by a space (' ').

Here's how it works:
' ': This is the separator. In this case, it's a space character.
.join(names): The join() method concatenates all the elements of 
the iterable (in this case, the names list) into a single string, using the specified separator (' ' in this case).

n this example, the list names contains individual strings ("Alice", "Bob", etc.), and ' '.join(names) combines 
them into a single string where each name is separated by a space.

If you used a different separator, like a comma (,), the result would be different:
Alice, Bob, Charlie, Diana

'''