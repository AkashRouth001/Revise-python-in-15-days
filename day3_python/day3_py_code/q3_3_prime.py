#3. Write a Python program to check if a given number is s prime number.
i =1
n =int(input("enter the number :"))
count =0

#method1(TC=> O(N))
for i in range(1,n):
      if(n%i==0):
            count = count+1

if(count==2):
      print(f"{n} is prime number")
else:
 print(f"{n} is not a prime number")


#method2(TC=>O(srt N))
for i in range(1,int(n**0.5)+1):
      if((n%i)==0):
            count = count+1
            if((n/i)!=i):
                  count=count+1
if(count==2):
      print(f"{n} is prime number")
else:
    print(f"{n} is not a prime number")
