# Question1
String1 = "Aditya"
lst1 = [1,2,3,4,5]
flt1 = 2.14
tup1 = (1,2,3,4,5)
# Question2
var1 = ' '
var2 = '[ DS , ML , Python]'
var3 = [ 'DS' , 'ML' , 'Python' ]
var4 = 1.0
print(type(var1))
print(type(var2))
print(type(var3))
print(type(var4))
c2 = 4
# Question 4
lst2 = [1,'a',2,'b','X',c2,2.4,True,3.1,False]
for i in lst2:
    print(i)
# Question 5
a = 81
b = 3
while(b<=a):
    if b % a == 0:
        print('Is Divisible')
        break
    else:
        print("Not Divisible")
        break
# Question 6
lst3 = [20,21,22,23,27,28,29,30,34,35,44,45,49,52,57,60,67,65,123,24,56,87,94,95,98]
for i in lst3:
    if i % 3 == 0:
        print('Completely Divisible')
    else:
        print('Not Divisible')

# Question 7
# tuples are immutable
   
tuple1 = (0, 1, 2, 3)
tuple1[0] = 4
print(tuple1)
# strings are immutable

message = "Welcome to GeeksforGeeks"
message[0] = 'p'
print(message)
#lists are mutable
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)
