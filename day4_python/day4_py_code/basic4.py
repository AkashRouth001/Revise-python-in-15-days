#write a function for circule area 
def area(r):
    a = r*r*3.141
    return a

r =int(input("enter the readus :"))
print(f"area is {area(r)}")

#create a function number is prime or not 
def chek_prime(n):
    i =1
    c=0
    for i in range(1,int(n**0.5)+1):
        if(n%i==0):
            c = c+1
            if((n/i)!=i):
                c = c+1
    
    if(c==2):
        return True

    return False

num = int(input("enter the number "))
if chek_prime(num):
    print(num ,"is prime number")
else:
    print(num ,"is not prime number")

#reverce string 
def rev(st):
    revst =""
    for char in st:
        revst = char + revst
    return revst

n="abc"
print(rev(n))