#lex_auth_01269445968039936095


def validate_credit_card_number(card_number):
    #start writing your code here
    list1=[]
    list2=[]
    list3=[]                       # for doubling items of list 2
    list4=[]                       # for left digits
    card_number =457992154
    for x in str(card_number):
   
        list1.append(int(x))
    for i in range(0,len(list1)):
        if i%2==0:
           j=list1[i]
           list2.append(j)
        else:
           list4.append(i)

    
    for j in list2:
        j = j*2
        list3.append(j) 

    def sum(x):
        


    

        
    
        


           


card_number= 1456734512345698 #4539869650133101  #1456734512345698 # #5239512608615007
result=validate_credit_card_number(card_number)
if(result):
    print("credit card number is valid")
else:
    print("credit card number is invalid")