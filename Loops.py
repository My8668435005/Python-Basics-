#used to repeat instructions
#while loop

count = 1

while count <= 5:
    print("hello")
    count += 1

#print the number from 1 to 100 
print("print the number from 1 to 100 ")

i1 = 0
while i1 <= 100:
    print(i1)
    i1 += 1


#print the numbers from 100 to 1

print("print the numbers from 100 to 1")

i2 = 100
while i2 >= 1:
    print(i2)
    i2 -= 1


#print the multiplication table of a number n

# n = int(input("enter the num : "))
# num = 1
# print("table of ", n)
# while num <= 10:
#     print(n*num)
#     num += 1


#print the element of the following list using a loop
# [1,4,9,16,25,36,49,64,81,100]

print("print the element of the following list using a loop - [1,4,9,16,25,36,49,64,81,100]")
num = [1,4,9,16,25,36,49,64,81,100]
idx = 0
while idx < len(num):
    print(num[idx])
    idx += 1
    

#search for a number x in this tuple using loop


# print("search for a number x in this tuple using loop")
# print("(1,4,9,16,25,36,49,64,81,100)")

# tuple = (1,4,9,16,25,36,49,64,81,100)

# x = int(input("enter num for search : "))
# i = 0
# while i < len(tuple):
#     if x == tuple[i]:
#         print("found at ",i)
#         break
#     else:
#         i += 1
    

#-------------------------------------------------------------------------------------------------------------------------------------

#break and continue keyword 
    
print("using continue keyword")
a = 0
while a <= 5:
    if (a == 3):
        a += 1
        continue #skip the three
    print(a)
    a += 1

#---------------------------------------------------------------------------------------------------

#for loop

#loop's are used to travers sequential mannar for list string tuple


print("printing element's using for loop")
l = [1,2,3,4,5,6,7,8]  #we can use tuple

for el in l:
    print(el)

#also for string 

print("printing charecters of string 'manish using for loop'")
str = "manish"
for char in str:
    print(char)

#search for an number in this tuple using for loop

# tpl = [1,4,9,16,25,36,49,64,81,100]

# x1 = int(input("enter searching number : "))

# for i in tpl:
#     if (x1 == i):
#         print("found ! ")
#         break
    

#Range function

#range(5) = 0,1,2,3,4
#step size 
#range(start,stop,step) 

print("printing sequence using range function")
for i in range(2,10,2):
    print(i)


#pass use to null statement that return nothing

for i in range(5):
    pass

#practice quetion's 

#write a program to find the sum of first n natural number (using while loop)
print("write a program to find the sum of first n natural number")
n = 5
sum = 0
for i in range(1,n+1):
    sum += i

print("total sum : ", sum)
    

#write a program to dind the factorial of first n numbers (using for loop)

n1 = 5
fact = 1
for i in range(1,n1+1):
    fact *= i
print("factorial is : ", fact)