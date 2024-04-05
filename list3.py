# Check if an element exists in a list: Write a program that takes a list and an element as input and determines if the element exists in the list
def check_element_exists(input_list,element):
    if element in input_list:
       return True
    else:
        return False
    
mylist = [1,2,3,4,5]
element_to_check=3
if check_element_exists(mylist,element_to_check):
    print(element_to_check,"element exist in list")
else:
    print("element exist in list")
