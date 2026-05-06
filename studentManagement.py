#student management system that can perform operations like add , delete, update , display using dictionory

#student class
class student:
    def __init__(self,roll_no, name , course):
        self.roll_no = roll_no
        self.name = name
        self.course = course

    def __str__(self):
        return f'roll no : {self.roll_no}, name : {self.name} , course : {self.course}'
    
#manager 
class manager:
    def __init__(self):
        self.students = {}  #dictionory

    #add student 
    def add_std(self, roll_no, name, course):  
        if (roll_no in self.students):    #check if it exist already exist in dictionory
            print("student is already exist")
        else:
            self.students[roll_no] = student(roll_no,name,course)   # if not then add it to dictionory
            print("student added succesfully !!")


    #delete student
    def del_student(self,roll_no):   
        if roll_no in self.students:  #if exist then delete
            del self.students[roll_no]   #using " del " keyword we can delete the record in dictionory
            print("student deleted !!")
        else :
            print("roll number not exist !!")


    # update student 
    def update_std(self,roll_no , name =  None, course = None):   
        if roll_no in self.students:  
            self.students[roll_no].name = name
            self.students[roll_no].course = course
            print("updated succesfully !!")
        else:
            print("record not exist !!")
        
    #display all students
    def display_all(self):
        if not self.students:
            print("no record exist !!")
        else:
            for i in self.students.values():  # "value" keyword returns the all key and value pair of dictionory
                print(i)

    

#creating object of manger() class
manage = manager()

#adding a student
manage.add_std(1,"manish","python")
manage.add_std(2,"krushna bankar","java")

#updating a student
manage.update_std(1,"manish bagul","android dev")

#display all students
manage.display_all()



        
        