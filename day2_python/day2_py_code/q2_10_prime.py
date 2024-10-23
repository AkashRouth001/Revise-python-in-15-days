#10. Write a program to check if a number is prime.
# Input from user
num = int(input("Enter a number: "))

# Prime check logic
if num > 1:
    for i in range(2, int(num**0.5) + 1):  # Only check up to square root of the number
        if num % i == 0:
            print(f"{num} is not a prime number.")
            break
    else:
        print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")
