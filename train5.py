'''
from collections import deque

x=("sun","east")
d= deque(x)
b= deque("aeiou")
print(d)
print(b)
for i in b:
    
    b.pop()
'''
'''
quiz = {'national_animal': 'tiger','independence':'1947','halleys_comet':'2062','rainbow_collor':'7'}
score =0
for i in quiz:
    print(i)
    x=input("enter answer ")
    if(x==quiz[i]):
        score=score+1
    print('current_score',score)

print('final score',score)
'''

with open("sample.txt","w") as f:
     f.write("Purva")
     f.write("\nShreya")
     f.write("\nMrunali")


with open("sample.txt","r") as f:
     print(f.readlines())


with open("question.txt","w") as f:
     f.write("1.national_animal")
     f.write("2.halleys_comet")
     f.write("3.independence")
 
with open("answers.txt","w")as t:
     t.write("tiger")
     t.write("1962")
     t.write("1947")

def quiz():
    
   
      with open("questions.txt","r")as i:
        i.readline()


'''
#reading and writing binary data
'''
# f1 =open("sample.jpg","rb")
# f2 =open("sign.jpg","wb")
# data= f1.read()
# f2.write(data)
# print("New Image is available")

with open("covid.txt","w") as f:
    f.write("China virus")
    f.write("\ndeadly virus")
    f.write("\nmillions infected")

with open("covid.txt","r") as f:
    print(f.read())              # read complete file
    print(f.read(5))              # read 5 character
    print(f.readline())          # reads single line
    print(f.readlines())          # read complete file with result contained in list

search_text =input("Enter text to change")

replace_text = input("Enter replacement")

with open("covid.txt","r") as file:
    data= file.read()
    data = data.replace(search_text,replace_text)
    
with open("covid.txt","w") as file:
    file.write(data)

# list = []
# list[1]="dont"
# print(list)

# result=[1,2,3,4]
# rolllist= [11,22,33,44]
# print(result)
# print(rolllist)
# item= list( zip(rolllist,result))
# print(item[0])