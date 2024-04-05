# Create a list of squares: Write a program that iterates through a list of numbers and creates a new list containing the squares of each element
def create_squares_list(numbers):
  square_list=[]
  for num in numbers:
    square = num**2
    square_list.append(square)
  return square_list
mylist=[1,2,4,6,8]
square_list = create_squares_list(mylist)
print("Original list",mylist)
print("Square list",square_list)
