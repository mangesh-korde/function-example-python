#Q..write a python function to check wheather a number
#   is in a given range??

def check_range(n):
    if n>=100 and n<=200:
        print("Number is in range...")
    else :
        print("Number is not in range..")


n=int(input("Enter no:"))
check_range(n)
