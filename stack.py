
class Stack:

    def __init__(self,size):
        self.size = size 
        self.stack = []*size  

        for i in range(0,size):
             x=-1
             self.stack.append(x)
        print(self.stack)
        

    def push(self,i,size):
        
        #j= self.empty()
        # if(x):
            # for i in range(0,size):
        x= int(input("Enter element: "))
        self.stack[i]=x

        print("Your stack: ",self.stack)
        # else:
        #      raise Exception("Stack is full")
    
    def empty(self):
         self.empty= False
         for i in self.stack:
              if(self.stack[i]==-1):
                   self.push(i,size)
                   self.empty= True
                   
         return self.empty     

    def check_topmost(self):
         print("Your TOP MOST element in stack: ",self.stack[size-1])
        

    def printn(self):
         print(self.stack)

    

size=int(input("Enter stack size: "))
obj= Stack(size)

obj.empty()                       # raise exception here if stack is full
obj.check_topmost()
obj.printn()




