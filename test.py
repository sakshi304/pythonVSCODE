
# # res= [int(x) for x in  str(card_number)]
# # print(res)
     
print("hello")
# # res=[]
# # for x in str(card_number):
   
# #     res.append(int(x))
# # print(res)

# # print(str(res))
card_number =1234567891234567
list1=[]*16
list2=[]
list4=[]
list5=[]

for x in str(card_number):

    list1.append(int(x))
print("list1",list1)

for i in range(0,len(list1)):
     if i%2==0:
        j=list1[i]
        list2.append(j)
     else:
        j=list1[i]
        list4.append(j)

print("list2",list2)

list3=[]
for j in list2:
        j = j*2
        list3.append(j)

'''
next task to split a double digit and sum it

'''

for j in list3:
     j     

   

print("list3",list3)  
print("list4",list4)  



# print("list1",list1)

# print("list2",list2)
# print(len(list1))


# print(card_number)

# list1=[]
# for i in str(card_number):
        
#         list1.append(i)
# print(list1)
