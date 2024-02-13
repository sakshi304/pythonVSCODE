
# r=2
# t= 4/3 *3.14
# print("volume",t*r**3)
from math import pi,pow
rad=2
vol= 4/3 * pi * pow(rad,3)
print("volume:", round(vol,3))
print("volume: %0.2f" %vol)


name="sakshi"
age= 20
print("Your name is ",name,"and age is",age)
print("your name is %s and age is %i" %(name,age))    
print("you name is {} and age is {}".format(age,name))
print("you name is {name} and age is {age}")
print(f"you name is {name} and age is {age}")
'''
'''
import time
# Importing urllib request module in the program  
import urllib.request  
# Using urlopen() function with url in it  
  
print("I am siri ("How may i help ")")

choice = input("1.weather, 2.tell a joke,3.open chrome for pyhton docs ")
match choice:
    case 1:
        look=time.ctime()
        print(f"Current time is {look}")
    case 2:
        print("GADHA")
    
    case 3:
       webUrl = urllib.request.urlopen('https://www.javatpoint.com/python-tutorial')



# import time
# seconds = time.ctime().split()    #slicing
# print("todays day is ",seconds[0],"and month is ",seconds[1],"and time is ",seconds[3:-1]) 

from datetime import datetime
hour= datetime.now().hour
print(hour)

def arithmatic(a,b):
    r=a+b
    n=a*b
    m=a-b
    return r,n,m

result = arithmatic(9,5)
print("result= ",result)

def func(**name):              # passing keyword argument
    print("my name is ",name["lname"])

func(fname="sakshi",lname="kothurkar")

def name(*name):               # passing list of arguments and printing every value
    print(name)

name("sakshi","chaitu",10023)

lambda_cube = lambda y:y*y*y
print("using lambda function  ",lambda_cube(2))

def myname():      # generator function
    yield 's'
    yield 'a'
    yield 'k'
    yield 's'
    yield 'h'
    yield 'i'

output = myname()
for i in range(0,6):  
   print(next(output))



