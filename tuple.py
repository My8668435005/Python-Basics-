#tuple are immutable sequence of value

tup = (2,3,5,6)
print(type(tup))
print(tup[3])

#empty tuple
tup1 = ()

#single value tuple
tup2 = (1,) #WE HAVE TO ASSIGN ","
print("single value tuple: ",tup2)



#-----------------------------------------------------------------------------------------


#methods in tuple

#find index or time of element

print("index :",tup.index(2)) 
print("count: ", tup.count(2))



#------------------------------------------------------------------------------

#practice question

#write a program to ask the user to 3 movies as a string and make list of them 

# print("enter your 3 mouies")
# mov1 = input("enter mov1: ")
# mov2 = input("enter mov2: ")
# mov3 = input("enter mov3: ")

# movList = []

# movList.append(mov1)
# movList.append(mov2)
# movList.append(mov3)
# print("List of movies: ",movList)

#----------------------------------------------------------------------------------------------------



#practice question 2 

#check palindrom of list

print("check palindrom of list:")
list1 = [1,2,1]
print(list1)
list2 = [1,2,3]

copy_list1 = list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):
    print("palindrom")
else:
    print("not palindrom")


#--------------------------------------------------------------------------------
#practice question 3

#write a program to count the number of student with grade "A" in the following tuple = ["C","D","A","A","B","B","A"]

tuple = ("C","D","A","A","B","B","A")
std = tuple.count("A")
print("no of std are having A grade: ",std)

#store the abouve value in a list and sort them form "A" to "D"
list = ["C","D","A","A","B","B","A"]
list.sort()
print("sorted list : ", list)


