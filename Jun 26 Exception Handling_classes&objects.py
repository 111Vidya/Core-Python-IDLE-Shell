#EXCEPTIONS are the errors when executing a program.
'''When error occurs pyhton generates an exception that can be handled which avoids
program to crash. when there is a code which can produce an error use excetion
handling. Python handles excetionusing try..except..block'''

try: # 1st try & except blocks are executed if no error except fn is skipped
    f=open("somemissingfile.txt","r") # if files dont exisit exception raside
    print(f.read())
except IOError: # exception occurs & matches excetion name code in except clause
    print("OOPs..file does not exist")

'''different types of errors.IOError,syntax error.there can be multiple
exception handling in the same block'''

#with open(file.txt) as f: 
#   print(f.read)

print("this line is executed after with open") #line wont print coz of error in code above

try: # exception handling done and all codes print
    with open(file.txt) as f: 
        print(f.read)
except NameError:
    print("file is not existing ")
    
print("this line is executed after with open")

try:      # multiple exception handling 
    with open("demo.txt") as f: 
        print(f.read())
    print(a)
except FileNotFoundError:  #refer online for error name and error type
    print("file is not existing ")
except:
    print("something is wrong") # handle gnerally all errors
finally:
    print("regardless of try and except method print finally")


#Raising Exceptions incase of user defined fn

def age_even_odd(age):
    if age<0:
        raise ValueError("Oops age cannot be less than 0")
    if age==0:
        print("New born")
    elif age%2==0:
        print("age is even")
    else:
        print("age is odd")

print("age even or odd function is executed")

try:
    age_even_odd(-8)
except ValueError as e:
    print(e.args[0])

print("age even or odd function is executed")

age_even_odd(4)
age_even_odd(45)
age_even_odd(0)

#can't have 2 return value.1st return value will be overridden by finally
def foo():
    try:
        return 1
    finally:
        return 2

k=foo()
print(k)

#Classes and Objects
'''Object oriented python program. Everything in python is an object.
Fruits is a class, orange and banana are objects.
same kind off attributes and templates define class,Objects are variety within
class.class is a blue print(recipe) which brings abstarct charecteristics of
a real thing(cake).

class contains variables and methods.to bake you need ingredients & instructions
class varaibles have the same value in all methods and instance variable have
different objects
class defines all necessary methods to access the data'''

#Create a class.user defined class capitalised
#instance attribute name & color. self is instance created for the object
#Class is collection of attributes and methods to build the objects

class Cars:
    def __init__(self,make,model,color,style): 
        self.make=make
        self.model=model
        self.color=color
        self.style=style

    def start(self):
        print(f"{self.make} {self.model} engine is started")
    def stop(self):
        print("engine stopped")

#Object instantiation is required to use the class defined above

car1=Cars("Tata","safari","Grey","SUV") #1 object
car2=Cars("Tata","Punch","Red","hatchback") #2nd object

print(car1.make)
print(car1.model)
car1.start()

    
    
    
    








   



