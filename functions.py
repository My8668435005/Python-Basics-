#function - it is block of statement that perform a specific task

def sum(a,b):
    print("sum is :",a+b)
    return "addition is done"

sum(2,3)  #function call

sum = sum(6,7)
print(sum)

#default parameters 
def sub(a= 3,b=1):
    print("sub is: ",a-b)

sub()


#------------------------------------------------------------------------------------

#wt function print the length of list

list = [2,3,4,5,5,6,7,5,3,6,3]

def list_len(lst):
    print("items of list: ",end="")
    for i in lst:
        print(i,end="  ")
    
    print("length is :",len(lst))

list_len(list)

#wtf to find the factorial of n (n is the parameter)

def fact(f):
    for i in range(1,f):
        f += i      #1+2+3
    print("fact is :",f)

fact(3)   


#wtf to convert USD to INR

def Converter(USD_val):
    inr_val = USD_val * 83
    print("INR val is of ", USD_val," :", inr_val )

Converter(9)
 
#----------------------------------------------------------------------------------------------------------------------------------

#Recursion 
#when a function call itself repeatedly

#it use call stack  

#print n to 1 
print("print n to 1  using recursion")
def show(n):
    if (n == 0):
        return
    print(n)
    show(n-1)
    
show(5)

#factorial using recursion

def fact(n):
    if(n == 0 or n == 1):
        return 1
    else: 
        return n * fact(n-1)
    
print("factorial is :" ,fact(4))


#write a recursive function to calculate the sum of first n natural number

def cal_sum(n):
    if(n == 0):
        return 0
    print(n)
    return cal_sum(n-1) + n

print("total sum is :",cal_sum(5))



#write a recursive function to print all element in a list
list = [2,4,4,53,5,3,5,2,45]

def prt_list(inx,list):
    if(inx == len(list)):
        return 
    print(list[inx])
    prt_list(inx+1,list)

print("element of list is : ")
prt_list(0,list)
