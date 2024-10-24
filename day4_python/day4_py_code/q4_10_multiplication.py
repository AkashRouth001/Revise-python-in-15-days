#10. Create a function that takes a number as input and prints its multiplication table.
def multiplication_table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

# Example usage
num = 6
multiplication_table(num)
