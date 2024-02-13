# list2=[2,3,4,5,6]
# sum=0
# for j in list2:
#     x=j%2
#     sum=sum+x

# -----------------------SELECTION SORT-----------------------------------------
# list= [('a',15),('b',3),('c',1),('d',2)]
# y=[]
# for i in range(len(list)):
#     x= list[i]
#     t=x[1]                                    # print(i,list[i])             # i= ('a',1)
#                                         # print(x[1])
#     min= t
#     for j in range(i,len(list)):
#         y= list[j]
#         s=y[1]
#         if(s<min):
#             temp=list[i]
#             list[i]= list[j]
#             list[j]=temp
#             print(list)
#             print("--------------")

#         min=s
# print(list)


# -----------------------BUBBLE SORT-------------------------------
list = [('a', 15), ('b', 3), ('c', 1), ('d', 2)]
n = len(list)

for j in range(n-1):
    for i in range(n):
        if i == n-1:
            break
        x = list[i]

        t = x[1]

        j = list[i+1]
        l = j[1]

        if (l < t):

            list[i], list[i+1] = list[i+1], list[i]

        print(list)
        print("--------------")

    n = n-1


print(list)

# x= i[1]
# min=x                                   #y.append(x)


# print(key(list))
#------------------------INSERTION SORT----------------------------------

list = [('a', 15), ('b', 3), ('c', 1), ('d', 2)]
n=len(list)
x=1
while(x<n+1):
    for j in range(0,x):
        for i in range(x)