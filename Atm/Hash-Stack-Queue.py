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



#-----------------------------------------: Stack :-----> LIFO , last in first out , plates ka stack

#: Control-z Control-v , jo sab se baad ma delete hota , wohi sab se pehla show hota

stack = []

#--------------------: Push

e1 = 10
e2 = 20
e3 = 30
stack.append(e1)
stack.append(e2)
stack.append(e3)
print(stack)      # [10, 20, 30]

#----------------------: POP

if not stack:
    print("Stack Empty!")
else:
    e = stack.pop()
    print("Removed Element: ",e )  # Removed Element:  30
    print("Stack : ",stack)        # Stack :  [10, 20]

#------------------------------: Peek
print("Top item: ",stack[-1])           # Top item:  20

#-------------------------------: size

print("Size: ", len(stack))                # Size:  2




#------------------------------------:         Queue       :-----------------------------------------------------------

# FiFo , add items from tail and remove items from head.

# Enqueue → insert an element at the tail.
# Dequeue → remove an element from the front.
# Peek / Front → check the element at the front without removing it.
# isEmpty → check if queue is empty.

#  Dequeue                               Enqueue
#    ^                                      |
#    |                                      v
#
# +---------+   +---------+   +---------+
# |    A    |   |    B    |   |    C    |
# +---------+   +---------+   +---------+


Queue = []

def Enqueue(item):
    Queue.append(item)
    print("Queue: ",Queue)

def DeQueue():
    if Queue:
        removed = Queue.pop(0)
        print(f"Removed: {removed}")
        print("Queue:", Queue)

def Peek():
    print(f'Peek item: {Queue[0]}')

def IsEmpty():
    print("Queue is empty" if not Queue else "Queue is not empty")

    if not Queue:
        print(f'Queue is empty')

Enqueue('A') # Queue:  ['A']
Enqueue('B') # Queue:  ['A', 'B']
Enqueue('C') # Queue:  ['A', 'B', 'C']

DeQueue()  # Queue:  ['B', 'C']

Peek()   # Peek item: B
IsEmpty()  # Queue is not empty





#------------------------------------:         DeQueue (double ended queue)       :-----------------------------------------------------------

# Linear data structure can add,remove element from both side ----->    Head  ---  Tail
# End where elements are added is Tail , End where elements are  removed is Head
# FIFO + LIFO
# EnQueue---> add element in qu ,
# DeQueue----> remove element in qu  ,
# IsFull , isEmpty

# import collections
#
# qu = collections.deque()
# qu.appendleft(10)
# qu.appendleft(20)
# qu.appendleft(30)
# print("Queue: ",qu)   # Queue:  deque([30, 20, 10])
#
# a = qu.pop()
# print("Item Removed: ",a , "   Queue: ",qu)   # Item Removed:  10    Queue:  deque([30, 20])
#
# print("Queue-Empty: ",not qu)   # Queue-Empty:  False
#
# print("Queue Size: ", len(qu))  # Queue Size:  2



#-----------------------------------------------------------: Dictionary Basic Operation

HashMap = {"A":70 ,"B":90 ,"C":30}


#------------------------------------: Add New Key Value Pair
NewKey = input("Enter Key Name: ")
Value = input("Enter Value: ")
HashMap.update({NewKey : Value})
print(HashMap)


#--------------------------------: Updating Key Name

W_K_T_U = input("Enter Key: ")
if W_K_T_U in HashMap:
    NK = input("Enter New Name: ")
    HashMap.update({NK: HashMap.pop(W_K_T_U)}) # OR HashMap[NK] = HashMap.pop(W_K_T_U)
    print(HashMap)
else:
    print("key Not Found!")

#-----------------------------: Update Value by finding key as we just gives the value to repace  with what value.
Which_value = input('Enter Value To Update: ')
if int(Which_value) in HashMap.values():
    NewValue = input('New Value: ')
    HashMap.update({key: NewValue for key,value in HashMap.items() if int(Which_value) == value})
print(HashMap)


#------------------------------------:   Interview Qs

# Sum values and display average.
Hash = {"A":70 ,"B":90 ,"C":30}

Temp = []
for keys , values in Hash.items():
    Temp.append(values)

print(f'Sum: {sum(Temp)})    Average: {(sum(Temp)) / len(Hash)}')    # Sum: 190)    Average: 63.333333333333336











