'''
# classmethod = static method : which contains only statis variables
# classmethod's first argument needs to be cls
class Animals:
    legs=4
    @classmethod
    def walk(cls,name):
        print("{} walks with {} legs....".format(name,cls.legs))

    
Animals.walk('dog')
Animals.walk('cat')

'''

# implementing inner class concept
'''
class BE_first_year:
    def __init__(self):
        self.college_name = "DY PATIL"
        self.branch_name="CSE"
        self.objsem= self.FirstSem()   # inner class constructor call
                                       # NOTE_THAT :  objsem name needs to be same i.e here and calling it outside class
    def display(self):
        print("College Name = ",self.college_name)
        print("branch Name = ",self.branch_name)
    
    # inner class
    
    class FirstSem:
        def __init__(self):
            self.sub1= "M1"
            self.sub2= "physics"
            self.sub3= "chemistry"
            self.sub4= "English"
        
        def show(self):
            print("subject1 =",self.sub1)
            print("subject2 =",self.sub2)
            print("subject3 =",self.sub3)
            print("subject4 =",self.sub4)

obj = BE_first_year()
obj.display()
# objsem= obj.FirstSem()        # accessing inner class object    # inner class object created in association with outer class object
objsem = obj.objsem
objsem.show()

'''
'''
# garbge collector program ( to check if it on/off)

import gc
print(gc.isenabled())
gc.disable()
print(gc.isenabled())
gc.enable()
print(gc.isenabled())

'''



# SINGLE INHERITANCE

class Faculty:           # parent class

    x= int(input("Input check if derived class object directly calls this static variable : ")) 
                                                # Hence derived class object calls this static variable
    def __init__(self,f_name, department,f_id):
        self.f_name = f_name
        self.department = department
        self.f_id = f_id

    def print_info(self):
        print('Faculty information: ',self.f_name,self.department, self.f_id)  

# obj = Faculty("Sakshi","computer_science",1001)
# obj.print_info()
#=======================================================

class Cse(Faculty):
    pass

obj = Cse("Sakshi","Comouter" ,1002)
obj.print_info()


# SINGLE Inheritance

class College:
    def college_name(self):
        print("DYP")

class Student(College):
    def student_info(self):
        print("Name:    Sakshi Kothurkar")
        print("Branch:  Computer Engineering")

obj = Student()
obj.college_name()
obj.student_info()

'''
'''
# Multilevel inheritace

class College:              # first class
    def college_name(self):
        print("College_name: DYP")
    
class Student(College):     # second class
    def student_info(self):
        print("Name:   sakshi kothurkar")
        print("Branch:   CSE")

class Exam(Student):

    def subject(self):
        print("Subject1: DSA")
        print("Subject2: CNS")
        print("Subject3: TOC")

obj = Exam()
obj.college_name()
obj.student_info()
obj.subject()

'''
'''

# MULTIPLE  Inheritance

# class SubjMarks:                           # class1
#     math= int(input("Enter paper marks of math"))
#     TOC = int(input("Enter paper marks of TOC"))
#     c = int(input("Enter paper marks of DSA"))
#     cns = int(input("Enter paper marks of CNS"))

# #============================================== parent class1 

# class PractMarks:      # class2
#     cpract= int(input("Enter practicals marks of c language"))

# #============================================== parent class2

# class Result(SubjMarks,PractMarks):           # childclass
#     #print("if student pass in both = subject and practical paper then  pass")
#     def total(self):
#         if self.math>40 and self.TOC> 40  and self.c>40 and self.cns>40 and self.cpract>20:
#             print('Pass')
#         else:
#             print('fail')

# obj=Result()
# obj.total()

