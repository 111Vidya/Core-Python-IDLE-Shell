#DECISION MAKING & LOOPING fn helping in decision making "if, else, elif"

num = int(input("enter any interger:"))
if num%2==0:
    print(f"given number {num} is even")
else:
    print(f"given number {num} is odd")

if num>0:
    print("positive")
elif num<0:
    print("negative")
else:
    print("given number is zero")

#Nested if
age= int(input("enter your age for eligibilty in singing Comp:"))
if age>=15:
    if age<=30:
        print("you are eligible")
    else:
      print("above 30 are not eligible")
else:
    print("below 15 are not eligible")

#also can be written    
if (15<=age<=30):
    print("you are eligible")
else:
    print("you are not eligible")
   
'''WHILE LOOP' repeats a statement or a group of statement while a given
condition is True. When it is False it gets terminated.it tests the condition
before executing the loop body
'FOR LOOP' executes a sequence of statements multiple times and abbreviates the
code that manages the loop variable'''

count=0 # While Loop repeat for <9 times
while count<9:
    print("count is:",count)
    count+= 1  #count = count +1

# while Loop repeat the while loop for <5 times
count=0
while count<5:

    num=int(input("enter any number:"))
    if num%2==0:
        print(f"given number {num} is even")
    else:
        print(f"given number {num} is odd")
    count+=1

print("Thanks for Playing")

 
#For Loop execute a block code on sequence data types or iterables ex:list,strings
#for i in iterable: 'i' each item in iterable 'in' membership operator
#    block of code

for i in "python": # loop for string 
    print(i)

a=[1,2,3,4,5] # Loop is terminated once the items are exhausted
for i in a:
    print(i+i)
    
print("-"*10)

#RANGE- a lot of looping and decision making is done based in this fn
# in built fn generate iterator over a seq of no. generates a seq of no.
for i in range(5):
    print(i)

for i in range(5,20):  # to genrate from 5 to n-1
    print(i)

for i in range(5,20,2): # step 2 in the range 
    print(i)

for i in range(1,6):
    print(i*"*")

fruits=['banana','apple','orange']
for i in fruits:
    print(i)

for i in range(len(fruits)): #instead of mentioning the list of fruits,len of fruits will index t
    print(fruits[i])

#Interview Q print even # from 1 to 100
print(list(range(2,101,2))) # print range of # with step to result in even#

# print range of even/odd# with logic of divisibility
even=[]
odd=[]
for i in range(1,101):
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print(even)
print(odd)

#Nested Loops
for i in range(1,12):
    print(2*i)

for i in range(2,5): # i outer loop*range of J
    for j in range(1,21): # indent here is inside the first loop
        print(f"{i}x{j} = {i*j}")

# Print star pattern
for i in range(3):
    for j in range(5):
        if(i==0 or i==2 or j==0 or j==4): #print stars when any 1 condition TRUE
            print("*",end=" ") # print-line end with space so it will print in same line
        else:
            print(" ",end=" ")
    print() #this print will take next line for every loop in this case 3rows

print("-"*20)

for i in range(3):
    for j in range(5):
        print("*",end=" ")
    print()

#Print inverted triangle
for i in range(6):
    for j in range(6-i):
        if(i==0 or i==5 or j==0 or j==6-i-1):
            print("*", end=" ")
        else:
            print(" ",end=" ")
    print()

#LOOP CONTROL STATEMENTS
#Break:terminates the loop statement that is true & transfer to nest loop.
#Continue:casues the loop to skip the iteration and code after will continue
#Pass:is a null operation, nothing happens when it exeutes.
#Pass statement is usefullin places where your code will eventually go but has not been written yet

for i in range(1,10): # Will skip 7
    if i==7:
        continue
    print(i)

for i in range(1,10): #will break at 7 
    if i==7:
        break
    print(i)

for i in range(1,10): #Nothing happens to 7
    if i==7:
        pass
    print(i)    
        

while True:
    print("welcome to odd or even game")
    num=int(input("enter any number:"))
    if num%2==0:
        print("entered number is even")
    else:
        print("entered number is odd")
    print("enter 'y' to play or 'n' to quit")
    cont=input() # continue based on the user entry

    if cont.lower()=='n':
        print("thanks for playing")
        break #if n break the code

#Looping through Dictionaries and Multiple Sequences is possible using zip fn.

#Iterator operator - iter & next. 
list1=[1,2,3,4]
it=iter(list1) #generate iterator object
print(next(it)) #next to print the iterator object

#Generator- functions that can be defined with yeild method




