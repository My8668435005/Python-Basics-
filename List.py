
#create list

marks = [93.4,87.5,47.6]
print(marks)
print(type(marks))

#print using index
print(marks[0])


#store multiple type of data
student = ["manish",21,"nashik"]
print("student detail stored in list: ", student)

#List are muttable 
#strings are immutable

student[0] = "manish bagul"
print(student[0])
print("changed name: ",student)


#slicing in List 
print("slice : ",marks[1:2])  #1 to 2-1
print("slice to end : ", marks[1:]) #automatically considered to end
print("slice from begin:",marks[:2]) #automatically considered form 0

#------------------------------------------------------------------------------------------------------------------

#method's of List 

list = [2,1,3]

#append method
list.append(4)
print("appended list : ",list)

#sort method
#ascending sorting by default
list.sort()
print("sorted list: ",list)

#descending 
list.sort(reverse=True)
print("descending : ",list)

#sorting can be perform on strings
Alfa = ['a','c','d','b']
Alfa.sort()
print("String sorting: ", Alfa)

#insert method
list.insert(2,5)
print("insert element: ",list)


