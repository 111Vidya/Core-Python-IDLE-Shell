# String Methods

s="apple"
print(s)
print(s.replace("p","P")) # Replace
print(s.replace("p","P",1)) #Replace only 1 capital P

txt="Hello, welcome to my world" # Find method returns the 1st occurance of the element in string
print(txt.find("e"))
print(txt.find("z")) # not in the string will return -1

txt="Company 12" #isalnum will check if the string is alpha numeric
print(txt.isalnum())
txt="Company12"  # isalnum return false as if there is a space
print(txt.isalnum())

#Split uses seperator to split the string. default space is seperator
line="apple ball cat dog egg fish"
print(line)
i=line.split()
print(i)

line="apple-ball-cat-dog-egg-fish"
print(line)
i=line.split("-") # max split is applied
print(i)
i=line.split("-",1) # only one split
print(i)

i=line.split("-") #Joins with a space or - or, 
sent= ".".join(i)
print(sent)
k = ('A','B','C','D')
print("#".join(k))

s="python" 
print(s.upper()) #convert into UPPER
print(s.lower()) #convert into lower
print(s.title()) #1st letter of each word is converted to Upper
print(s.upper()) #first letter of the sentence is converted to upper
print(s.strip()) #Trim off the spaces on the right and left
print(s.rstrip()) #Trim space on the right 
print(s.lstrip()) #Trim space on the left
print(s.startswith("p"))
print(s.endswith("m"))
      
#python string methods- https://www.w3schools.com/python/python_ref_string.asp 

#Raw Strings
print("apple ball")
print("apple \nball") # '\'escape carac 'n' new line
print(r"apple \nball") # Raw String
print("apple \tball")  # Tab space. refer python escape characters on w3schools

#String Formatting - helps insert external input values into string using 'f'
name=input("Enter your name:")
subject=input("Which subject you want to choose:")
if subject.lower()=="Science":
    print(f"congratulations {name}, you have chosen {subject}")
elif subject=="math":
    print(f"congratulations {name}, you have chosen {subject}")
else:
    print("your choice is invalid")

# Curly braces used to insert external values in formatting fn 'f'
x=10
y=20
result=x+y
print(f"sum of {x} & {y} is {result}")

'''LISTS- seqential data with multiple elements with different datatypes
TUPLES similar to lists.
Strings are immutable u cannot make changes to existng memory space.
Lists are mutable.Lists can be created using [],
similar to strings it can be sliced,indexed and concatnate'''
#List Operations -     

list1=[1,2,3,4,5,6,7,8,9,10]
print(list1)
print(type(list1))
print(max(list1))
print(min(list1))
print(sum(list1))

list2=["physics","chemistry", True, 2+3j, 45.0,67]
print(list2)
print(type(list2))

#size of list
print(len(list1),len(list2))

#Indexing on list
print(f"first element of list1 is {list1[0]}")
print(f"last element of list2 is {list2[3]}")
print("last element of list2", list2[-1]) # diff way without using formatting
print(f"3rd element to 5th element of list1 is {list1[2:5]}")
print(f"reversedlist is {list1[::-1]}") # Reversed list
print(f"odd number of list1 {list1[::2]}") # Step fn

#Update and add to list since lists are mutable
fruits=["apple","mango","banana","kiwi"]
print(fruits)
print(type(fruits))
fruits[0]="orange" # update
print(fruits)

#Add values to the end of the list- append and extend
fruits.append("litchi")
fruits.append("peach")
fruits.append("jackfruit") # append to add 1 at a time
print(fruits)

fruits.extend(["pear","grapes"]) #extend to add a list.similar fn can be achived using concat
print(fruits)

fruits.insert(1,"pineapple")# insert fn at index 1
print(fruits)

#JUNE 17th class DELETION FROM LIST

fruits.remove("litchi") # remove the 1st occurance
print(fruits)

del fruits[0] #del method to remove fruits from the 0th index.when we use keywords use box brackets
print(fruits)

#POP method used to remove item and store in a store in a diff variable
last_item=fruits.pop() # will auto remove last item
print(last_item)

third_item=fruits.pop(2) # pop with index
print(third_item)
print(fruits)

fruits[2:4]=[] #remove multiple items
print(fruits)

fruits.clear() #clear
print(fruits)

