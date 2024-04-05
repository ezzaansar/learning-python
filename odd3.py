# If n is even and in the inclusive range of 6 to 20, print Weird
n = int(input("enter an integer"))
if n%2==0 and n in range(6,20):
    print("Weird")