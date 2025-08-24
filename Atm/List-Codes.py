###--------> Basic Info List <----------

# List = [1,2,3,4,5,2,1,3,42,1,3,3,1]
# from functools import reduce  # +,-,/,* can be done by it by passing lambda inside reduce
# print(List.index(3  if 3 in List else False)) # returns index $2 , 1st occurance
# print([index for index, value in enumerate(List) if value == 3]) # all occurrences in a list
# print(len(List)) # length starting from 1
# List.remove(item) # give item to remove
# List.pop(index) # give index to pop
# max(List), min(List)
# inp = int(input("enter item to count its occurrence in list:  "))
# print(f'item: {inp} , occurs: {l.count(inp)}  Times')
# List.reverse()
# List.sort(reverse=True)
# appeand(item)
# insert(index,item)


from functools import reduce
from pickle import FALSE


# #Minus:
# Lst = [1,2,3]
# M = reduce(lambda x,y : x-y ,Lst)          #= -4    As: 1-2=-1  then -1-3=-4
# print(M)
#
# Sum , Multy , Divide:
# Lst = [1,2,3]
# print("Sum: ",sum(Lst))
#
# D = reduce(lambda x,y:x/y , Lst)           #= 0.16  As: 1/2=0.5  then 0.5/3=0.16
# print("Divide= ",D)


# ///////////////////////////////////////////////////////////////////////:  Sorting
# ///////////////////////////////////////////////////////////////////////
# ///////////////////////////////////////////////////////////////////////: Sorting
# ///////////////////////////////////////////////////////////////////////

# Python's built-in sorting (Timsort) is efficient with a time complexity of O(n log n)
# #
# class Sorting:
#     def __init__(self, List, tuple_list, number):
#         self.List = List
#         self.tuple_list = tuple_list
#
#         self.Map = [
#             {'year': 2000, 'Age': -2},
#             {'year': 2010, 'Age': 8},
#             {'year': 2020, 'Age': 18},
#         ]
#
#     def SimpleSort(self):
#         Sort = self.List.sort(reverse=True)
#         print(f'List: {self.List} Sorted: {True if Sort is None else False}')
#
#     def Sort_By_Length_Of_Indexes(self):
#         zero_inx = self.List[0]
#
#         def sort_by_len(index):
#             return len(str(index)) if isinstance(zero_inx, int) == True else len(index)
#
#         Sort_By_Len = self.List.sort(key=sort_by_len)
#         print(f'List: {self.List}  Sorted:  {True if Sort_By_Len is None else False}')
#
#     def Sort_By_1st_Index(self):
#         Sort = self.tuple_list.sort(key=lambda x: x[1])
#         print(f'List: {self.tuple_list} Sorted: {True if Sort is None else False}')
#
#     def key_base_sorting(self):
#         Map_Sort = self.Map.sort(key=lambda index: index['Age'], reverse=True)
#         print(f' {self.Map} Sorted: {True if Map_Sort is None else FALSE}')
#
#
# Object = Sorting(['1098', '22', '322'], [(1, 'b'), (2, 'c'), (3, 'a')])

# Object.SimpleSort()
# Object.Sort_By_Length_Of_Indexes()
# Object.Sort_By_1st_Index()
# Object.key_base_sorting()
# /////////////////////////////////////////////////////////////////////
#::::::::::::-------------------------------------------------------
# ----------------------------------------------------------------------

# ---------- Recursion :----------------
# Its a case where function calls itself directly or indirectly to solve a problem, in python
# its used in maths calculations and divide & conquer algos.

# syntax:


# def Recursion(parameter):
#     if base_case_condition:
#         return base_result
#
#     else:
#         Recusrion(modified_parameter)
# Recursion()

# Base - Case: stoping condition that prevents infinite recursion.
# Recusrsive - Case: part of fun where it calls it self with modified parms.


def Factorial(number):
    if number == 0:
        return 1
    else:
        return number * Factorial(number - 1)


number = 5

print(f"Factorial Of: {number} is: {Factorial(number)}")


# ---- Fabnoci:
# where each number is the sum of the two preceding ones, typically starting with 0 and 1.
# The sequence is: 0, 1, 1, 2, 3, 5, 8, 13, 21, and so on.
# F(n) = F(n - 1) + F(n - 2)


def Fibnoci(number):
    if number <= 1:
        return number
    else:
        return Fibnoci(number - 1) + Fibnoci(number - 2)


number = 10

for x in range(number):
    print(Fibnoci(x), end=" ")


def ReverseString(String):
    if len(String) <= 1:
        return String

    else:
        return ReverseString(String[1:]) + String[0]


print(ReverseString(String="Hello"))


def ReverseList(List):
    if len(List) <= 1:
        return List

    else:
        return ReverseList(List[1:]) + [List[0]]


print(ReverseList(List=[1, 2, 3]))


# Quartz Conjection:
def Fun(number):
    number = int(number)
    if number == 4:
        print("Number: ", number)
        return

    if number % 2 == 0:
        return Fun(number / 2)

    else:
        return Fun(number * 3 + 1)


# -------------###################################################################:
# ----------------------------------: Calculate the sum of 2 nums form list whose sum is > all other elements sum.
# -------------###################################################################:
# Logic , find pairs of elements , dont make pair of same element, use an var to store sum and check sum > previous or not on run time.

# List = [1,2,5,3,4]
#
# Max_Sum = 0
# for x in List:
#     for y in List:
#         if x != y:
#             Pair = (x,y)
#             if Max_Sum < sum(Pair):
#                 Max_Sum = sum(Pair)
# print(f'Max Sum: {Max_Sum}')


# /////////////////////////////////////////////////////: Missing Nums:

# l = [1, 2, 3, 5,4,6,11,12]
# max_number = max(l)
# Filter = range(1, max_number + 2)
# for x in Filter:
#     if x not in l:
#         print("Missing number is:", x)


###---> Max , Min , SndMax
# List = [1,2,3,4]
# MAX = List[0]
# SndMax = 0
# MIN = List[0]
#
# for num in List:
#     if num > MAX:
#         SndMax = MAX
#         MAX = num
#     elif num> SndMax and num< MAX:
#         SndMax = num
#
# for small in List:
#     if small < MIN:
#         MIN = small
#
# print("Max: ",MAX)
# print("Min: ",MIN)
# print("SndMax: ",SndMax)


# Dict Like Behaviour
#
# LIST = ["aa", "AA", "bb", "BB", "cc", "CC", "dd", "DD"]
# inp = int(input('Enter Key: '))
# if inp % 2 == 0:
#     key = inp - 2
#     val = inp - 1
#     print(f'Key: {LIST[key]}   Value: {LIST[val]}')
#
# if inp % 2 != 0:
#     key = inp - 1
#     val = inp
#     print(f'Key: {LIST[key]}   Value: {LIST[val]}')


# Uniquel element finder
# A = ["a" ,"b","c","d","a" ,"b"]
#
# Filter = []
# Unique = []
#
# for i in A:
#     if i in Unique:
#         Filter.append(i)
#     else:
#         Unique.append(i)
#
# print(Filter)


# Find Selective Indexes Sum     VIP---> Use Odoo wala method , sum(y.loan for y in rec.line_ids)  <---VIP
# List = [1,2,3,4,5,6,7,8,9,10]
# Indexes = [1,3,5]
# print([List[i] for i in Indexes])
# Sum = sum(List[i] for i in Indexes)
# print(Sum)


# Adding corresponding elements from two lists ?
List = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Filter_Even = [x for x in List if x % 2 == 0]
Filter_Odd = [x for x in List if x % 2 != 0]
print(Filter_Even, Filter_Odd)
for i in range(min(len(Filter_Even), len(Filter_Odd))):
    print(f'Sum: {Filter_Even[i] + Filter_Odd[i]}')

##OR : Comprehensive_sum = [even[x] + odd[x] for x in range(min(len(even),len(odd)))]


###:--> Logic: humne 2no even , odoo ki length ki range ma loop kiya and unko apas ma add krdiya ,
# Why use min() :- Compares the lengths of Filter_Even and Filter_Odd.
# if same no.of items han to ye chaleGa , else ni , as agr hum isko use na kren and rying to access an
# index beyond the smaller list would cause an error.
# min() ensures the loop runs only as many times as the smallest list’s size, avoiding index errors.


# Sum the 1st index of list-1 with each index of list-2 , then repeat process for remaining indexes.
#
# List = [1,2,3,4,5,6,7,8,9,10]
# Filter_Even = [x for x in List if x%2==0]
# Filter_Odd = [x for x in List if x%2 !=0]
# print(Filter_Even)
# print(Filter_Odd)
# for x in Filter_Even:
#     for y in Filter_Odd:
#         S = x+y
#         print(S)


###########---------------------------------->How Many Times Occur 1 Element  +    Duplicates Removal From List


List = ['a', 'b', 'c', 'e', 'e', 'c', 'b', 'a', 'g']
Done = []
duplicate_items = []
unique_items = []
for indexes, items in enumerate(List):
    if items not in Done:
        zero_inx = List[indexes]
        Temp = []
        for inx, val in enumerate(List):
            if val == zero_inx:
                Temp.append(items)
        print('Item: {} Occurs: {} - Times'.format(items, len(Temp)))

        if len(Temp) > 1:
            duplicate_items.append(Temp[0])
        if len(Temp) == 1:
            unique_items.append(Temp[0])

    Done.append(items)

print(f'Duplicates:- {duplicate_items}')
print(f'Unique:- {unique_items}')

##:- Logic: know the each element indexes and len() them
#
# List = ['a','b','c','c','e', 'f' ,'a'  ]
# INDEX_A = []
# inx_a = List[0]
# print(inx_a)
# for index,value in enumerate(List):
#     if value == inx_a:
#         INDEX_A.append(index)
# print(INDEX_A)


# ----OR - Using Comprehension------->
List = ['a', 'b', 'c', 'e', 'e', 'c', 'b', 'a', 'g']
Done = []
Dupllicates = []
R1 = [
    (f'Item: {x} Occurs: {List.count(x)}', Dupllicates.append(x))
    for x in List if (x not in Done and not Done.append(x))
                     and List.count(x) > 1
]
print(R1)
print(Dupllicates)

#####-------------------------------------------------------END------------------------------------------------------------
#####-------------------------------------------------------------------------------------------------------------------
#####-------------------------------------------------------------------------------------------------------------------
#####-------------------------------------------------------------------------------------------------------------------

# Check if two lists are equal
# L1 = [3,2,1]
# L2 = [1, 2, 3]
# if L1 == L2:
#     print("Equal")
# else:
#     print("Not Equal")


# Merge two sorted arrays into a single sorted array
# L1 = [1,2,3,4,5]
# L2 = [6,7,8,9,10]
# L1.extend(L2)
# print(L1)

#####################################################################################---------------: Set Operations :-------:-------------#################################################

# ------------------------------------------------Find the intersection of two lists
# L1 = [1,2,3,4]
# L2 = [3,5,6]
# S1 = set(L1)
# S2 = set(L2)
# inter = S1.intersection(S2)
# print(inter)

# #----> InterSection : Remove Duplicates also ---> Without Using Set
#
# List = ['a','b','c','e', 'f' ,'n' ,'a' , 'n' , 'b','f','m','m']
# Listy = ['a','b','c','z','y','m' , 'n', 'a' , 'n','f','f','f','m']
# Done = []
# InterSection = []
#
# for x in List:
#     if x in Listy and x not in Done:
#         InterSection.append(x)
#         Done.append(x)
#
# print(InterSection)

##---------Intersection using List Comprehension
# intersection = []
# [intersection.append(x) for x in List if x in Listy and x not in intersection]
# print(intersection)


# ----------------------------------------------------------Find the union of two lists
# L1 = [1,2,3,4]
# L2 = [3,5,6]
# U1 = set(L1)
# U2 = set(L2)
# U = U1.union(U2)
# print(U)


# #----> Union Of Lists : Without Using Set

# List = ['a','b','c','e', 'f' ,'n' ,'a' , 'n' , 'b','f','m','m','o']
# Listy = ['a','b','c','z','y','m' , 'n', 'a' , 'n','f','f','f','m','o']
# Done = []

# for x in List:
#     if x not in Listy or x in Listy and x not in Done:
#         Union.append(x)
#         Done.append(x)
# for x in Listy:
#     if x not in List and x not in Done:
#         Union.append(x)
#         Done.append(x)
# print(union)

##---------union using List Comprehension
# union = []
# [union.append(x) for x in (list+listy) if x not in union ]
# print(union)


# ----------------------------------------------------------Find the difference between two lists
# L1 = [1,2,3,4]
# L2 = [3,5,6]
# D1 = set(L1)
# D2 = set(L2)
# Diff1 = D1.difference(D2)
# Diff2 = D2.difference(D1)
# Z = Diff1.union(Diff2)
# print(Z)

##--------> Diff Without Set

##--> Finding Diff b/w 2 lists : mean that element that is avail in 1 list not both .... 1st
# find intersec comman items then other then comman will be those present in single list not both...

# # List = ['a','b','c','e', 'f' ,'n' ,'a' , 'n' , 'b','f','m','m']
# # Listy = ['a','b','c','z','y','m' , 'n', 'a' , 'n','f','f','f','m']
# # InterSection = []
# # Diff = []
# # Done = []
# # for x in List:
# #     if x in Listy and x not in Done:
# #         InterSection.append(x)
# #         Done.append(x)
# # for x in List + Listy:
# #     if x not in InterSection and x not in Done:
# #         Diff.append(x)
# #         Done.append(x)
# # print(f'Diff: {Diff}')

# ----> Using List Comprehension:

# Intersection = []
# Differance = []
# Find_Inter = [Intersection.append(x) for x in List if x in Listy and x  not in Intersection]
# Find_Diff_Elements = [Differance.append(x)  for x in (List+Listy) if x not in Differance and x not in Intersection ]
# print(Differance)


# ---------OR --> Simple check if element not in 2nd list append it in diff...

List = [2, 3, 4]
List_2 = [2, 3, 6]
Diff = []
Comprehes1 = [Diff.append(x) for x in List if x not in List_2 and x not in Diff]
Comprehes2 = [Diff.append(x) for x in List_2 if x not in List and x not in Diff]
print(Diff)

####--------------------------------------------------------END------------------------------------------------------------
####--------------------------------------------------------------------------------------------------------------------
####--------------------------------------------------------------------------------------------------------------------
####--------------------------------------------------------------------------------------------------------------------


# Finf len of list without using function :
# L1 = [3,2,1,4]
# Total = 0
#
# for x in L1:
#     Total +=1
#
# print(Total)

# -----------------------------------------> Frequency

# Find the frequency of each element in a list
# L1 = [3,2,1,4,4,5,5]
# for x in L1:
#     Count = L1.count(x)
#     print(f"Item: {x} Occurs: {Count} Times")

#####--> Using Comprehension:
# Result = [f'item:{item}  Occurs:{self.Items.count(item)} - Times' for item in Items if item not in Done and not Done.append(item) ]

##------------------------------------------------------END----------------------------------------------------
##------------------------------------------------------END----------------------------------------------------
##------------------------------------------------------END----------------------------------------------------
##------------------------------------------------------END----------------------------------------------------


# Check if a list is a palindrome : mean front or end sa read krna same ho: (1221)
# List = [1,2,3,2,1]
# if List[0:] == List[::-1]:
#     print('Yes PlaiDrome')
# else:
#     print('Not PaliDrome')


##########--------------------------Kadens Dynamic Approach -----------------------------------------------------------------:
##########-------------------------------------------------------------------------------------------------------------------:

Array = [9, 7, -11, 6, 5, -5, 9, 15, 9]
min = 0  # Maximum Ending Here
max = float('-inf')  # Maximum So Far

for value in Array:
    min = min + value
    if max < min:
        max = min
    if min < 0:
        min = 0  # Reset min if it goes negative

print(max)  # Output: 44

##########--------------------------Kadens Brute Force ----------------------------------:

# Brute Force For Kadens Algorithim  : Find SubArrays then sum the subArrays then find max in
# sumArray then use index of max_sum to find that subArray
# array = [4, -1, 2, 1]
# subarrays = []
# for x in range(len(array)):
#     for y in range(x, len(array)):
#         subarrays.append(array[x:y + 1])
# print(subarrays)
#
# sum_array = []
# for each_sum in subarrays:
#     sum_array.append(sum(each_sum))
# print('Sumed: ', sum_array)
#
# max_sum = max(sum_array)
# index_of_max_sum = sum_array.index(max_sum)
# print(f'Sub Array: {subarrays[index_of_max_sum]}    Sum: {max_sum} ')


##########--------------------------------------------------------------------------------------------------------------


# OR : Find the majority element (element that appears more than n/2 times) in a list.
# Count which item occur most: Cant not mix(str,int)
# List = [1,222,3,4,5,2,2,2,3]
# X = max(List,key=List.count)
# print("Majority Times Element: ",X)
#
# --> OR
#               self.Array =  [9,7, 7, 11]
#               for x in self.Array:
#               print(f'Element: {x} Yes') if self.Array.count(x) > len(self.Array)/2 else print(f'Element: {x} No')


# Sort a list of tuples based on the second element.
# LST = [(1, 5), (2, 3), (3, 7), (4, 2)]
# def Cs(i):
#     return i[1]
# S = LST.sort(key=Cs)
# print(LST)


# SubSet Of any list:
#
# List = [1,2,3]
# L = [[]]
#
# for i in range(len(List)):
#     for x in range(len(L)):
#         A = L[x].copy()
#         A.append(List[i])
#         L.append(A)
# print(L)


# Given a list of numbers, rearrange them such that the even numbers appear
# before the odd numbers while maintaining their relative order.

# LST = [1, 5, 2, 3, 3, 7, 4, 2]
# Even = [x for x in LST if x%2==0]
# ODD = [x for x in LST if x%2 !=0]
# Even.extend(ODD)
# print(Even)


# Divisible By 3 or any number:
# Num = 12
# if Num % 3 == 0:
#     print(True)
# else:
#     print(False)


# Leap Year:-
# year = 2024
# if year%4==0 and (year%100 !=0 or year % 400 ==0):
#     print("leap year")
# else:
#     print("not")


# Stars:
# i = 1
# while i <= 5 :
#     print(i * "*")
#     i = i + 1
#
# i = 5
# while i >= 1 :
#     print(i * "*")
#     i = i - 1


# def Prime(number):
#     for each in number:
#         for i in range(2, int(each/2) + 1):
#             if each % i == 0:
#                 return None
#         Filter.append(each)
#     return Filter
#
# Filter = []
#   
#
# Prime(number)
#
# for x in Filter:
#     print("Prime:", x)


# 
# num = 11
# for i in range(2,num):
#     if num % i == 0:
#         print('Num Is Not Prime')
#         break
# else:
#     print('Num Is Prime')


# Given an array representing stock prices on consecutive days,
# find the maximum profit that can be obtained by buying and selling stocks once.
# Logic:----
#   koi item MIN se small ha then:- min = item  ,,x - min krna ,
#   agr ans large aya maxSofar se then:- mp=sell
#
# prices = [7, 0, 5, 3, 1, 7]
# MinSoFar = prices[0]
# MP = 0
#
# for x in prices:
#     if x < MinSoFar:
#         MinSoFar = x
#     Sell = x-MinSoFar
#     if Sell > MP:
#         MP = Sell
#
# print(MP)


# En,DE
# class A:
#     key = 9
#     EnList = []
#     DeList = []
#     def Encryption(self,LST):
#         for i in range(len(LST)):
#             Var = chr(ord(LST[i]) + self.key)
#             self.EnList.append(Var)
#         return self.EnList

#     def DeCryption(self,EnList):
#         for i in range(len(EnList)):
#             Var = chr(ord(EnList[i]) - self.key)
#             self.DeList.append(Var)
#         return self.DeList
#
# LST = ["a" , "b" ,"c"]
#
# OBJ = A()
# OBJ.Encryption(LST)
# OBJ.DeCryption(OBJ.EnList)
#
# print(f"Encryption Of:- {LST} Is: {OBJ.EnList}")
# print(f"Decryption Of:- {OBJ.EnList} Is: {OBJ.DeList}")


########-----------------Floor Divion : returns index always ....

# Find Median:
# in python Len(Obj) // 2 == gives us the median , mean center element index
# if no.of elements are odd , and if no.of elements are even then it gives the
# index(next from center) , so we have to -1 for previous center
# so after it divide by 2

# EVEN EXAMPLE:
# L = [1,2,3,4,5,6,7,8]
# x = len(L) // 2
# print(x) #:index: 4 which is 5
# y = x - 1 # so -1 from index for previous
# print((L[x]+L[y])/2 )

# Odd EXAMPLE:
# L = [1,2,3,4,5,6,7,8]
# for x in L:
#     Median = x // 2
# print("Index: ",Median , "item: " ,L[Median])


# //////////////////////////////////////::
# x = 'a'
# INT = ord(x)
# STR = chr(INT)
# Binary = bin(ord(x))
# print(STR)

# def ConvrtToBinary(LST):
#     BinaryNum = []
#     for x in range(len(LST)):
#         Bin = bin(ord(LST[x]))
#         BinaryNum.append(Bin)
#     return BinaryNum
#
# LST = ["a","h","s","a","n"]
# print(ConvrtToBinary(LST)    )
#
# def ConvrtBinToStr(LST):
#     Str = []
#     for x in LST:
#         INT = int(x, 2)
#         STR = chr(INT)
#         Str.append(STR)
#     return ''.join(Str)
#
# LST = ['0b1100001', '0b1101000', '0b1110011', '0b1100001', '0b1101110']
# print(ConvrtBinToStr(LST))


# Sum Of First 1000
# def Sum(x):
#     total = 0
#     for i in range(x+1):
#         total += i
#     print(total)
#
# Sum(1000)


# Changing Number 1 to 2:Matrix!
# def Fun():
#     Matrix = [
#         [1, 2, 1],
#         [1, 1, 2],
#         [2, 1, 1]
#     ]
#
#     for RowIndx , LI in enumerate(Matrix):
#         for ItmIndx , Item in enumerate(LI):
#             if Item == 1:
#                 Matrix[RowIndx][ItmIndx] = 2
#     for row in Matrix:
#         for item in row:
#             print(item, end=' ')
#         print()
# Fun()
