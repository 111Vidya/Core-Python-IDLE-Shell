#FILE HANDLING
'''Read and write a file use fn "open" that will return a file object(fp) that is
stored in a variable.Acess mode determines the mode in which the file needs to
be opened.
format-fp=open(file_name[,access mode][,buffering])
r mode opens the file read only. r or rb are default modes
rb read only file binary
r+ open file for both reading and writing
rb+ open file for both reading and writing in binary format
w file for writing only.overwrites the existing file.to create a new filechange name
wb file for writing only in binary
w+ file for reading and writing.overwrites the existing file or change name
wb+ file for reading and writing in binary
a opens file for appending.add to exisiting file.cursor will be at the end
ab opens file for appending in binary format
a+ opens file for both reading and appending
ab+ opens file for both reading and appendingn in binary mode
buffering-optional parameter.needed for large files.it will not read the entire
file at one shot it will ration the chunks of bytes to read in memory.
Once the file is open with the syntax.Use read() to read a string from an open
file. Py strings can have binary data too.
file.closed returns if it is true or false
file.mode returns the access mode in which it is opened
file.name for the name of the file'''

fo=open("demo.txt",'w') #will create a new file called demo.txt,overwrites if it exists
fo.write("This is a demo file created using open function in write mode.")
fo.close() # if not closed causes buffering
print(fo.closed) #to check if the file is closed True or False.always close

fo=open("demo.txt","r") # read only also default mode even if 'r' not mentioned
print(fo.read())
print(fo.mode)
fo.close() #check mode before closing

#use the path if the file where saved and change to fwd/ instead of backward

# Append mode
fo=open("demo.txt","a")
fo.write(" append mode does not overwrite the file.instead allows making changes from the end of the file.")
fo.close()

fo=open("demo.txt","r")
print(fo.read())
print(fo.tell()) #Tell fn will read all the text and cursor at the end
fo.close()

with open("demo.txt") as fo:
    print(fo.read(8))
    print(fo.tell()) # Tell fn to point at where the cursor is
    fo.seek(0,0) #Offset=0 & whence=0 the begining

with open("demo.txt") as fo:
    print(fo.read(8))
    print(fo.tell()) # Tell fn to point at where the cursor is
    fo.seek(2,0) #Offset=2 & whence=0 2 points after the begining

# SEEK fn
'''used to change the current position of the file pointer to a specific
location allowing to read or write from that point'''


#Create file with "with open()"

with open("demo2.txt","wb") as fp:
    fp.write(b'\x00\x01\x02\x03')

with open("demo2.txt","rb") as fp: #read binary file
    data=fp.read()

print(data)

#Seek
f=open("demo2.txt","w")
f.write("This is 1st line")
f.close()
f=open("demo2.txt","r")
print(f.read)
f=open("demo2.txt","a")
f.writelines("This is 2nd line")
f.close()
f=open("demo2.txt","r")
print(f.read)
f.close()

with open("demo2.txt") as f:
    f.seek(5,0)
    print(f.read(5)) # Reading from 5th byte to succeeding 5 bytes


# Rename and Delete File can be done Py OS module

import os
print(os.getcwd()) # current working directory
os.chdir # change directory
# os.rename("demo2.txt","ML.txt")
# os.remove("ML.txt") to remove file


    

    









