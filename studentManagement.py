class student:
    def __init__(self,roll_no, name , course):
        self.roll_no = roll_no
        self.name = name
        self.course = course

    def __str__(self):
        return f'roll no : {self.roll_no}, name : {self.name} , course : {self.course}'
    

class manager:
    def __init__(self):
        self.students = {}

    def add_std(self, roll_no, name, course):
        if (roll_no in self.students):
            print("student is already exist")
        else:
            self.students[roll_no] = student(roll_no,name,course)
            print("student added succesfully !!")

    def del_student(self,roll_no):
        if roll_no in self.students:
            del self.students[roll_no]
            print("student deleted !!")
        else :
            print("roll number not exist !!")

    def update_std(self,roll_no , name =  None, course = None):
        if roll_no in self.students:
            self.students[roll_no].name = name
            self.students[roll_no].course = course
            print("updated succesfully !!")
        else:
            print("record not exist !!")
        

    def display_all(self):
        if not self.students:
            print("no record exist !!")
        else:
            for i in self.students.values():
                print(i)

    

    
manage = manager()
manage.add_std(1,"manish","python")
manage.add_std(2,"krushna bankar","java")
manage.update_std(1,"manish bagul","android dev")

manage.display_all()



        
        