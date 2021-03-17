a=5
b=5.6
c=3+6j
print(type(a))
print(type(b))
print(type(c))
s1="hello python"
s2='am njoroge samson'
s3="'iam a programmer'"
print(s1)
print(s2)
print(s3)
print(type(s1))
print(type(s2))
print(type(s3))
#escape sequence 
m="python\\"
print(m)
n="py\nthon"
print(n)
#accessing charactersin using string 
h="samsonmwangi"
print(h[1])
print(h[5])
print(h[8])
print(h[1:8])
print(h[6:10])
print(h[0:5:6])
#string operations addition,multiplacation,replacement and lowercase and uppercase operations
a="45"
b="55"
print(a+b)
a="samson"
b="mwangi"
print(a+b)
#multiplication in string
a="samson"
b=3
print(a*b)
#spliting values from the string
s="samson mwangi njosh"
print(s.split(' '))
#replacing values in a string
s="samson mwangi"
print(s.replace('samson','njoroge'))
#using upper and lowercase in strings
s="samson"
print(s.upper())
s="MWANGI"
print(s.lower())
#list method using strings
animals=['cat','cow','donkey','zebra' ,'lion']
print(animals)
#adding an item in a list
animals.append('fish')
print(animals)
#removing an item from a list
animals.remove('donkey')
print(animals)
#inserting an item in a list in a specific location
animals.insert(1,'human')
print(animals)
#removing and displaying removed item fron the list
print(animals.pop())
print(animals)
#list sort
list1=['23','33','43','53','63']
list1.sort()
print(list1)
#list.reverse
list1.reverse()
print(list1)
#tuples in python
t=(1,['2','3','4'],"python")
print(t)
print(type(t))
#tuple idexing
t=('1','3','4','67')
print(t[2])
print(t[0])
print(t[3])
#creating dictionaries in pyhton
x={'food':'githeri','society':'gikuyu', 'quantity':'2','color':'pink'}
x2=dict(food='githeri',society='gikuyu', quantity='4', color='pink')
x3=dict([("food","githeri"),("society","gikuyu"),("quantity","4"),("color","pink")])
print(x)
print(x2)
print(x3)
#data assignment
a=['2','3','5','8']
b=a #assign a to b
b[0]=99
print(a)
#shallow copy
a=['2','3','6','9','[5, 7, 8]']
b=a.copy()#shallow copy
print(a)
#operators
a=10
a+=1
print("a+=1",a)
a-=1
print("a-=1",a)
a*=2
print("a*=2",a)
a/=2
print("a/=2",a)
#comperition operation
print(1>=2)
print(1<=2)
print(1!=2)
print(1==2)
#logic operations
True or False
True and False
not True
not False
#identity operators
a=20
b=30
c=a
print(a is b)
print(a is c)
print(b is not c)
print(a==b==c)
d = {
        "john":40, 
         "peter":45
        } 
print(d["john"])