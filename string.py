### STRINGS


b = "mangoes "
a=' 12'

print(a+b)
print (a<b)
print(a>b)
print (b*2)

#PRINTING a string with an apostrophe

print('This is a string\' with an apostrophe ')

num1='20'
num2='21'

sum1=(num1+num2)

print(sum1)


###########STRING INDEXING

#Indexing is used to find any character in a string using[]
# # it starts from 0 i.e. the first character is indexed 0

my_name='polycarp'

print(my_name[4])





############SLICING strings
#this prints only the stated section os a string


print(my_name[1:4 ]) #prints from index 1 to 4
print(my_name[:3]) #prints from the start
print(my_name[4:])
print(my_name[-6:-3])
print(my_name[::5])
print(my_name[2::6])




###finding the length of a string

print(len(my_name)) #tells you how many characters are in the string



##printing intagers within a string

x= 20
y= 25

print('the product of %d and %d is %d' %(x, y, x*y)) #% is a place holder %d -> intagers, %f-> floating points, %s->string

#specifying the number of decimal places
x= 1.2872
y=9.773

#string methods

a= 'this is in UPPER CASE'
print(a.upper()) #prints the string in upper case
print(a.count('s')) #counts how many times the character has been used in the string
print(a.find('upper'))#finds the position of the word in the string
print(a.swapcase()) #changes upper case to lower case and vice versa
print(a.replace('UPPER' , 'lower'))#replaces the specified part of the string