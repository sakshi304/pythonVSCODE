''''''

import os
path ="D:\HTML Notes\Chapter 3"
x= os.listdir(path)

# print(x)
# print("end")
y=[]
print(x)
for i in x:
    
   if(i.endswith('.pdf')):
       print("PDF FILES: ",i)

       print(os.path.getsize(os.path.join(path,i)))
       

for j in x: 
    y.append(os.path.getsize(os.path.join(path,j)))
     

item= list(zip(x,y))
print("BEFORE SORT: ")
print(item)
item.sort(key=lambda x:x[1])        # item is numerous tuples inside list [(0,1),(0,1),(0,1),(0,1)]   0,1 are postions
                                    # x is tuple in list
print("AFTER SORT: ")               
print(item)

#OR 

''' 

#questn : enter any path as input listdir will redirect to that path or else default path will work

'''
import os
def check(path="D:\\"):            
    
        
        
        try:
            x= os.listdir(path)

                # print(x)
                # print("end")
            y=[]
            print(x)
            for i in x:
                
                if(i.endswith('.pdf')):
                     print("PDF FILES: ",i)
                     print(os.path.getsize(os.path.join(path,i)))
                
            for j in x: 
                y.append(os.path.getsize(os.path.join(path,j)))
                
            item= list(zip(x,y))
            print("BEFORE SORT: ")
            print(item)
            item.sort(key=lambda x:x[1])        # item is numerous tuples inside list [(0,1),(0,1),(0,1),(0,1)]   0,1 are postions
                                                # 
            print("AFTER SORT: ")               
            print(item)
            
            
        except:
            print("path not found")

x=input("enter path")
check(x)

'''
'''
bank_bal=2000
if bank_bal>1000:
    raise Exception("your account balance is below a accessing limit")
else:
    print("Your amount has withdrawl")

'''
'''
try:
    a= int(input("enter first integer no"))
    b=int(input("enter second integer no"))
    print(a/b)
except (ZeroDivisionError, ValueError) as message:
    print(message)
else:
    print("there are no error in try block")
finally:
    print("i am finally block i always executed whether error raise or not")

'''

#operation with csv file

'''
import csv
f= open("student.csv","a",newline="")
a= csv.writer(f) # here it will return csvwriter object
#a.writerow(["studentID","rollno","name","mobileno"])
#studentid=1
#rollno=1001
#name= "sakshi"
#mobileno = 1546513212

studentid = int(input("enter student id:"))
rollno= int(input("Enter your roll number"))
name = input("ENter your name")
mobileno= int(input("Enter your mobile no"))
a.writerow([studentid,rollno,name,mobileno])
print("student record has save")

'''
# WAP input column name : = ID ,name,rollno,emailid, address, mobileno,p1,p2,p3,p4,p5,total,percentage
# input := name, rollno ,emailid,address, mobileno
# input :=p1,p2,p3,p4,p5
# calculate :=total,percentage
# condition :=if you will pass in all paper then result will be =pass else fail 

# import csv
# f= open("marks.csv",mode='a',newline="")
# a= csv.writer(f)
# n= int(input("Enter no of data to be entered: "))
# id=0

# #a.writerow(['ID' ,'\t name','\trollno','\t\temailid', '\t\t   address', '\t\tmobileno','\t\tp1','\t   p2','\t p3','   p4','  p5','\t\ttotal','\t   percentage','\tresult'])
# email=1234

# for i in range(0,n):
#     id=id+1
   

#     name = input("enter name ")

#     rollno = int(input("enter rollno "))
#     address = input("enter address ")
#     mobile = int(input("enter mobilenno "))

#     email+=1

#     mail= ("%i@gamil.com"%email)
#     p1= int(input("Enter p1 marks: "))
#     p2= int(input("Enter p2 marks: "))
#     p3= int(input("Enter p3 marks: "))
#     p4= int(input("Enter p4 marks: "))
#     p5= int(input("Enter p5 marks: "))
#     total= p1+p2+p3+p4+p5
#     percentage= (total/250)*100

#     result=[]
#     rolllist= []
#     if p1>20 and p2>20 and p3>20 and p4>20 and p5>20:   # for list 
#             result.append("Pass")                                                #result[i]="pass"
#             rolllist.append(rollno)                                                #rolllist[i]=rollno
#     else:
#         result.append("Pass") 
#         rolllist.append(rollno)  

#     x=i
#     if x==i:                   # for csv result column
#        if p1>20 and p2>20 and p3>20 and p4>20 and p5>20:
#             result= "pass"
#        else:
#             result= "fail"
#     a.writerow([id ,"\t",name,"\t",rollno,"\t\t",mail,"\t",address,"\t\t", mobile,"    ",p1,"   ",p2,"  ",p3,"  ",p4,"   ",p5,"  ",total,"\t\t",percentage,"\t\t",result])

# print(result)
# print(rolllist)
# item= list( zip(rolllist,result))
# print(item)
# def check():
    
    
#          print(result)
#          print(rolllist) 
#          y= int(input("enter roll no to check result"))

#          if y>0:
            
#             print(item[y-1])
             
#          else:
#             raise Exception("Invalid rollno")
    

# x=True
# while(x):
#     check()
#     x=int(input("check further? 1/0"))




# y="y"
# while y="y":



# def result(x):
#     with open("marks.csv",'r') as file:
#         csvreader =csv.reader(file)
#         for 
#     if <40:
#         print("Fail")

#     else:
#         print("pass")

# y="yes"
# while y =='yes':
#     x= int(input("enter roll no to check reslt"))

#     result(x)
#     ch=input("continue? yes/no")
 