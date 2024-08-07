''' How to call methods from object? 2 broad ways
. call the method from instance - Bound Method Calls
. call method from inside the class itself - Unbound Method Calls
Accordingly there are 2 ways of calling methods:
. Bound Method Calls-Py automatically bounds the method object(color) to the
instance(self) attribute. 
. Unbound Method Calls- instance(self) is not passed on when def method. when
calling pass on the object .
Attributes are make model color .How to initialize attributes?
Use '__init__' method known as constructor method
we can add, remove and check if an attribute exists or not'''

class Cars: # Class
    def __init__(self,make,model,color,style): #self initiate instance
        self.make=make #attributes
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

class Shark: #Class def
    def __init__ (self,name): #initialize object self name.instances
        self.name=name #define name

jai=Shark("jai") # Pass name object to class
print(jai.name)

print(getattr(jai,"name"))
print(hasattr(jai,"name")) # true or false to tell if it has attr or not
print(hasattr(jai,"age"))
print(setattr(jai,"name","Veeru")) # set to Veeru
print(jai.name)

#delattr(jai,"name") #deleting the object
print(jai.name)

print(Shark.__dir__) # call class directly

#class variables are defined outside the constructor method, instance variables are inside

'''CLASS INHERITENCE - PARENT CLASS or base class crearte a pattern out of which
child or subclasses can be based on. Parent classes allow us to create child
classes through inheritance without having to write the same code over again
each time. Any class can be made into a parent class, so they are each fully
functional classes in their own right, rather thena being templates.
Inheritance is using old Gen class and editing.Child class can reuse parent code'''
# Inheritance - Parent Class

class Person:
    def __init__(self,name,gender,age):
        self.name=name
        self.gender=gender
        self.age=age

    def say_hello(self):
        print(f"Hello, my name is {self.name}")

    def say_bye(self):
        print(f"Bye meet you again")

p1= Person("Tom","M",62)
type(p1)
print(p1.name)
print(p1.age)
p1.say_hello()
p1.say_bye()

p2= Person("Mary","F",32)
print(p2.name)
print(p2.age)
print(p2.gender)
p2.say_hello()
p2.say_bye()

# Inheritance- construct derived class

class Astronaut(Person):
    def __init__(self,name,gender,age,role):
        super(). __init__(name,gender,age) #super keyword helps access methods from parent class
        self.role=role

    def launch_satellite(self):
        print(f"{self.name} is launching a satellite")

    def say_hello(self): #say_hello fn when repeated in child class method will override parent class
        print("Astronaut is saying hello")

class Dancer(Person):
    def __init__ (self,name,gender,age,genre):
        super(). __init__(name,gender,age) #call the base class constructor
        self.genre=genre

    def dance(self):
        print(f"{self.name} is performing a {self.genre} dance!")

class Engineer(Person):
    def __init__(self,name,gender,age,specialization): 
        super(). __init__(name,gender,age) #call the base class constructor
        self.specialization = specialization

    def introduce(self):
        print(f"I am a {self.specialization} engineer")

e1=Engineer("John","M",34,"civil")
e1.say_hello()
e1.say_bye()
e1.introduce()

a1=Astronaut("George","M",46,"Pilot")
print(a1.name)
a1.launch_satellite()
a1.say_hello()

d1=Dancer("Madhuri","F",22,"Classical")
print(d1.age)
d1.dance() #Child Class
d1.say_hello() #Parent class

'''POLYMORPHISM-Access methods from both parent class and child class.
Two classes can have the same method with different functionality.'''

class Dog:
    def make_sound(self):
        print("bow bow")

class Cat:
    def make_sound(self):
        print("meow meow")

class Cow:
    def make_sound(self):
        print("moo moo")

class Bird:
    def make_sound(self):
        print("coo coo")

def animal_sound(animal):
    animal.make_sound()

dog=Dog() #Class Dog same fn defined 
cat=Cat() #Objects will refer to the respective class
cow=Cow() #polymorphism
bird=Bird()

animal_sound(dog)
animal_sound(cat)
animal_sound(cow)
animal_sound(bird)

#Private and public attributes/Encapsulation

class Person:
    #define constructor
    def __init__(self,name,age):
        self.name=name
        self._age=age #private attribute

    #Define Method
    def is_eligible(self):
        if self._age >=18:
            return "Eligible"
        else:
            return "Underage"

p1=Person("Jim", 16)

print(p1.name)
'''print(p1.age) # Private attribute will throw and error & not print'''

print(p1.is_eligible())
    
#Abstract classes- child class must implement abstarct method from parent class
#Parent class method must be difined for child class

class Animal:  #define parent class Animal
    def __init__(self,name): # Define attribute name
        self.name=name

    def make_sound(self): #Define method make sound
        raise NotImplementedError("Subclass must implement abstract method")

class Dog(Animal): #define child class inheriting parent class
    def make_sound(self): # abstract method from parent
        print(f"{self.name} says bow bow")

class Cat(Animal):
    def make_sound(self):
        print(f"{self.name} says meow meow")

dog=Dog("ceaser")
dog.make_sound()

cat=Cat("tommy")
cat.make_sound()
        
    
        
        
    

              

              



        




