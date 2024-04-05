# If n is even and in the inclusive range of 2 to 5, print Not Weird
n = int(input("Enter an integer"))
if (n%2)==0 and n in range (2,5):
    print("Not Weird")