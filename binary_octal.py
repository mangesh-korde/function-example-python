#Q..write a python function to accept decimal number and
#   convert it into binary number and octal number???

def bin_oct(n):
    print("Binary No=",bin(n))
    print("Octal No=",oct(n))


n=int(input("Enter Number:"))
bin_oct(n)
