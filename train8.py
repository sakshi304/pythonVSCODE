import re
# import os

# # path='D:\\pythonVSCODE\\wednes8.txt'
# # x= os.listdir(path)                         # This reads only directory not the files

# print(" ----------------RESULT FORM TEXT FILE AS INPUT------------------")
# with open("wednes8.txt","r") as f:
#     pattern = re.compile("python")
#     match =pattern.finditer(f.read())
#     for i in match:
#         print(i.start(),"----",i.end(),i.group())




# print("----------------------PROVIDING STRING-------------------------")
# count=0
# mat =re.finditer("HI","HIHIAADHIIhi")
# for i in mat:
#     count+=1
#     print(i.start(),"----",i.end(),i.group())
# print("Number of occurences of HI",count)


# print("-------------------USER SEARCH INPUT----------------------------")
# obj= input("Run Search for: ")
# mat=re.finditer(obj,"hello jarvis . welcome jarvis")
# for i in mat:
#     print(i.start(),"----",i.end(),i.group())


# import os
# path ="D:\Download data"
# x= os.listdir(path)


# print("------------------Result From Directory------------------------")
# pattern = re.compile(".pdf")
# for i in x:
#     match =pattern.finditer(i)
#     for j in match:
#         print(i,j.start(),"----",j.end(),j.group())


# for i in x:
    
#    if(i.endswith('.pdf')):
#        print("PDF FILES: ",i)

#        print(os.path.getsize(os.path.join(path,i)))
       

obj= input("Enter any string")
objmatch= re.finditer(obj,"HI this is sakshi, ......sakshi")
for match in objmatch:
    print(match.start(),".......",match.group())