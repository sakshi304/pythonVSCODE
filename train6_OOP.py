# class syntax
'''
class student:
    roll_number =101
    num1=50
    num2=100

    def add(self):
        print(self.num1+self.num2)
        self.name = input("enter name: ")
        print(self.name)
obj = student()
obj.add()
print(obj.roll_number)

# construcutor   

class NewClass:                       # self is similar to this in cpp
    def __init__(self):               #self is used to refernence class variables and objects
        print("Constuctor: executes first")

    def show(self):
        print("welcome")

obj=NewClass()
obj.show()
obj=NewClass()

'''
'''
class HOD:
    def __init__(self):
        self.name = "sakshi"        # instance variable
        self.age = 21
        self.empid =2664

    def info(self):                 #m instance method
        print("my name is: ",self.name)
        print()



'''
'''
# declaring instance variable inside a consgtructor by using a self variable.

class Student:
    def __init__(self):
        self.s_name = "sakshi"
        self.l_name= "kothurkar"
        self.s_rollno= 101
        self.s_branch= "CS"
        self.s_mb= 000000000

obj = Student()
print(obj.__dict__)     # print result in the form of dictionary

'''
'''
# accessing and deleting instance variable from the class

class Student:
    def __init__(self):
        self.s_name = input("Enter your name")
        self.s_rollno = 101
    
    def getdata(self):
        self.s_mb = 64963262635



obj = Student()
obj.getdata()               # memory is allocated for getdata() in object
obj.info()
obj.s_branch =" CS"         # adding instance variable by using object
del obj.s_rollno            # deleting a instance variable 
print(obj.s_name)           # accessing a variable outside a class
print(obj.__dict__)         # prints every variable along with its value of an object in form of dictionary



'''

class College:
    collegename= "Modern College"     # STATIC VARIABLE (1 memory)

    def __init__(self):
        self.studentname= "Sakshi"    # instanace variable (3 separate memory)
        College.trusty= "Deepak"      # declaring static inside a constructor using class name

    def object(self,state):
        College.state= "Maharashtra"  
        self.state= state

principal = College()      # object creation
teacher = College()
accountant =  College()
print("principal=",principal.collegename,"......",principal.studentname)
print("teacher=",principal.collegename,"......",teacher.studentname)
print("accountant=",principal.collegename,"......",accountant.studentname)

print("------------------------------------------------------")
College.collegename ="DYP"              # changing value of stai=tic varible using class name  
College.locality = "Pimpri"             # second way to add static variable
principal.studentname="sakshi kothurkar"

print("principal=",principal.collegename,"......",principal.studentname)
print("teacher=",principal.collegename,"......",teacher.studentname)
print("accountant=",principal.collegename,"......",accountant.studentname)
print("accountant=",principal.locality,"......",accountant.studentname)

print("-------------------------------------------------")
principal.object("PUNJAB")
print("Variables of principal objecct",principal.__dict__)    # static variables wont get printed



