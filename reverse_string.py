#Q...write a python function reverse  a string???

 #METHOD - 1

def rev_string(s):
    print(s[::-1])

s=input("ENter string:")
rev_string(s)




#METHOD -2
'''
def rev_string(s):
    
    for i in range(len(s)-1,0,-1):
        print(s[i],end="")
    print(s[0],end="")

s="karan"
print("Reverse String=")
rev_string(s)
'''
