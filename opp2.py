#private attribute and methods

#public - access outside the class
#private - access only under class

class Account:
    def __init__(self,bal,password):
        self.balance = bal
        self.__password = password

s1 = Account(1000,12344)
print(s1.balance)
# print(s1.__password) #it occurs error because it is private variable 
                     # we can not use outside the class
                     #we can create private variable by giving "__" before the 


#define private method 
class Person:
    def __hello():
        print("hello")

p1 = Person()
# p1.__hello    - it gives error 



#------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#inheritance
#when one class derives the propeties and methods of another class (parents/base)

class Car:
    @staticmethod
    def start():
        print("car started...")

    @staticmethod
    def stop():
        print("car stoped...")


class toyotaCar(Car):
    def __init__(self,name):
        self.name = name

car1 = toyotaCar("fotuner")
car2 = toyotaCar("prius")

print(car1.start())
 


#multiple inheritance
#single inheritence
#multi level 


#Super method

class car:
    def __init__(self,type):
        self.type = type
        
    @staticmethod
    def start():
        print("car started...")

    @staticmethod
    def stop():
        print("car stoped...")


class toyotaCar(car):
    def __init__(self,name,type):
        super().__init__(type)
        self.name = name
         
car1 = toyotaCar("fotuner","electric")
print(car1.type)



#class methods

#it is the concept of changing class attributes 

class Persons:
    name = "krushna"

    # def changeName(self,name):
        # Persons.name = name           #it change the attribute of class directly
        # self.__class__.name = name    #also do this

#we use "@classmethod" keyword 
#in this method we dont have self 
#at the place of "self" object we class object first as attribute
    @classmethod  #decorator
    def changeName(cls,name):
        cls.name = name
    

p1 = Persons()
p1.changeName("manish")
print(p1.name)
print(Persons.name)




# @property decorator

# we use @property decorator on any method in the class to use the method as a property
 

# class std:
#     def __init__(self,phy,chem,math):
#         self.phy = phy
#         self.chem =chem
#         self.math =math
#         self .percentage = str((self.phy+self.math+self.chem)/3) + "%"

# stud1 = std(86,98,68)
# print(stud1.percentage)

# stud1.phy = 66
# print(stud1.phy)
# print(stud1.percentage)  #the problem with this is percentage remains same


# that s why we use "@property" method
#that convert the function into a attribute of class 

class Std:
    def __init__(self,phy,chem,math):
        self.phy = phy
        self.chem =chem
        self.math =math
    @property
    def percentage(self):
        return str((self.phy+self.math+self.chem)/3) + "%"

std1 = Std(86,98,68)
print("old percentage: ",std1.percentage)

std1.phy = 66
print("new marks of phy : ",std1.phy)
print("new percentage: ",std1.percentage) #in this we call for an function but "@property" method return the attribute 


#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# Plymorphism : operator overloading
#when the same operator is allowed to have different meaning according to the context

#operator and Dunder function

# a+b # addition a.__add__(b)

class complex:
    def __init__(self,real,imaginory):
        self.imaginory = imaginory
        self.real = real

    def shownum(self):
        print(self.real,"i +",self.imaginory," j")

    def __add__(self, num2):  #when we call "+" that take two parameter befor and after him that are two complex numbers
        newReal = self.real + num2.real
        newimg = self.imaginory + num2.imaginory
        return complex(newReal,newimg)

num1 = complex(3,4)
num1.shownum()

num2 = complex(4,5)
num2.shownum()

num3 = num1 + num2
num3.shownum()


#----------------------------------------------------------------------------------------------------------------------------------------------------

print("----------------------------practice question 1------------------------------------------")


#practice question 1
class circle:
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return (22/7) * self.radius ** 2
    
    def perimeter(self):
        return 2 * (22/7) * self.radius
    
crl1 = circle(21)
print("area: ",crl1.area())
print("perimeter : ",crl1.perimeter())



#practice question 2
print("----------------------------practice question 2------------------------------------------")
class Employee:
    def __init__(self,role,dept,salary):
        self.role = role
        self.dept = dept
        self.salary = salary

    def showDetails(self):
        print("role : ",self.role)
        print("dpt : ",self.dept)
        print("salary : ", self.salary)

class Engineer(Employee):
    def __init__(self, name , age):
        self.name = name
        self.age = age
        super().__init__("Engineer", "IT","75000")

eng1 = Engineer("manish",21)

eng1.showDetails()
        


print("---------------------------- practice question 3 ------------------------------------------")

class order:
    def __init__(self,item,price):
        self.item = item
        self.price = price

    def __gt__(self, ord2):
        return self.price > ord2.price
    

ord1 = order("chips",20)
ord2 = order("tea" , 15)

ord3 = ord1 > ord2
print(ord3) 
