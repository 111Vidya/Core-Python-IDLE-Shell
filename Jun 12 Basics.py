Python 3.12.4 (v3.12.4:8e8a4baf65, Jun  6 2024, 17:33:18) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
#june 6
print("Hello world")
Hello world
print("hello"")
      
SyntaxError: unterminated string literal (detected at line 1)
print("hello""world")
      
helloworld
>>> print("hello"","world")
...       
SyntaxError: unterminated string literal (detected at line 1)
>>> ##Escape Character to print double quotes
...       
>>> print('hi there')
...       
hi there
>>> print('hi "there"')
...       
hi "there"
>>> print("hi "there"")
...       
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> print("hi \"there\"")
...       
hi "there"
>>> 
>>> 2+2
...       
4
>>> 3*3
...       
9
>>> 10/2
...       
5.0
>>> 
>>> ##IDENTIFIERS = VARIABLES
...       
>>> ##CASE SENSITIVE, NO SPL CHARACHTERS EXCEPT _,NO SPACES, CANNOT START WITH _,IF STARTS WITH _ MEANS PRIVATE CLASS VARIABLE,2 LEADING AND TRAILING _ MEANS EXTRA PRIVATE, CANNOT STRAT WITH NUMBER,
...       
>>> ##RESERVED WORDS - PRE DEFINED WORDS CANNOT BE USED AS IDENTIFIER AS THEY ARE KNOWN AS KEYWORDS EX: ELSE,ELSEIF,GLOBAL
...       
>>> '''This is a multi-line comment
this has 2 lines'''

# KEYWORDS ORANGE, STRINGS GREEN, COMMENTS RED,DEFINITION BLUE, MISC WORDS BLACK

''' CODE BLOCKS AND INDENTATION- DENOTED BY LINE INDENTATION, NO. OF SPACES IS
VARIABLE BUT ALL STATEMENTS WITHIN THE BLOCK MUST BE INDENTED SAME AMT'''

# AL THE KEYWORDS ARE LOWER CASE- 'IN' IS A KEYWORD
