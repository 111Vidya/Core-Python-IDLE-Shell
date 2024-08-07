#Scope of variables
'''variables are identifers that store data.variables may not be accissible in
all locatins in that program.depends where it is declared
Scope of variable determines the portion of program where it can be accessed.
Two basic scopes:
GLOBAL variable-defined outside all fn 
LOCAL variable-defined in a fn are local and cannot be accessed outside.
Same names can be used for local and global variables'''

a=99 #GLOBAL Variable

def func():
    a=88 # LOCAL Variable
    print(a)
    
func() #Access the Local variable within the fn
print(a) #Access Global varaible

# access global fn as a part of def to change variable outside fn

def func():
    global a #Access global Variable as a fn
    a=88 
    print(a)

func() 
print(a)

#Funtions like MAP, FILTER, REDUCE used for mathematical calc
'''MAP() fn applies a given fn to each item of an iterable(list,tuple) and returns
a list of the results. map(function,iterable)'''

#MAP

def calcsquares(n):
    return n*n

numbers=(5,6,7,8,9)
result=map(calcsquares,numbers) #Map is used to apply fn to all iterables of tuple
num_squares=list(result)
print(num_squares)

#Map with Lambda . Usually used with lambda
result=list(map(lambda x: x*x, numbers)) #Map a fn to each iterator
print(result)

#Passing multiple iterarators to map
num1=[4,5,6,7]
num2=[8,9,10,11]
result=list(map(lambda n1,n2:n1+n2,num1,num2))
print(result)

num1=[4,5,6,7]
num2=[8,9,10,11]
result=map(lambda n1,n2:(n1,n2),num1,num2) # Store in tuple
result=list(result)
print(result)
print(dict(result)) #results as dictionary

'''FILTER-Constructs an iterator from elements of iterable for which fn
returns true. methods filters the iterable with the help of fn that test each
element in the iterable and returns only the true instances as result'''

def myfunc(n):
    if n<18:
        return False
    else:
        return True

ages=[19,20,14,15,3,18,4,29]
result=(filter(myfunc,ages))
print(list(result))

#Filter with lambda

result=filter(lambda x:x>=18,ages)
print(list(result))

'''REDUCE-used to apply a particular fn passed in its argument to all of
the list elements mentioned in the sequence passed along.
This fn is defined in "functools" module.Take 1st 2 elemenrts of a list and
result is obtained.Same function is applied to previously attained result
and the number succeeding the 2nd element and result is aagain stored.
Process continue till no more elements are left'''

import functools #use any one of these modules

a=list(range(20))
result=functools.reduce(lambda x,y:x+y,a)
print(result)

from functools import reduce
x=list(range(11))
print(len(x))
result=reduce(lambda a,b:a+b,x)
print(result)

n=[4,8,10,3,2,1,100,200] #two ways of reduce
result=reduce(max,n)                             
print(result)

result=reduce(lambda x,y: x if x>y else y,n)
print(result)



