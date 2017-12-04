'''
     Python is a general purpose, dynamically typed and interpreted, object
     oriented programming language that was created in the late 1980s by
     Guido van Rossum.

     Python's design philosophy revolves around readability. It's meant to be
     easy to read and easy to write. This is accomplished by using white-space
     to deliniate code blocks instead of the more traditional curly brackets and
     semi-colons.

     Generally all python code is run using an interpreter. The most popular and
     original interpreter is called CPython, because it's implemented in the c
     programming language. Several other interpreters exist however, many of
     which are implemented in languages other than C like Java and C#.

     The most common Python interpreter CPython, uses an automatic garbage collector
     to manage memory. And Python is widely known for having a non-traditional,
     minimalist syntax which is largly based on white space, and designed to be
     clean and readable.

     When first getting into python it can be a bit confusing becasue unlike many
     other programming languages Python has two major, non-compatible versions that
     are currently widely used.

     Python version 2.7.2, released in 2007, is the last iteration of verison 2
     that was released. This verison is for the most part, backwards compatiable
     with all previous versions.

     In 2008, the Founder, Guido van Rossum decided to clean up the Python codebase and overhall
     a lot of the things in Python 2 that he didn't like, thus creating Python 3.

     Python 3 was adopted slowly at first, mainly because it is not backwards compatible with
     Python 2, and there was a huge eco-system of package libraries written for
     Python 2 which now would not work in python 3.

     But now-a-day's the Python 3 ecosystem has for the most part caught up, making
     Python 3 the obvious choice for new developers looking to learn the language.
     Python 3 is also the version that will be taught in this tutorial.

     Many developers choose to write Python using a specilized integrated
     development enviornment. Three of the most popular are Eclipse,
     PyCharm and Netbeans.
'''



# P R I N T I N G

print("Hello")
 print("World")        # unexpected indent
print("!")




# V A R I A B L E S
'''
Names are case-sensitive and may begin with:
   letters, $, _
After, may include
   letters, numbers, $, _
Convention says
   Start with a lowercase word, then additional words are separated
   by underscores
   ex. my_first_variable
'''
name = "Mike"    # Strings
age = 30         # Integer
gpa = 3.5         # Decimal
is_tall = True    # Boolean -> True/False

name = "John"

print("Your name is " + name)
print("Your name is", name)






# C A S T I N G   &   C O N V E R T I N G

print( int(3.14) )
print( float(3) )
print( str(True) )
print( int("50") + int("70") )






# S T R I N G S

greeting = "Hello"
#indexes:   01234

print( len(greeting) )
print( greeting[0] )
print( greeting[-1] )
print( greeting.find("llo") )
print( greeting.find("z") )
print( greeting[2:] )
print( greeting[2:3] )





# N U M B E R S

print( 2 * 3 )       # Basic Arithmetic: +, -, /, *
print( 2**3 )       # Basic Arithmetic: +, -, /, *
print( 10 % 3 )      # Modulus Op. : returns remainder of 10/3
print( 1 + 2 * 3 )   # order of operations
print(10 / 3.0)      # int's and doubles


num = 10
num += 100 # +=, -=, /=, *=
print(num)

++num
print(num)

# Math class has useful math methods
import math
print( pow(2, 3) )
print( math.sqrt(144) )
print( round(2.7) )




# U S E R   I N P U T
name = input("Enter your name: ")
print("Hello", name + "!")

num1 = int(input("Enter First Num: "))
num2 = int(input("Enter Second Num: "))
print(num1 + num2)





# L I S T S
lucky_numbers = [4, 8, "fifteen", 16, 23, 42.0]
#      indexes  0  1       2      3   4   5

lucky_numbers[0] = 90
print(lucky_numbers[0])
print(lucky_numbers[1])
print(lucky_numbers[-1])
print(lucky_numbers[2:])
print(lucky_numbers[2:4])
print(len(lucky_numbers))





# N Dimensional Lists

numberGrid = [ [1, 2], [3, 4] ]
numberGrid[0][1] = 99

print(numberGrid[0][0])
print(numberGrid[0][1])





# L I S T    F U N C T I O N S

friends = []
friends.append("Oscar")
friends.append("Angela")
friends.insert(1, "Kevin")

# friends.remove("Kevin")
print( friends )
print( friends.index("Oscar") )
print( friends.count("Angela") )
friends.sort()
print( friends )
friends.clear()
print( friends )




# T U P L E S
lucky_numbers = (4, 8, "fifteen", 16, 23, 42.0)
#      indexes  0  1       2      3   4   5

lucky_numbers[0] = 90
print(lucky_numbers[0])
print(lucky_numbers[1])
print(lucky_numbers[-1])
print(lucky_numbers[2:])
print(lucky_numbers[2:4])
print(len(lucky_numbers))









# F U N C T I O N S

def add_numbers(num1, num2=99):
     return num1 + num2

sum = add_numbers(4, 3)
print(sum)







# I F    S T A T E M E N T S

is_student = False
is_smart = False

if is_student and is_smart:
	print("You are a student")
elif is_student and not(is_smart):
	print("You are not a smart student")
else:
	print("You are not a student and not smart")


# >, <, >=, <=, !=, ==
if 1 > 3:
	print("number omparison was true")


if "dog" == "cat":
   print("string omparison was true")






# D I C T I O N A R I E S

test_grades = {
    "Andy" : "B+",
    "Stanley" : "C",
    "Ryan" : "A",
    3 : 95.2
}
print( test_grades["Andy"] )
print( test_grades.get("Ryan", "No Student Found") )
print( test_grades[3] )





# W H I L E    L O O P S

index = 1
while index <= 5:
	print(index)
	index += 1






# F O R    L O O P S


for index in range(5):
    print(index)

# lucky_nums = [4, 8, 15, 16, 23, 42]
# for lucky_num in lucky_nums:
#     print(lucky_num)

# for letter in "Giraffe":
#     print(letter)






# E X C E P T I O N    C A T C H I N G

# answer = 10 / int(input("Enter Number: "))

# try:
#     answer = 10 / int(input("Enter Number: "))
# except:
#     print("Error")

# try:
#     answer = 10 / int(input("Enter Number: "))
# except ZeroDivisionError as e:
#     print(e)
# except:
#     print("Caught any exception")       # Big no-no







# Classes & Objects

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def read_book(self):
         print("Reading", self.title, "by", self.author)

book1 = Book("Harry Potter", "JK Rowling");
# book1.title = "Half-Blood Prince"

print(book1.title)
book1.read_book()








# Getters & Setters

class Book:
    def __init__(self, title, author):
        self.title = title;
        self.author = author

    @property
    def title(self):
        print("getting title")
        return self._title

    @title.setter
    def title(self, value):
        print("setting title")
        self._title = value

    @title.deleter
    def title(self):
        del self._title


    def read_book(self):
         print("Reading", self.title, "by", self.author)

book1 = Book("Harry Potter", "JK Rowling");
# book1.title = "Half-Blood Prince"

print(book1.title)
book1.read_book()




#Inheritance
class Chef{

  constructor(name, age){
       this.name = name;
       this.age = age;
  }

  makeChicken(){
       document.write("The chef makes chicken <br>");
  }

  makeSalad(){
       document.write("The chef makes salad <br>");
  }

  makeSpecialDish(){
       document.write("The chef makes a special dish <br>");
  }
}

class ItalianChef extends Chef{

  constructor(name, age, countryOfOrigin){
       super(name, age);
       this.countryOfOrigin = countryOfOrigin;
  }

  makePasta(){
       document.write("The chef makes pasta <br>");
  }

  // overridden
  makeSpecialDish(){
       document.write("The chef makes chicken parm <br>");
  }
}

var myChef = new Chef("Gordon Ramsay", 50);
myChef.makeChicken();

var myItalianChef = new ItalianChef("Massimo Bottura", 55, "Italy");
myItalianChef.makeChicken();
document.write(myItalianChef.age);


# I N T E R P R E T E R
python3

