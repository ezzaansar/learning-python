# Write a program to reverse the string "hello" using a for loop

original_string="hello"
reversed_string= ""
for i in range(len(original_string)-1,-1,-1):

 reversed_string += original_string[i]

print("Reversed string:", reversed_string)