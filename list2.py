# Find the sum of elements in a list:  Write a program that iterates through a list of numbers and calculates the sum of all the elements.

mylist=[1,2,3,4,5]
total = 0
for num in mylist:
    total = total+num
print("sum of elements",total)