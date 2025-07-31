#Encapsulation:

# By default acessiable all methods,variable
# PROTECTED = SINGLE _    class fun , class obj can use
# Private = 2 __         acessiable only in class , not outhside by obj

# class protected:
#     _a = 10
#
# class B:
#     obj = protected()
#     b= 10
#     s = int(b) + int(obj._a)           # can not do:   s = int(b) + int(_a)
#     print(s)
#
# OBJ_B = B()


# class Private():
#     __a = 10
# class B():
#     obj = Private()
#     b= 10
#     s = int(b) + int(obj.__a)    # Error AyaGa , Juggar:Hack :int(obj._Private__a)
#     print(s)
# OBJ = B()




#::::::::::::::::::::--------------::::::::::::::###############################################
#/////////////////////////////////////////////#: Abstraction-Example:
#First.py --> Add()
#
#Second.py ---> Subtract()
#
#Main.py ---> import First,Second
# First.Add()  , Second.Subtract()
#
#/////////////////////////////////////////////# Abstraction--->  implemented by abstract class and interface.
#/////////////////////////////////////////////#

######: Abstract Class:
# from abc import ABC, abstractmethod
# class Car(ABC):
#     def WheelCount(self):
#         print("Car Have 4-Wheels!")
#
#     @abstractmethod
#     def Speed(self):
#         pass
# class Rocco(Car):
#     def Speed(self):
#         print("Rocco ---> 200Km/H")
#
# Obj_Car = Rocco()
# Obj_Car.WheelCount()
# Obj_Car.Speed()






#////////////////////////////////////////////////////////////////
#////////////////////////////////////////////////////////////////#:  PolyMorphisim:
# class Vechile():
#   def Move(self):
#     print("Car :- Moves")
#
# class Boat(Vechile):
#   def Move(self):
#     print("Boat :- Sails")
#
# class Plane(Vechile):
#   def Move(self):
#     print("Plane :- Flies")
#
#
# VehObj = Vechile()
# BoatObj = Boat()
# PlaneObj = Plane()
#
# for x in VehObj,BoatObj,PlaneObj:
#   x.Move()

###############:::::# OverLoad:Ex-1:

# class Calculator:
#     def add(self, a, b):
#         return a + b
#
#     def add(self, a, b, c):
#         return a + b + c
#
#
# calc = Calculator()
# print(calc.add(2, 3 ,4))

###############:::::# # OverRide: its runTime polymor and always happen in [parent--child] and
# used to change behaviour of existing methods.

# class Animal:
#     def sound(self):
#         print("Generic animal sound")
#
# class Dog(Animal):
#     def sound(self):
#         print("Bark")
#
# dog = Dog()
# dog.sound()



#////////////////////////////////////////////////////////////////
#////////////////////////////////////////////////////////////////:::
# Class Method
#: uses @classmethod decorator and passes CLS as 1st argument , classMethd is bounded with class not object.
#:can acess class , can modify class , knows class state,
#:By classMthd we can control the value of class-variable globally.

# class Ahsan:
#     grade = 2
#     def __init__(self, age):
#         self.age = age
#
#     def Result(self):
#         print("Age: ",self.age , "Grade:",self.grade)
#
#     @classmethod
#     def ClassMethod(cls,grade):
#         cls.grade = grade
#
# obj = Ahsan(5)
# obj1 = Ahsan(15)
#
# Ahsan.ClassMethod(100)
#
# # obj.grade = 100
# # obj1.grade = 500
#
# obj.Result()
# obj1.Result()


#Static methd:
# knows nothing about class state.

# class A:
#     @staticmethod
#     def a():
#         print("This is a Static Method , Uses: Grouping related functionality: , Improving code readability")
#         print("No parameter like: CLS , Cant acess or modify class attributes")
# Obj = A()
# Obj.a()


#----------------------------:Virtual Method:
#virtual method is a method whose behavior can be overridden by  inheritance  by  same name.
# in python all methods are virtual by default , menas virtual methods are implemented with method_overRiding.
# class A:
#     def Virtual(self):
#         print("Hy!")
# class B:
#     def Virtual(self):
#         print("Its Virtual Method!")
# obj = B()
# obj.Virtual()




#/////////////////////////////////////////////////////////////////
# early means when type of variable is determined at compile time.
#Early-Binding:
# x: int=10

#Late-Binding:
# x =10









#/////////////////////////////////////////////////////////////////: Enums:
# Enums, short for "enumerations," are like labels
# Enums allow us to define a set of named constants.
# These constants are used to represent values that are fixed and known at compile-time.
#Example, if you have a set of colors (Red, Green, Blue), instead of using strings like "Red", "Green",
# "Blue" directly in your code, you can define an enum:
from enum import Enum
# class Color(Enum):
#     RED = 1
#     GREEN = 2
#     BLUE = 3

#Now you use: Color.RED, Color.GREEN, Color.BLUE
# Benefit: Readability , Maintainability






#:::::::::::::::###########################--------------------###:#######-------------------------
#:::::::::::::::###########################--------------------###: inheritance:
#:::::::::::::::###########################--------------------###:--------------------------------

#When we use , __init()__ in child class , then child looses all its parent inheritance and init()
#overRides parent inhertance.

# class Parent():
#     def __init__(self):
#         self.Name= "Ahsan"
#         self.Age = 22
#     def Life(self):
#         print(f"AGE: {self.Age}  Name: {self.Name}")
#
# class Child(Parent):
#     def __init__(self):
#        self.Country = "Pakistan"
#     def Life_Indication(self):
#         print(f"INDICATION: {self.Age}")
#         print(f"INDICATION: {self.Name}")
#
#
# obj = Child()
# obj.Life_Indication()

#:::::::::::::::::::::::::::::::Parent inheritance + init()

# Then To use , Parent inheritance + init() use: ParentClass_Name.__init__(self)
# class Parent():
#     def __init__(self):
#         self.Name= "Ahsan"
#         self.Age = 22
#     def Life(self):
#         print(f"AGE: {self.Age}  Name: {self.Name}")
#
# class Child(Parent):
#     def __init__(self):
#         self.Cout= 22
#         Parent.__init__(self)
#     def Life_Indication(self):
#         print(f"INDICATION: {self.Age}")
#         print(f"INDICATION: {self.Name}")
#
# obj = Child()
# obj.Life_Indication()




#:::::::::::::::::::::::::::::::super().__init__(self), super keepsn inheritance and we do not need to write
# parenClass_Name. as it do it in background , self paremeter also not required.

# class Parent():
#     def __init__(self):
#         self.Name= "Ahsan"
#         self.Age = 22
#     def Life(self):
#         print(f"AGE: {self.Age}  Name: {self.Name}")
#
# class Child(Parent):
#     def __init__(self):
#        self.Country = "Pakistan"
#        super().__init__()
#     def Life_Indication(self):
#         print(f"INDICATION: {self.Age}")
#         print(f"INDICATION: {self.Name}")
#
#
# obj = Child()
# obj.Life_Indication()


#------------------------------------:MultiLevel inheritance:
# class GrandFather():
#     def GrandProperty(self):
#         pass
# class Father(GrandFather):
#     def Fatherproperty(self):
#         pass
# class Child(Father):
#     def GrandProperty(self):
#         print("Its Grand Property!")
#
#     def Fatherproperty(self):
#         print("Its Father Property!")
#
# Obj = Child()
# Obj.GrandProperty()
# Obj.Fatherproperty()




#:::::::::::::::###########################--------------------###:#######-------------------------
#:::::::::::::::###########################--------------------###: First Class Method:
#:::::::::::::::###########################--------------------###:--------------------------------


# when function is treated like an variable , function can be passed as an argument to other function ,
# can be retuned by another function , Can be assigned to variable

#---------------------: Assign to variable:
# def FCM(name):
#     return f"Hello, {name}"
#
# Variable = FCM
# print(Variable("Ahsan"))

#-------------------As an Argument:
# def Fun(name):
#     return f"Hy {name}"
# def Super(Fun):
#     return Fun
#
# print(Super(Fun("Ahsan")))

#-------------------Returning From other Fun:

# def Returning_Fun():
#     return f"I am Returning To U!"
# def Fun():
#     if "1" == "1":
#         return Returning_Fun
#     else:
#         return lambda: "Error!"
#
# X = Fun()
# print(X())



########################################################################################################################
#--------------------------: Diamond Problem In Multiple Inheritance  :-------------------------------------------------

# occurs in multiple inheritance when a class inherit 2 classes which are inherited from comman ancestor.this creates an issue , when we will access methods from base class (ol ansestor) which path we will follow.
                         # A
                      # /     \
                     # B       C
                     #   \   /
                     #     D

# Example:
# Now, if class D tries to access something from class A, which path should it follow? Through B or C?

# How Python Resolves It:
# Python Uses MRO , Method Resolution Order , MRO uses C3 Literalization that creates a specific order of classes when looking up for not methods.

class A:
    def Say(self):
        print('Ahsan')

class B:
    def Say(self):
        print('Ahsan')

class C:
    def Say(self):
        print('KHAN')

class D(C,B):
    pass

Object = D()
Object.Say() # KHAN python chooses that class who is inherited first as C was first , B was 2nd. that's it.
print(D.mro()) # [<class '__main__.D'>, <class '__main__.C'>, <class '__main__.B'>, <class 'object'>]







#---------------###############################
#-------------------------------------------------Genrator : genrating even nums upto 10:

# def Genrate_EvenNums(limit):
#     N = 0
#     while N<=limit:
#         yield N
#         N+=2
#
# EvenNums = Genrate_EvenNums(10)
# for x in EvenNums:
#     print(x)





#############-------######################--------::::::::::::::
#############-------######################--------::::::::::::::: Lambda
#############-------######################--------::::::::::::::

#lambda is an small anonymus fuction , takes any no.of arguments , only have 1 expression(+,-,*,/)
#:  you can reuse a lambda function by assigning it to a variable

# x = lambda a : a+10
# Y = lambda a,b : a+b
#
# print(x(5))
# print(Y(5,5))
# print(x(25))



#############-------######################--------::::::::::::::
#############-------######################--------::::::::::::::: Scope
#############-------######################--------::::::::::::::
# variable is only available inside the region where it is created , this is scope bcz variable belongs to the
# local scope of that function.
# mean if varibale or function is created inside an function , then trying to acess them outside the parent
# function , we wiil not get them , and error occurs.

#----------------: Local Scope
#
# def fun():
#     A = 200
#     if "1" == "1":
#         def Fun2():
#             print( "True" )
#         Fun2()
# fun()
#
# print(A) # error through hoga , thats scope
# Fun2()   # error through hoga , thats scope


#----------------: Global Scope
#variable created in  main body of   code is a global variable and belongs to the global scope and is
# available from within any scope, global and local.
#For example , constructor m jo self.Variable banate han , wo global scope ka hota , jider mrzi use krlo.

# x = 300
# def Fun():
#     print(x)
# Fun()

#----------------: Global Keyword
#If you need to create a global variable that can be used inside,outside the functions , use Global keyword
#syntax: global Variable_Name
#               Variable Value
# def Fun():
#     global x
#     x = 100
#     print(x)
# Fun()
# print(x)







#can change the value of any variable by specofying it global at other place , global value will be
# used then at every place.
# x = 50
# def fun():
#     global x
#     x= 20
# fun()
# print(x)


#-------> Non_Local <-------: The nonlocal keyword makes the variable belong to the outer function.
# def fun():
#     x= 20
#     def F2():
#         nonlocal x
#         x =25
#     F2()
#     return x  # 25 return hoga , as 25 ab function ke outside ke funs ka variable hogya ha.
#
# print(fun())



# #----------------------------------------------------------------> Is_Instance() <------------------------------------
#
# isinstance() is used to check that object belongs to which class or data type
# Syntax: isinstance(object , classinfo)
# object : var or value to check
# classinfo : data type or class , to compare against
# Returns True if object matches type otherwise false.
#
#-Example:-
# x = 10
# print(isinstance(x, int))   # True
# print(isinstance(x, float)) # False
# print(isinstance(x, str))   # False

#--> Checking againt tuple:
# print(isinstance(x , (float , str) ))   # false
# print(isinstance(x , (float , str , int) ))   # true


#-----> Why Use isinstance() Instead of type()?
#
# Handles Inheritance: isinstance() considers subclasses, while type() does not.
# Flexible: Allows checking against multiple types at once using a tuple.
#
#-- Example:-
#
# class Animal:
#     pass
#
# class Dog(Animal):
#     pass
#
# object = Dog()
#
# print(isinstance( object , Animal  )) True
# print(isinstance(object,Dog))         True
# print(type(object) == Dog )            True
# print(type(object) == Animal)         False  ,inherit bi ha phr bi false , so dont use it.
#
#
#------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------->  Map & Strip <----------------------------------------------------
#
# Map & Strip Function:---
# map function is used to apply a function to a iterable list or tuple and returns a map object , which is a iterator.--> map(function, iterable)
# strip removes any white spaces beginning or end of string.
# Example1:
#
# s = ['1','2','3']
# res = map(int,s)
# mapped = list(res)
# print(mapped) # [1, 2, 3]
# print(s)     # ['1', '2', '3']
#
#
# Example2:
# def fun(a, b):
#     return a + b
# x = map(fun, (1, 2, 3), (1, 2, 3))
# print(tuple(x))  # (2, 4, 6)
#
# Exp-3:-
# a = [1, 2, 3, 4]
# res = list(map(lambda x: x* 2 ,a))
# print(res)
#
#-Exp-4:-
# fruits = ['apple','banana']
# x = map(str.upper , fruits)
# print(list(x)) # ['Apple', 'Banana']

# Exp-4:-
#
# s = ['heloo ', '  python']
# res = list(map(str.strip , s))
# print(res) # ['heloo', 'python']
#

# Exp-4:-
# string = ['  ahsan        ']
# res = (string[0].strip())
# print(res) # 'ahsan'




#------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------->  Filter  <----------------------------------------------------

# Filter method filters any sequence with the help of an function that test each element to be true or not.
# The filter() function in Python filters elements from an iterable (like a list) based on a function (or None for truthy values)
# Syntax: filter(function, sequence)
# filter ke without hum print x krte han element ko show krne ke liye but with filter hum list ko use krte cnverion ke liye.
#returns filter object: <filter object at 0x00000183FD39ACB0> without list.
#
#-Exp1:-
# def even(n):
#     return n % 2 == 0
# a = [1,2,3,4,5,6]
# Even = filter(even , a)
# print(list(Even)) # [2, 4, 6]
#
#
# #-Exp2:-
#
# Filter_Odd = filter(lambda x: x%2!=0 , a)
# print(list(Filter_Odd)) # [1, 3, 5]




#------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------->  Eval()  <----------------------------------------------------



# Eval Function takes the  argument and evaluates it as python code and runs it.

# Syntax: eval(expression, globals=None, locals=None)
# expression = string is passed and evaluates as python expression.
# globals = dict to specify available global method,vars.
# locals =  Another dictionary to specify the available local methods and variables.


# expr = 'x*(x+1)*(x+2)'
# x = 5
# y = eval(expr)
# print(y)


# def Fun():
#      expr = 'x*(x+1)*(x+2)'
#      x = 5
#     Result = eval(expr, globals=None, locals=None)
#     print(Result)
# Fun()


# x= 5
# R1 = x + 0
# print(eval('not x is None')) # True
# print(eval('x is None')) # False
# print(eval('R1 == 5'))   # True
# print(eval('R1 != 5'))   # False
# print(eval('x%2==0'))    # False as 5 is odd not even



# Vulnerability issues with Python eval() Function
# We can get any function access by eval as eval will execute anything passed to it.
#
# def secret_function():
#     return '1234'
#
# def Eval():
#     result = eval( secret_function() )
#     print(f'Result: {result}')
#
# Eval()


# --- Making eval() safe  ---:
# Setting {"__builtins__": None} inside eval() disables Python’s built-in functions and modules, preventing the execution of potentially dangerous code.
# can make it safe by using an dictionary and passing variable , functions that should be acessed inside it and caling any by passing in expr.
# Exp-1:-
#
# def Secret_Function():
#     return 'Secret Key 911'
#
# def Evaluate_Fun():
#     safe_dict = {'x':5}
#     expr = 'x*2'
#
#     result = eval(expr, {"__builtins__": None}, safe_dict)
#     print(f"Result: {result}")
#
# Evaluate_Fun()



#---Exp-2:-

# def secret_function():
#     return "Secret Key 911"
#
# def evaluate_fun():
#     safe_dict = {"x": 5, "secret_function": secret_function}   # Added function
#     expr = "secret_function()"  # Now eval can find it
#
#     result = eval(expr, {"__builtins__": None}, safe_dict)
#     print(f"Result: {result}")
#
# # evaluate_fun()

#- Exp-3:-

# def secret_function():
#     return "Secret Key 911"
#
# def evaluate_fun():
#     safe_dict = {"x": 5}
#     expr = "secret_function()"
#
#     result = eval(expr, {"__builtins__": None}, safe_dict)
#     print(f"Result: {result}")
#
# evaluate_fun()   # NoneType' object is not subscriptable : as sec_fun not added in dict.







#------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------->  Any()  <----------------------------------------------------





# Python Any Function returns true if any of the iterables are true as 1,true or other ,
# returns false if false or 0 or empty string or list,dict,set,tuple. in dict it check keys not vals.
#
#-------------------------------- Exp-1:-
# testing_any = any([0,True,0])
# print(testing_any)   # True

# testing_any = any([False]) # False
# testing_any = any([]) # False
# testing_any = any( ()  ) # False

# string_test = 'Hy' # True
# string_test = '' # False

#------------------------------- Exp-2:-

# List = [1,2,3,4,5]

# res = any(item > 2 for item in List)
# print(f'Res: {res}') # True

# # this function gives same result as built-in any() function
# def Customr_Any():
#     for x in List:
#         return True
#     return False
# print(Customr_Any()) # True












#------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------->  All()  <----------------------------------------------------
# The Python all() function returns true if all  items of  iterable (List, Dictionary, Tuple, set, etc.) are True
# otherwise it returns False. It also returns True if the iterable object is empty.
#
# Why To Use?
# Sometimes working on some code if we want to ensure that user has not entered a False value then we use the all() function.

# testing_all = [4,5,1]
# print(all(testing_all)) # True

# testing_all = []
# print(all(testing_all)) # True , on empty but not on false

# testing_all = [False]
# print(all(testing_all)) # False

# testing_all = [4,5,33]
# print(all(x > 5 for x in testing_all)) # False , as all are not greater then 0
# print(all(x > 0 for x in testing_all)) # True , as all are greater then 0
# print(all(x%2==0  for x in testing_all)) # False
# print(all({0: 22 , 1: 22})) # False


# s = '000'
# print(all(s)) # True




#--------------------------------------- Split -------------------------------------#


# Split Method splits the string into list , we can specify the separator but default separator is whitespace
# max split : optional ,specifies how many splits we want , default val -1 mean all.its index val.


# # Default Separator
# String = 'Ahsan Khan'
# Split = String.split()
# print(Split) # ['Ahsan', 'Khan']

#------

# String = 'hello, my name is Peter, I am 26 years old'
# Split =  String.split(' ',1)
# print(Split) # ['hello,', 'my', 'name is Peter, I am 26 years old']  2 means index , that why 3 occurs.

#--------------------------------------- Join -------------------------------------#

# Join takes the elements in iterable form and joins them in 1 list using any thing inside '' called separator and returns values as strings.
# takes the keys as default in dictionary.
# Note: If the key of the string is not a string, it raises the TypeError exception.---> Dict
#
# Tuple = ('john','peter')
# x = ''.join(Tuple)
# print(x) # johnpeter


# Dict = {'name': 'Pak' , 'Country': 'Pacific'}
# x = ''.join(Dict)
# print(x) # nameCountry


# Dict = {'name': 'Pak' , 'Country': 'Pacific'}
# x = ''.join(Dict.values())
# print(x)



# -------------------------: Sorted :----------------------------------------
# sorted function returns the sorted list of iterable object.can specify ase or desc order ,
# strings are sorted alphabeticly and numbers numerically.we can not sort both abc,123 at a time.
# Returns an list of sorted vals. tuple dont have sort so we use sorted.
# Syntax:-----------            Sorted(iterable,key=key,reverse=True)


# A = ('1111','24','755','43345')
# Sort = sorted(A,reverse=False)
# print(Sort)

# Sort = sorted(A,key=len)
# print(Sort)   # ['24', '755', '1111', '43345']  : only for str not int.

# Exp-2--------------:
# List ke ander dictionary ko hum .get('') krKe access krte han.

# Bikes = [
#     {'model':'Yamaha 100', 'price':200},
#     {'model': 'Suzuki 110', 'price':450},
#     {'model':'Honda 70', 'price':100}
# ]
# Sort = sorted(Bikes , key=lambda x : x.get('price'))
# print(Sort)


# -------------------------------: Zip :-------------------------------------------
# it takes tuples of iterable object as input and 1st items of each iterable are paired together.
# returns an zip object by converting it to tuple at last.
 # -------: zip(iterator1, iterator2, iterator3 ...)

# A = ('asn','Mr')
# B = ('khan','ism')
# Zip = zip(A, B)
# print(tuple(Zip)) # (('asn', 'khan'), ('Mr', 'ism'))


# Looping: Return greater element in each tuple.
# l1 = [111,22,33]
# l2 = [11,22,333]
#
# for x in zip(l1, l2):
#     print(max(x)) # returns 1 element form tuple which is greater.









