#Q..write a python function to sum of all
#   the numbers in the list??

'''
 METHOD -1
def sum_list(s):
    sum=0
    for val in s:
        sum=sum+val
    print("sum of Element=",sum)


s=[11,33,44,22,55,66]
sum_list(s)
'''

# METHOD- 2
def sum_list(s):
    sum=0
    for val in s:
        sum=sum+val
    print("Sum of ELement=",sum)

s=[]
n=int(input("enter limit:"))
for i in range(0,n):
    num=int(input("Enter Number:"))
    s.append(num)
sum_list(s)
