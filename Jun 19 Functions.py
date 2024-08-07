'''FUNCTIONS-inbuilt functions(print,input,max).
USER DEFINED FN -group of related statement to perform a task. break program
smaller,organized and managebale.It avoids repetition and code reusable.
has 2 parts DEFINING & CALLING'''

def my_func():    #Defining gives it a name, structure and instruction
    print("This is my Function")

my_func()         #Calling generates the output

def guessthecountry(cur):
    if cur=="INR":
        print("India")
    elif cur==("GBP"):
        print("UK")
    elif cur==("Dolor"):
        print("USA")
    else:
        print("NONE")
        
cur=input("Enter the currency to guess the country:")

guessthecountry(cur)
   

#Call by value reference -Immutable string data does not change outside fn
string = "Tata" #Outside fn
def test(string):
    string="I Love Tata" #inside fn
    print("Inside the function:", string) #insidefn when executed will print ilovetata

test(string) #as a part of def it changed
print("Outside Function:",string) #actual string object has not changed

#Pass by Object reference -mutable data.the actual object(list1) changes
list1=[1,2,3,4]
def addlist(l):
    l.append(5)
    print("Inside fn:",l)
    
addlist(list1)
print("Outside fn:",list1)

#Arguments-inputs that we pass on to the functions
#Positional Arguments-when possition cannot be changed.maintain order of argument

def display_info(name,age): #Possitional arguments
    print("My name is:", name)
    print("My age is:",age)
display_info("Vid",30)

display_info(30,"Vid") # Understanding possitionall arguments. maintain possition

#Keyword argument
def display_info(name,age): 
    print("My name is:", name)
    print("My age is:",age)

display_info(age=30,name="Vid")

#Default arguments
def display_info_default(name="Vid",age=15): #Default values 
    print("My name is:", name)
    print("My age is:",age)

display_info_default() #No mention of passing values.

#Variable Arguments-Use *before aruguments that can vary.
def add(*numbers):
    sum=0
    for i in numbers:
        sum=sum+i
    return sum
x=add(20,30,40)
print("the sum of given num:",x)

'''Anonymous Functions - LAMBDA need not be declared with 'def' keyword.
Create fn without a name. use a lambda as name.
Can take any no. of arguments and one code,return one value in the form of expression.
Cannot be a direct call to print. it requires an expression like return.
Lamda have thier own local namespace. define and use it there'''

x=lambda a:a*a
print(x(5))
print(x(10))

y= lambda a,b,c:a+b-c
print(y(10,5,3))
print(y(100,20,50))

def myfunc(n):
    return lambda a:a*n #use lambda to cut down the length of the code

mydoubler=myfunc(2) # n value
print(mydoubler(10)) # a value

mytripler=myfunc(3)
print(mytripler(10))

#fn to take the length and breadth of a rectangle and return the area
def area_rec(length,breadth):
    return length*breadth
length=float(input("enter length:"))
breadth=float(input("enter breadth:"))
area=area_rec(length,breadth)
print(f"area of rectangle is: {area}")

area=area_rec(10,4)
print(area)


