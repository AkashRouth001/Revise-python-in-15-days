
![App Screenshot](https://github.com/AkashRouth001/Revise-python-in-15-days/blob/993fa060e8494efc8634687bd075eb7841a212a3/image/day2.jpg)


A variable is the name given to a memory location in a program. For example. 
```python
a= 30# variables = container to store a value. 

b= "harry" # keywords = reserved words in python 

c= 71.22   # identifiers = class/function variable name
```
## question we practice
![App Screenshot](https://github.com/AkashRouth001/Revise-python-in-15-days/blob/993fa060e8494efc8634687bd075eb7841a212a3/image/day2%20question.jpg)
## DATA TYPES 
Primarily these are the following data types in Python: 
- Integers 
- Floating point numbers 
- Strings 
- Booleans  
- None

## RULES FOR CHOOSING AN IDENTIFIER 
- A variable name can contain alphabets, digits, and underscores. 
- A variable name can only start with an alphabet and underscores. 
- A variable name can’t start with a digit. 
- No while space is allowed to be used inside a variable name. 
Examples of a few variable names are: harry, one8, seven, _seven etc. 

## OPERATORS IN PYTHON 
Following are some common operators in python: 
1. Arithmetic operators: +, -, *, / etc. 
2. Assignment operators:  =, +=, -= etc. 
3. Comparison operators: ==, >, >=, <,  != etc. 
4. Logical operators: and, or, not.

## TYPE() FUNCTION AND TYPECASTING.  
type() function is used to find the data type of a given variable in python. 
```python
a = 31  
type(a) # class <int> 
b = "31" 
type (b) # class <str>
```
A number can be converted into a string and vice versa (if possible) 
There are many functions to convert one data type into another. 
```python
str(31)    
=>"31"   # integer to string conversion 
int("32")  => 32    
# string to integer conversion 
float(32)  = 32.0  # integer to float conversion
```
… and so, on 
Here "31" is a string literal and 31 a numeric literal. 
## INPUT () FUNCTION 
This function allows the user to take input from the keyboard as a string. 
```python
A = input ("enter name")   # if a is "harry", the user entered harry 
```
It is important to note that the output of input is always a string (even is a number is 
entered). 