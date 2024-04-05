# program to print area of triangle
def area_triangle(base,height):
    return 0.5 * base * height 
base=int(input('enter the base of triangle'))
height=int(input('enter the height of triangle'))
result= area_triangle(base,height)
print("the area of triangle is",result)