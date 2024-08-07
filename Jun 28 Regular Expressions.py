#RegEx
''' are patterns used to match in strings. to find patterns in text data.
RegEx is a module in py called 're'.it can do pattern matching patternn searching.
used for data validation,ph no. email patterns alpha numeric spl charac

a, x, 9 ordinary charac match themselves axactly
. matches any single charac
\w matches a letter or digitor underbar(a-z,A-Z,0-9,_)
\b boundry b/w word and non word
\s single white space charac
\S non whitespace charc
\t \r \n tab return newline
\d deimal digit 0-9
^ = start, $=end   match the start or end of the string
\  inhibit the specialness of a charac'''

import re

phone_number=re.compile(r'\d{10}') #repetition of 10 digits \d= decimal digit
s="my phone number is 987-789-6789, but my collegues number is +91-9877895678"
mo=re.search(phone_number,s)
print(mo.group())

phone_number=re.compile(r'\d{3}-\d{3}-\d{4}') #\d is element
s="my phone number is 987-789-6789, but my collegues number is +91-9877895678"
mo=re.search(phone_number,s)
print(mo.group()) # will give the 1st occurance ofthe string data


# to find all combi of digits in the string add '+' to \d
#findall fn finds all patterns that are non overlapping numbers
result=re.findall(r'\d+', 'there are 12 apples and 683 oranges.The total is 695')
print(result) # no need to print group here

result=re.findall(r'apples', 'there are 12 apples and 683 oranges.The total is 695')
print(result) # no spl charac. just find a word that is mentioned

result=re.findall(r'a..', 'there are 12 apples and 683 oranges.The total is 695')
print(result)# . represents anything.here the pattern is 3 letter words starting with a

result=re.findall(r'a.d', 'there are 12 apples and 683 oranges.The total is 695')
print(result) #  3 letter words starting with a and ending with d

pattern="ix"
text="onesixer"
match=re.search(pattern,text)
#print(match) #result=re.match object index of ix

print(match.group()) # search for ix

# r stands for raw strings
#grouping the elements- ()
#define the character class- []
#+- matches one or more repetations of the preceeding elements
#?- matches 0 or 1 repetation
#*- matches with 0 or more

# character classes-if square brackets are used 
#[abc]- match anyone 'a','b','c'
#[a-z]- range of a to z in lower class
#[A-Z]- range of A to Z in upper class
#[0-9]- any digit
#[^abc]- if it starts with lowercase a or b or c

#Define URL patterns
http=re.compile(r"https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(/.*)?")

result_http=re.search(http,"my website url is https://vidya-4567.co.in/downloads")
print(result_http.group()) #search - only 1st occurance

#Email Patterns

str="my email is cyrax_bronzewings@google.com. you can also reach me at vermithor_dragon@gmail.com"

match= re.findall("\w+_?\w+@\w+.com",str) #findall- all matches will be results
if match:
    print(match)

#\w+_?\w+@\w+.com- 1st group all words and _ 2nd group@ 3rd group .com

str1="my email is cyrax_bronzewings@google.com. you can also reach me at \
vermithor_dragon@gmail.org"

match= re.findall("\w+_?\w+@\w+.[a-z]{2,}",str1) #2 or more results in curly braces
if match:
    print(match)

#complex email patterns

email=re.compile(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}')
result=re.findall(email,str1)
print(result)


            



