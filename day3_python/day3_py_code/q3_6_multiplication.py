#6. Implement a program that prints the multiplication table of a given number.
n=int(input("entr the number:"))
i = 1
for i in range(1,11):
    print(f"{n}X{i}={n*i}")