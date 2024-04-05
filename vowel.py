# Write a program that takes a string as input and returns the number of vowels (a, e, i, o, u) in the string.
def count_vowels(str):
    vowel = "aeiouAEIOU"
    count = 0
    for char in str:
      if char in vowel:
       count+=1
    return count
user_input = input("enter an integer")
vowel_count = count_vowels(user_input)
print("number of vowels are",vowel_count)