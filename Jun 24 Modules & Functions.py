# Create a dictionary of students- ex for map,reduce,filter

students = [
     {"name": "Alice", "age": 22, "grade": 88},
     {"name": "Bob", "age": 24, "grade": 75},
     {"name": "Charlie", "age": 23, "grade": 95},
     {"name": "David", "age": 24, "grade": 60},
     {"name": "Eve", "age": 22, "grade": 80},
]

def get_name(student): # MAP
    return student["name"]
student_name=list(map(get_name,students))
print(student_name)

def high_grade(student): #FILTER
    return student["grade"]>80

high_grade_stu = list(filter(high_grade,students))
print(high_grade_stu)

def add_grades(total, student):
    return total+student["grade"]

from functools import reduce

total_grades=reduce(add_grades,students,0) #REDUCE-0 is the initializer assigned to total
print(total_grades)

avg_grade=total_grades/len(students)
print(avg_grade)

'''Namespaces-collections of names of identifiers.types:builtin,global,
local.2 different modules can have same namespaces ex math and Arith module
can both have add as a namespaces

Function of modules is reusability.In the same module you cant repeat a
namespace'''

import mymodule# user defined module saved in same folder
import mymodule2

print(mymodule.add(3,6))

print(mymodule.sub(100,40))

print(mymodule2.add(3,6)) # diff modules same namespaces

'''MODULES-PY file consisiting of code for re-usability.Alows you to logically
organize and group py codes making it easier to use and understand.It can include
fn,classes,variables & runnable code'''

import math
print(math.ceil(3.6))

def ceil(a1,a2):
    a=a1-a2
    return(a)
a=math.ceil(1.5) # ceil from math module
b=ceil(1,22) # ceil from local def .namespaces do not interfere with each other
print(a,b)

import math as mt # alias fu.using mt is shortcut for math
a=mt.floor(4.3)
print(a)
 
'''when defining local variable namespace and if it duplicates with namespace in
modules,local namespace will overshadow the namspace in the module when using
from to import specific fn
If using the import entire module prifix module name to fn. if usong from to
import specific fn directly call fn'''

print(dir(math)) #find all the fn/namespaces defined in a module













