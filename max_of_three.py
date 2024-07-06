#Q..write a python function to
#   find the MAX of three numbers??
def max(a,b,c):
    print(type(a))
    print(type(b))
    print(type(c))
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c

a=int(input("Enter no 1:"))
b=int(input("Enter no 2:"))
c=int(input("Enter no 3:"))
print("Maximum no=",max(a,b,c))
