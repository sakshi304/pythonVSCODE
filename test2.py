card_number =1234567891234567
list1=[]
list2=[]

for x in str(card_number):

    list1.append(int(x))

for i in range(0,len(list1)):
     if i%2==0:
        j=list1[i]
        list2.append(j)
     #print(i)
for j in list2:
        list2.append(j**2)

print("list1",list1)

print("list2",list2)
print(len(list1))

