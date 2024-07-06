#Q..write a python function that takes a
#   number asa parameter and check number is
#   prime or not???

def check_prime(n):
    flag=0
    for i in range(2,n):
        if n%i==0:
            flag=1
            break
    if flag==0:
        print("Number is prime..")
    else:
        print("Number is not prime...")

n=int(input("Enter no:"))
check_prime(n)
