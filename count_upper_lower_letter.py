#Q..count uppercase and lowercase letters in a string??

def upper_lower(s):
    cnt=0
    cnt1=0
    for ch in s:
        if ch>='A' and ch<='Z':
            cnt=cnt+1
        else:
            cnt1=cnt1+1
    print("upper-case letters=",cnt)
    print("Lower-case letters=",cnt1)


    
s=input("Enter string:")
upper_lower(s)
