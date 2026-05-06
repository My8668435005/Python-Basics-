#python can be used to perform operation on a file (read and write data)

#type of files -
# 1. text file: .txt , .docx ,.log
# 2. Binary file : mp4 , .mov ,.png ,.jpeg etc


# f = open("python/demo.txt","a")  # open for only read "r"

# f.write("\n i want to learn javascript")
#  #we have to close the file 
# f.close()


# 'r' - open for reading 
# 'w' - open for writing , truncating the file first
# 'x' - create a new file and open it for writing 
# 'a' - open for writing , appending to the end of the file if it exist
# 'b' - binory mode
# 't' - text mode 
# '+' - open a disk for updating (reading and writing)


# d = open("python/demo.txt",'r+')     # using r+ we can read and write both
# d.write("my name is manish bagul")
# print(d.read())
# d.close()




#with proper syntax

# with open("python/demo.txt",'r') as f:
#     data = f.read()
#     print(data)

# with open("python/demo.txt",'w') as f:
#     f.write("new data")





#deleting a file
#using os module

#modeule is a fiel written by another programmer that generally has a function we can use
#import os
#os.remove(filename)

import os

# os.remove("python/demo.txt")

#practice question's

#create a new
#create a new file "practice.txt" using python . add the following data in it:
#hi everyone 
#we are learning file i/o

# with open("practice.txt",'w') as f:
#     f.write("hi everyone")
#     f.write("\nwe are learning file i/o")
#     f.write("\nusing java")
#     f.write("\ni like programing in java")
#     f.close()

# with open("practice.txt",'r') as f:
#     data = f.read()


# new_data = data.replace("java", "python")
# print(new_data)


# with open("practice.txt",'w') as f: 
#     f.write(new_data)



#practice question's
#search if the word "learning" exist in the file or not

# word = "learning"
# with open("practice.txt",'r') as f:
#     data = f.read()
#     if(data.find(word) != -1):
#         print("found")
#     else:
#         print("not found")


#from a file containing number separeted by comma , print the count of even numbers.
count = 0
with open("practice.txt","r") as f:
    data = f.read()
    print(data)

    nums = data.split(",")
    for val in nums:
        if(int(val) % 2 == 0):
            count += 1

print(count)