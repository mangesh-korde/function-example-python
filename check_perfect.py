#Q..Check number is perfect or not???

def check_perfect(n):
    sum=0
    for i in range(1,n):
        if n%i==0:
            sum=sum+i
    if sum==n:
        print("Number is perfect..")
    else:
        print("Number is not perfect...")


n=int(input("Enter number:"))
check_perfect(n)
