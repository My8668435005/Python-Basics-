#oop (object oriented programing) 
#to map with real world scenarions ,we started using objects in code
#this is called oop


#class and object's

#class is a blue print for creating objects

#creating class


class class_name:
    var_name = "manish"

#creating object's

s1 = class_name()
print(s1.var_name)



#---------------------------------------------------------------------------------------------------------------------------------------------------------


#init function 
#constructor - 
# all classes have a function called _init_() , which is always executed when the class is being initiated

class student:

    def __init__(self,fullname):  #parameterized constructor
        self.name = fullname
        print("adding new student..",self.name)


s2 = student("manish bagul")
print(s2.name)




#class and instance attribute
# class.attr
#obj.attr

#methods (functions)
#methods are functions that belong to object

class std:
    def __init__(self,fullname,marks):
        self.name = fullname
        self.marks = marks

    def wellcome(self):
        print("wellcome students",self.name)

    def get_marks(self):
        return self.marks


s3 = std("manish bagul",99)
s3.wellcome()
print("marks -",s3.get_marks())


#practice questions

#create student class that take name and marks of 3 subject as argument in cunstructor
#then create a method to print the average

class sub_mark:
    def __init__(self,name1,name2,name3,marks1,marks2,marks3):
        self.sub1 = name1
        self.marks1 = marks1
        self.sub2 = name2
        self.marks2 = marks2
        self.sub3 = name3
        self.marks3 = marks3

    def avg(self):
        sum = self.marks1+self.marks2+self.marks3
        total_avg = sum/3
        print("average is : ",total_avg)

s4 = sub_mark("eng","phy","math",99,78,97)
s4.avg()

#we can also use list 




#static method
#method that dont use the self parameter (work at class level)

#decorator @staticmethod

#important



#Abstraction 
#hiding the implementetation details of a class and only showing the essential feature to the user



class car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False
    
    def start(self):
        self.acc = True
        self.clutch = True
        print("car is strating....")


c1 = car()
c1.start()   #there is no background process how car is started 
             # it is only the object we call and car started



#encapsulation 
#wrapping data and functions into a single unit (object)



#practice questions 
#create Account class with 2 attribute - balance and account no
#create method for dibet, credit and priting the balance

print("--------------------Banking application -------------------------")

class Account:
    def __init__(self,bal,acc):
        self.balance = bal
        self.account = acc

    def debit(self,amount):
            self.balance =- amount
            print("Rs.",amount," was debited...")

    def creadite(self,amount):
            self.balance += amount
            print(amount, "is creadited ")

    def show_bal(self):
            print("total balance is: ",self.balance)


        
acc1 = Account(100000, 1234)
acc1.creadite(100)
acc1.show_bal()



#del keyword
#used to delete object properties or object itself

#del s1.name
#del s1









