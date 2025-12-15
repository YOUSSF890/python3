print("hello pythone with youssef")


print("\n---------------------------\n")
# ---------------------------------
# what is type()
# All Data in python is Object
# ---------------------------------

print(type(10)) # int
print(type(-100)) # int
print(type(10.201)) # float
print(type("youssef")) # string
print(type([1,2,5,8])) # list
print(type((1,2,3,4,5,10))) # tuple
print(type( {"one" : 1 ,"tow" : 2} )) # dict => dictionary
print(type(2 == 2)) # bool => boolean --> true folst   

print("\n---------------------------\n")

Myvaryble = "youssef is good\n"
Age = 20
print(Myvaryble)
print(Age)

print("\n---------------------------\n")
# Concatenation

name1 = "YOUSSEF"
name2 = "LAGZOULI"
print(name1 + " " + name2)

#string

mystring ="youssef lagzouli"

print(mystring[0])  #==> y
print(mystring[2])  #== >u
print(mystring[-1]) #==> i

#Slicing (Access Multiple Sequence Items)
# [Start:End] End Not Included
# [Start:End:Steps]

print(mystring[3:7]) # print -> ssef
print(mystring[:6]) # print -> yousse

print(mystring[3::2]) # print -> se azui


#-------------------------------------
#---------- Srtings Methods-----------
#-------------------------------------

# strinp() rstrip() lstrip()

a = "    I Love Python   "
print(a.strip())
print(a.rstrip())
print(a.lstrip())

print("\n---------------------------\n")

a = "##########I Love Python#####"
print(a.strip("#"))
print(a.rstrip('#'))
print(a.lstrip('#'))

print("\n---------------------------\n")

a = "###n##I Lnove Pytn#hon#n##n##"
print(a.strip("#n"))
print(a.rstrip('#n'))
print(a.lstrip('#n'))
print("\n---------------------------\n")

# title()

b = "I Love 2d Graphics and 3G technology and python"
print(b.title())
print("\n---------------------------\n")

#capitalize()

b = "I Love 2d Graphics and 3G technology and python"
print(b.capitalize())
print("\n---------------------------\n")

# zfill

a,b,c,d = '1','11','111','1111'

print(a)
print(b)
print(c)
print(d)
print("\n---------------------------\n")
print(a.zfill(3))
print(b.zfill(3))
print(c.zfill(3))
print(d.zfill(3))
print("\n---------------------------\n")

#upper()

g = "Youssef"
print(g.upper())
print("\n---------------------------\n")

# lower()

g = "YOUSSef"
print(g.lower())
print("\n---------------------------\n")

# split() rsplit()

a = "I Love Python and PHP"
print(a.split())
print("\n---------------------------\n")

a = "I-Love-Python-and PHP"
print(a.split("-"))
print(a.rsplit("-"))
print("\n---------------------------\n")

a = "I-Love-Python-and-PHP"
print(a.split("-",2))
print(a.rsplit("-",2))
print("\n---------------------------\n")

#center()

e = "Osama"
print(e.center(9))
print(e.center(9,'@'))
print("\n---------------------------\n")

#count()
a = "I Love Python and PHP and PHP and "
print(a.count("PHP"))
print(a.count("PHP",0,23))
print("\n---------------------------\n")

# swapcase()

a = "I Love Python"
b = "i lOVE pYTHON"
print(a.swapcase())
print(b.swapcase())
print("\n---------------------------\n")

# startswith()

h = "I Love Python"
print(h.startswith("I"))
print(h.startswith("S"))
print(h.startswith("P",7,12))

print(h.endswith("n"))
print(h.endswith("S"))
print(h.endswith("e",2,6))