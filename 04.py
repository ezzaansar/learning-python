# - Extracting a sublist: Write a program that takes a list and uses slicing to extract a portion of the list based on starting and ending indices.
list = input("enter an integer").split()
list = [int(x)for x in list]
start_index = int(input("enter an integer"))
end_index = int(input("enter an integer"))
user_list = list[start_index:end_index]
print("extracted list",user_list)