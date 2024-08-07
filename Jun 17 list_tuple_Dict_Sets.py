#COUNT Method

x=[100,101,101,102,103,104,102,103,105,109]
print(x.count(102))

print(x.index(101)) # INDEX - first occurance 
print("index of 104 is",(x.index(104)))

x.reverse() # reverse the order of list
print(x)

x.sort() # sort list items in ascending order
print(x)

x.sort(reverse=True) # Descending order
print(x)

'''TUPLES similar to list, a seq of immutable objects. Surrounded by
parentheses(),items seperated by comma. List uses square brackets. No changes
are allowed to tuples or the objects'''

a=(1,2,3,4.5,6,True,"acdc")
print(a)
print(type(a))
print(len(a))
print(a.index(4.5))
print(a.count(3))

# Max and Min wont work as the tupple contains String

b=list(a) # Convert tuple to list
print(b)
print(type(b))
x=tuple(b)
print(x)
print(type(x))

'''PYTHON DICTIONARY - KEY VALUE associative array(knwn as hashes).
any key of the dictionary is associated to a value.value of dictionary=any python dat
Dictionaries are unordered key-value pairs.
" are usually numbers and strings
" are enclosed by curly braces({}) values are accessed using square braces([])
each key is seperated from its value by a colon(:), items are seperated by commas,
and is enclosed in a {}
Dictionaries are mutable'''

emp={"name":"John",

     "age":23,
     "role":"datascientist",
     "salary":16}
print(emp)
print(type(emp))
print(emp.keys())
print(emp.values())
print("employee name:",emp['name']) # use square brackets 
print("employee age:",emp.get('age')) # get method use parentheses
#print("employee city:",emp['city']) # error as there is no city as a key
print("employee city:",emp.get('city')) #get method will return as 'none'
print("employee city:",emp.get('city',"city is not available"))

print(emp)

#Update dict with city as it is mutable
emp["city"]="Hyderbad"
print("employee city:",emp.get('city',"city is not available"))
#get method will return the value or say 'none'

# Create a list of values
emp={"name":["John","Jill","Jack"],"age":[21,23,24]}
print(emp)
print("employee name:",emp['name'][0])
emp["city"]=["Hyderabad","London","Tokyo"]
emp["salary"]=[10,12,14]
print(emp)

#Delete items from Dict
del emp["salary"]
print(emp)

#Clear all info from Dict
#emp.clear()
print(emp)
print("city" in emp) # Membership operator to check if city is in emp
print("Tokyo" in emp) #Membership operator works only for KEY

#SETS can also be created with {} but cannot have duplicate values.
#Unordered data type. it takes its own order cant use indexing on sets.
#Unique values only will be taken, dulicates removed ex: sizes, blood group
list=[11,12,13,13,13,14,15,16,17,17,12,1,2]
print(len(list),list)
set={11,12,13,13,13,14,15,16,17,17,12,1,2}
print(len(set),set)













