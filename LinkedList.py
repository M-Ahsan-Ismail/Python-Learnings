class Node:
    def __init__(self,Data):
        self.Data = Data
        self.Next = None
class LinkedList():
    def __init__(self):
        self.head = None
        self.N_Itms = 0

    def __len__(self):
        return self.N_Itms

    def insert(self,value):
        NewNode = Node(value)
        NewNode.Next = self.head

        self.head = NewNode
        self.N_Itms = self.N_Itms+1


    def traverse(self):
        a = self.head
        while a is not None:
            print(a.Data, end="->")
            a = a.Next
        print("None")


https://youtu.be/f9Aje_cN_CY?t=10203






Obj = LinkedList()
Obj.insert(0)
Obj.insert(1)
Obj.insert(2)
Obj.insert(3)

Obj.traverse()



# print(len(Obj))