
#  print("welcome") # indentation error
# print(123+'abc') # type Error
# print(int("hello")) # Value Error
#print(10/0) # ZeroDivision Error
#print(name) # name error

#l=[1,2,3]
#print(l[4])


# try:
#     a=5
#     b=0
#     print(a/b)
#    # print("welcome")
# except:
#     print('Some error occurred.')
# print("Out of try except blocks.")

# try:
#     a=5
#     b=0
#     print(a/b)
# except TypeError:
#     print('Unsupported operation')
# print ("Out of try except blocks")

# try:
#     a=5
#     b=0
#     print (a/b)
# except TypeError:
#     print('Unsupported operation')
# except ZeroDivisionError:
#     print ('Division by zero not allowed')
# print ('Out of try except blocks')



# try:
#     print("try block")
#     x=int(input('Enter a number: '))
#     y=int(input('Enter another number: '))
#     z=x/y
# except ZeroDivisionError:
#     print("except ZeroDivisionError block")
#     print("Division by 0 not accepted")
# else:
#     print("else block")
#     print("Division = ", z)
# finally:
#     print("finally block")
#     x=0
#     y=0
# print ("Out of try, except, else and finally blocks." )


try:
    x=int(input('Enter a number upto 100: '))
    if x > 100:
        raise ValueError(x)
except ValueError:
    print(x, "is out of allowed range")
else:
    print(x, "is within the allowed range")



# file Handling

f = open("t1.txt","r")
for line in f:
    print(line)


f = open("t1.txt","r")
line = f.read(4)  # read only 4 characters
print(line)
f.close()

# With Open Block -

with open ("t1.txt","r") as f:
    l= f.read()
    print(l)


with open("t1.txt","r") as f:
    data = f.readlines()
    for l in data:
        word = l.split()
        print(word)


with open("t1.txt","r") as f:
    f.seek(4)         # seek function file pointer at specific position
    print(f.tell())  # tell function print file pointer position
    l= f.read()
    print(l)


f = open("t1.txt","a") # here you can change file mode means
f.write("This is new contents ")
f.write("file handlingn ")
f.write("This is last line")
print("content added")
f.close()


f = open("t1.txt","r+")
f.write("welcome to spark")
f.seek(0)
l= f.read()
print(l)


# read any string from console and add this string in file

val = input("enter string")
f = open("t1.txt","r+")
f.write(val)
f.seek(0)
l=f.read()
print(l)





