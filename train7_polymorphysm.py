# # Polymorphysm example:

#--------------------COMPILE TIME POLYMORHPHISM------------------------
# class Principal:
#     def role(self):
#         print("I am managing all activity of college")

# class Dean:
#     def role(self):
#         print("Dean+ ia mm decision taking person")

# class HOD:
#     def role(self):
#         print("hod= I have responsibility of teachers and students")

# class Faculty:
#     def responsibility(self):
#         print("faculty baba")

# def func(obj):              
#     obj.role()             # function call

# campus=[Principal(),Dean(),HOD(),Faculty()]

# for obj in campus:
#     func(obj)

'''
Above code trows error as faculty class does not have any function named role 

:::::::::::::::::SOLUTION FOR THE ABOVE PROBLEM:::::::::::::::::::::
---------------->> USE hasattr(obj,'attribute') function  = checks whether object has ann attribute
'''

# class Principal:
#     def role(self):
#         print("I am managing all activity of college")

# class Dean:
#     def role(self):
#         print("Dean =i am decision taking person")

# class HOD:
#     def role(self):
#         print("hod= I have responsibility of teachers and students")

# class Faculty:
#     def responsibility(self):
#         print("faculty baba")

# def func(obj):              
#     if hasattr(obj,'role'):             # function call
#         obj.role()

#     elif hasattr(obj,'order'):
#         obj.order()
    

# obj= Principal()        # creating object of principal class1
# func(obj)

# obj= Dean()
# func(obj)

# print("-----------------OOOOOOOORRRRRRRRR---------------------------------")
# campus=[Principal(),Dean(),HOD(),Faculty()]
# for obj in campus:
#     func(obj)































#------------------------RUNTIME POLYMORPHYSM-------------------------------
# METHOD OVERRIDING
'''
class Father :
    def bike(self):
        print("Harley davidson")
    
    def laptop(self):
        print("SUPER CLASS:laptop with 2GB RAM and 500GB HDD I3 processor")

class Aman(Father):
    def laptop(self):
        super().laptop()                           # Super class method call if u wanna call
        print("CHILD CLASS ATTRIBUTE : 8GB and 1TB HDD I7")
        

obj = Aman()
obj.bike()
obj.laptop()

'''
# Constructor Overriding

class Father:
    def __init__(self):
        print("i am super class constructor")

class Child(Father):
    def __init__(self):
        
        super().__init__()
        print("I am child class constructor")
        super().__init__()

obj= Child()
