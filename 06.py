# Reversing a list using slicing: Can you use slicing to reverse a list without using a loop?
def reverse(list):
    rev = 0
    return list[::-1]
user_list = [1,2,3,4,5]
my_list = reverse(user_list)
print("rev list are",my_list)
