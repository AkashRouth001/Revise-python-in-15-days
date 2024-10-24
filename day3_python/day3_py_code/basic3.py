# use of if and loop 
#Q> chake the number is -ve,+ve or 0

num = -8
if(num ==0):
    print(num,"is zero")
elif(num>0):
    print(num,"is positive number")
else:
    print(num,"is negative")

#Q> print the 1st 10 even number 
''' there are 3 typr of loop 
1.while loop
2.for loop
'''
print("whith the help of while loop")
count =1
num =1
while (count<=10):
    if((num%2)==0):
        print(num)
        count=count+1
    num = num+1

print("whith the help of for loop")

count1 = 0  # Initialize the counter

# Loop through numbers starting from 1 upwards
for i in range(1, 100):  # Set a large enough range to ensure 10 even numbers are found
    if (i % 2) == 0:  # Check if the number is even
        print(i)  # Print the even number
        count1 += 1  # Increment the counter
    if count1 == 10:  # Stop when 10 even numbers are printed
        break

# for loop type 
'''we wrtire for loop in c like 
for (i = 1; i * i <= n; i++) {
    // Loop body
}

same thing in python
'''
n = 100  # Example value for n
i = 1

# For loop in Python
for i in range(1, int(n**0.5) + 1):
    # Loop body
    print(i)

'''USING C
for (i = 1; i * i <= n; i++) {
    // Loop body
}

'''
'''USING PYTHON'''
n = 100  # Example value for n
i = 1

# For loop in Python
for i in range(1, int(n**0.5) + 1):
    # Loop body
    print(i)

#..............................
'''USING C
for (i = 1; i < n; i += 2) {
    // Loop body
}

'''
'''USING PYTHON'''
n = 10  # Example value for n

# For loop in Python
for i in range(1, n, 2):
    # Loop body
    print(i)


#..............................
'''USING C
for (i = 1; i < n; i = i * 2) {
    // Loop body
}

'''
'''USING PYTHON'''
n = 100  # Example value for n
i = 1

# Use a while loop to multiply i by 2 in each iteration
while i < n:
    # Loop body
    print(i)
    i = i * 2
#..............................