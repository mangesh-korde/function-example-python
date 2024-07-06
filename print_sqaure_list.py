#Q..write a python function to create and print list
#   where the values are square of numbers bteween 1 to 50(both included..)??

def list_square():
    a=[]
    for i in range(1,51):
        n=i*i
        a.append(n)
    print(a)

list_square()
