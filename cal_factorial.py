#Q.. write a python function to calculate the
#    factorial of a number . The fnction accepts
#    number as argument??

def cal_facto(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f


n=int(input("Enter number:"))
print("calculate factorial=",cal_facto(n))
