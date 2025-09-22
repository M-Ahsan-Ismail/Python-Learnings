🔹 List
Indexed, Ordered, Mutable (changeable), Allows Duplicates
Items maintain insertion order.
Example: my_list = [1, 2, 3, 3]

🔹 Tuple
Indexed, Ordered, Immutable (unchangeable), Allows Duplicates
Once created, cannot add, remove, or update items.
Example: my_tuple = (1, 2, 3, 3)


🔹 Set
Unordered, Unindexed, Mutable, No Duplicates
Can add or remove items, but cannot update a specific item directly.
Items may appear in any order.
Example: my_set = {"apple", "banana", "cherry"}


🔹 Dictionary
Ordered (Python 3.7+), Mutable, Keys Unique (no duplicates)
Stores data as key → value pairs.
Example: my_dict = {"name": "Ali", "age": 25}



#: ////////////////////////////: Stack: lifo , last in first out , plates ka stack
#: Cntrl-z Cntrl-v , jo sab se baad ma delete hota , wohi sab se pehla show hota

# stack = []
#
# #Push:
#
# e1 = 10
# e2 = 20
# e3 = 30
# stack.append(e1)
# stack.append(e2)
# stack.append(e3)
# print(stack)
#
# #POP:
#
# if not stack:
#     print("Stack Empty!")
# else:
#     e = stack.pop()
#     print("Removed Element: ",e )
#     print("Stack : ",stack)
#
# # Peek
# print("Top item: ",stack[-1])
#
# # size
#
# print("Size: ", len(stack))



#//////: Queue , linear dsa , element add,remove both side sa hoskta ismay--> Head---Tail
# End where elements are added is Tail , End where removed in Head
# FIFO + LIFO
# EnQueue--->add element in qu ,
# DeQueue----> remeove element  ,
# IsFull , isEmpty
#
# import collections
#
# qu = collections.deque()
# qu.appendleft(10)
# qu.appendleft(20)
# qu.appendleft(30)
# print("Queue: ",qu)
#
# a = qu.pop()
# print("Item Removed: ",a , "   Queue: ",qu)
#
# print("Queue-Empty: ",not qu)
#
# print("Queue Size: ", len(qu))

#////////////////////////////////////
# Tuple:
# tup = (1,2,3,)




#//////////////////////////////////

# HashMap = { "KEY1" : "Ahsan", "KEY2" : "Khan"   }
#
#
# newK = input("Enter Name: ")
# v = input("enter its value: ")
# HashMap.update({newK:v})
# print(HashMap)
#
#
# W_K_T_U = input("Enter Key: ")
# if W_K_T_U in HashMap:
#     NK = input("Enter New Name: ")
#     HashMap[NK] = HashMap.pop(W_K_T_U)
#     print(HashMap)
# else:
#     print("key Not Found!")
#
# WVal = input("Enter Vale: ")
# if WVal in HashMap.values():
#     NN = input("Enter new Value: ")
#     HashMap.update({key : NN for key,value in HashMap.items() if value==WVal })
#     print(HashMap)
# else:
#     print("Value Not Found!")





#Interview Qs:
#
# Hash = {"A":70 ,"B":90 ,"C":30}
# new = {f"{key}": value for key, value in Hash.items()}
# print(new)
# T=0
# Li = []
# for x in Hash.values():
#    T+=x
#    Li.append(x)
#
# print('sum: ',T)
# print('divide: ', T/len(Li))









