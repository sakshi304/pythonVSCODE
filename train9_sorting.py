import os
path ="D:\DELETE_THIS_FILE"
x= os.listdir(path)

# print(x)
# print("end")
y=[]
# print(x)
for i in x:
    
   if(i.endswith('.pdf')):
       print("PDF FILES: ",i)

       print(os.path.getsize(os.path.join(path,i)))
       

for j in x: 
    y.append(os.path.getsize(os.path.join(path,j)))
     

list= list(zip(x,y))
# print(list)
print("")
print("")
print("")
print("")
print("")
for i in range(len(list)):
    x= list[i]
    t=x[1]                                    # print(i,list[i])             # i= ('a',1)
                                        # print(x[1])
    min= t
    for j in range(i,len(list)):
        y= list[j]
        s=y[1]
        if(s<min):
            temp=list[i]
            list[i]= list[j]
            list[j]=temp
            # print(list)
            # print("--------------")
        
        min=s
    print(list)
    print("----------------------------------")
print(list)



