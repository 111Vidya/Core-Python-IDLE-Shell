''' Data Types - Numbers, String, Boolean, List, Tuples, Set, Dictionary
Sequential Data Types - String, List, Tuples, Set, Dictionary(hold multiple values)

a. Variable holding NUMERIC values- it is immutable. When a numeric value is assigned
to a variable a new object is created in memory block. and when changing the
value for same variable a new memory object is created.
Numerical Datatypes- int(Whole no.) no decimal point
float- Decimal points and e to the power scientific notation
complex- includes imaginary no a+bj a&b are float & j is imaginary.Real part of
the number is a & imaginary part b'''

print("Hello")

#Get Charc at position 1
a="Hello, World"
print(a[1])
print(len(a)) # Length

a=10
print(a)
print(id(a)) # memory ID
print(type(a))

a=20
print(id(a)) # memory id will change

b=30.2
print(type(b))

c=2+3j
print(type(c))

#b. STRINGS - collection of character . Strings surrounded by '',"",''''''
s="I Love Python"
print(s)
print(type(s))
print(len(s))

#Indexing in pyton starts with 0
print(s[0])
print(s[1])
print(s[2])
print(s[12])

#Python indexing also has negetive indexing.From reverse order.last charac will be -1
print(s[len(s)-1])

#Retrive a subset of string- SLICING 0:5 will give 4 charc last but one index
print(s[0:5])
print(s[-5:-2])
print(s[7:]) # or
print(s[7:14])
print(s[:6])
print(s[:-1]) # the last letter will not be printed

#REVERSE String
print(s[::-1])
print(s[0:5][::-1]) # reverse substring

# STEP FN [start:end:step]
print(s[0:5:2])
print(s[::2]) #print in the reg order with a step of 2

#c. BOOLEAN - True/False.Comparision operators <,>,>=,<=,==,!=
a=True
print(a)
print(type(a))

# >
x=10
y=20
print(x>y)
# <
print(x<y)
# >=
print(x>=y)
# <=
print(x<=y)
# == EQUAL TO
print(x==y)
# != NOT EQUAL TO
print(x!=y)
# Mathematical Fn
import math # module
c=20.3
print(math.ceil(c))
print(dir(math)) #list of FN of Math module.16K modules available on python.org

#Arithmetic Operators- +,-,*,/,%(remainder division),**(exponential,squareof3),//(integer division)
print(10/3)  #float division
print(10//3) #Int division/portion division
print(10%3)  #Remainder division

#Comparision Operators <,>,>=,<=,==,!=
#Logical Operators and,or,not
#Assignment Operators =,+=,-=,/=,*=

a=10
a+=1 #Incremental Operator
a-=1 #Decremental Operator
a/=2 #Divisional Operator
a*=2 #Exponential Operator

#Bitwise Operators &,|, ^,~,>>,<< .Used on Binary data 
#Membership Operators in , not in
s="ABCDE"
"B" in s
"B" not in s

#Identity Operators is, is not

print(("Vidya"+" ")*3) # Arithmetic operators in strings



