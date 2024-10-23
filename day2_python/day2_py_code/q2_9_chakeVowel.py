sent = "I am the best "
nsent =  sent.replace(" ","").lower()
count = 0
for char in nsent:
    if("a"==char):
        count=count+1
    elif("e"==char):
        count = count+1
    elif("i"==char):
        count = count+1
    elif("o"==char):
        count = count+1
    elif("u"==char):
        count = count+1

print(count)
    
    