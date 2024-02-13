# Main thread program
# import threading
# print("Hello world: ",threading.current_thread().getName())

# here current_thread() return thread object 
# here getName() method return current executing thread name


# 1: Creating a thread without using any class:
# child thread

# from threading import*
# import threading
# import time
# def activate():         # user defined method
#     for i in range(1,11):
#         time.sleep(2)
#         print("This is Child Thread\n")

# t= Thread(target=activate)     # creaitng thread object
# t.start()           # starting of thread
# # when we call start() method then thread will create

# # PROCESSES have default thread which is known as MainThread
# # for below : Main Thread
# for i in range(1,5): 
#     print("This is= MAIN THREAD")

# 2: Creating  a Thread by extending Thread class
# whenever we call start() method then automatically run() method will be executed and performs our job

# from threading import*
# import time
# class MyThread(Thread):         #child class
#     def run(self):
#         for i in range(10):
#             time.sleep(2)
#             print("Child Thread-1")
# obj_t= MyThread()
# obj_t.start()

# 3: Creating a thread without extending thread class:

# from threading import*
# class Mytest:
#     def display(self):
#         for i in range(10):
#             print("child thread \n")

# obj=Mytest()
# t= Thread(target=obj.display)
# t.start()

#--------------------Program Without multithreading---------------------------------
from threading import*
import time
def add(num):
    for n in num:
        time.sleep(1)
        print("Add=: ",2+n)
        print()
def mult(num):
    for n in num:
        time.sleep(1)
        print("MULT=: ",n*n)
        print()

num=[1,2,3,4]
starttime=time.time()
add(num)
mult(num)
print("The total time taken: ",time.time()-starttime)




























t1= Thread(target=add,args=num)
t2= Thread(target=mult,args=num)
t1.start()
t2.start()
t1.join()
t2.join()      # Whenever this method is called for any Thread object, it blocks the calling thread till the time the thread whose join() method is called terminates
print("The total time=:",time.time()-starttime)