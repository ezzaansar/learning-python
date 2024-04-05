# Extracting every other element: Write a program that uses slicing to extract every other element from a list.
user_list = ['A','a','B','b','C' ,'c','D','d', 'E','e' ,'F','f']
original_list = user_list[::-2]
print("".join(original_list))
