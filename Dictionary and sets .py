#Dictionory - used to store data in the form of key value pair value 

#dictionory is muttable
#dont allow duplicate

#syntax - dic_name = { "key_name" : "value"}

info ={ 
    "name" : "manish", #string
    "subject" : ["python","c++","java"], #list 
    "topics":(4,5,7,8), # tuple
    "age": 21, #integer
    "marks": 93.4, #float
    1 : 2,
    "is_adult":True, #Boolean
}


#access value of dictionory
#dict["key_name"]
print("name :" ,info["name"])
print("age : " , info["age"])


#assign value to key
#dict["key_name"] = "value"
info["name"] = "manish bagul"
print("new name: ",info["name"])

#add new key value
info["father_name"] = "yadav"
print("father name: ",info["father_name"])


#empty dictionory
emt_dic = {}


#nested dictionory
student ={
    "name":"manish bagul",
    "subject": {
        "phy":89,
        "chem":98,
        "bio":99
    }
}

print("student: ",student)
print("student - subject: ",student["subject"])
print("student - subject - phy:",student["subject"]["phy"])


#method of dictionory

# mydict.keys() - return all keys
# mydict.values() - return all Value
# mydict.items() - return all (key,value) pair as tuple
# mydict.get("key") - return the key according to value
# mydict.update(newdict) - insert the specific item to the diction


# all keys 
print("all keys",student.keys()) #bydefault it return tuple

# we typecast to list
print("all keys in list form: ",list(student.keys()))

# return collection of values
print("values :",list(student.values()))

#items method return all pair of key value
print("itmes: ", list(student.items()) )

#we also access specific pair
pair = list(student.items())
print(pair[0])

#get method return value on the basis of key
print("value of key name: ",student.get("name"))

#update method add new key value 
new_dic = {"city":"nashik", "state": "maharastra"}
student.update(new_dic)
print("new dictinory: ",student)







#------------------------------------------------------------------------------------------------------------------


#set in python 
#set is the collection of unodered items
#each element in the set must be unique and immutable
#we can not store list and dictionory in set
#we can store tuple in set

collection = {1,2,3,4,"manish","bagul"}
print("set : ",collection)

#it ignore duplicate values
#same value considered as one

#empty set
collection1 = {} #this is dictionory

#we have to use set propety
collection2 = set()

#methods of set 

#add 
collection2.add(2)
collection2.add(3)
collection2.add(1)
collection2.add(2)
collection2.add((1,2,3))
collection2.add("manish")
print("collection2 : ",collection2)

#remove
collection2.remove(2)
print("collection2 : ",collection2)


#clear method used to clear set
collection2.clear()
print("collection2 : ",collection2)

#union method 
collection.union(collection2)
print("union of set: ", collection)

#also intersections
collection.intersection(collection2)
print("intersection value: " , collection)



#----------------------------------------------------------------------------------------------------------------------
#practice questions 



#store the following words meaning in a pyhton dictionory
#table : "a piece of furniture " ,"list of fact and figure"
#cat: "a small animal"

dic1 = {
    "table":["a piece of furniture","list of facts and figures"],
    "cat":"a small animal"
}
print(dic1["table"])


#practice question

#find total number of class room for each subject
#"python","python","python","javascript","java","java","java","c++","c++","c"

subject ={
    "python","python","python","javascript","java",
    "java","java","c++","c++","c"
}

print("total num of class room :" , len(subject))



#practice question

#write a program to enter marks of 3 subjects from the user and store them in a dictionory 
#start with an empty dictionory and add one by one . use subject name as key and marks as value


mark1 = int(input("enter math marks :"))
mark2 = int(input("enter eng marks :"))
mark3 = int(input("enter hindi marks :"))

marks_dic = {}

marks_dic["math"] = mark1
marks_dic["eng"] = mark2
marks_dic["hindi"] = mark3

print("subject and marks : ", marks_dic)



#practice question 

#figure out a way to store 9 to 9.0 as seperate value in the set 
#(you can take help of built in data type )
value = {("float",9.0),("int",9)} #we can store 
print(value)

