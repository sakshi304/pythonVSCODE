# quiz for dictionary
quiz = {'national_animal': 'tiger','independence':'1947','halleys_comet':'2062','rainbow_collor':'7'}
score =0
for i in quiz:
    print(i)
    x=input("enter answer ")
    if(x==quiz[i]):
        score=score+1
    print('current_score',score)

print('final score',score)



#ques: sqaure of nos 

x= [1,2,3,4,5]                                         # 1: using lambda
lambda_square =lambda x:x*x
for i in x:
    print(lambda_square(i));

square_it = list(map(lambda x: x*x, [1,2,3,4]))        # 2: using lambda along with map
print("using lambda along with mapping",square_it)

def square(x): return x*x
squares= list(map(square,[1,2,3,4]))                   #3: using mapping function
print("using mapping",squares)

print([i*i for i in range (0,9)])                      #4: minimal
print([i*i for i in (0,9)])


# quest 3: remove spaces and @ and capitalize 1st char 
'''
list= [" ManGO ","@apple@","bananas","chikku","guavaa"]
# for i in list:     
#       i.strip().capitalize()                                   # didnt work
#       print(i)

def clean(x): return x.strip(" @").capitalize()      # using function
list= [clean(f) for f in list]
print(list)

'''
# quest 3: zipping two lists : zip function
'''
movies =["patthan ", "kesari","drishyam"]
star= ["SRK","AK","AD"]
block= list(zip(movies,star)) 
print(block) 
print(f"{j} stars in {i} "for i,j in (movies,star))

'''
#quest 4: count number of characters in a given string
'''
str = "pineapple"
print(str.count('p'))

x={}
for i in str:
    if i in x:
        x.value= value+1
'''
#########################################################################     

#lambda_table= lambda
'''
for i in range(2,11):
    for j in range(1,11):
        print(i*j, end="\t")

print("------------------------------------------")
for i in range(12,20):
    for j in range(1,11):
        print(i*j, end="\t") 

for i in range(1,11):
    print(i*2," ",i*3," ",i*4," ",i*5," ",i*6," ",i*7," ",i*8," ",i*9," ",i*10)   

'''
# n=6
# for i in range(1,n):
#     print(i," ",n-i)

# print("=================")
# for i,j in zip(range(1,6),range(5,0,-1)):    # combine two for loops
#     print(i," ",j)

# #quest : single input from user
# #        entered character is upper?lower? special symb?  

# x = input("enter input")

# def check(x):
#     if x.islower():
#         print("Lowercase")

#     else:
#         print("Uppercase")
# check(x)

# ch= ord(input("Enter any charac"))
# if ch>=65 and ch<=91:
#     print("your entered character is upper case")
# elif ch>=97 and ch<=122:
#     print("your entered character is lower case")
# elif ch>=48 and ch<=57:
#     print("your entered character is digit")
# else:
#     print("your entered character is special symbol")

# quest : 

# registration(){
#   username
#   password
# }


username= 0
password= 0
def registration():
    x=input("enter username: ")
    y=input("enter password: ")
    print("exit regitration")
   # global username 
    username = x
   # global password 
    password = y

def login(name, passwrd):

     while(name!=username and passwrd!=password):
        
    
y= registration()

x=login(username,password)
while(x):
    z=input("enter username: ")
    y=input("enter password: ")
    x =login(z,y)
'''  
'''
def login():
    username = input("Enter username")
    password = input("Enter password")

    while True:
          if(name!= username)

def register():
    
'''
'''
# questn :curency count  15335
# 1000: 1
# 500:  1
# 200:1
# 100:1
# 20 : 1
# 10 : 1
# 5 : 1


Amount= int(input("enter amount"))

print(" 100 notes ",Amount//100)
print(" 50 notes  ",(Amount % 100)//50)
print(" 20 notes",(()))

'''
'''
n= int(input("Enter the number of rows: "))    
for i in range(1,n+1):
    for j in range(1,n+1):
        print(i,end=" ")
    print()

for i in range(1,n+1):
    for j in range(1,n+1):
        print(chr(64+i),end=" ")
    print()

for i in range(1,n+1):
    for j in range(1,n+1):
        print(n+1-i,end=" ")
    print()

'''