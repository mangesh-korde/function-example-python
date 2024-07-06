#Q..write a python function that takes a list and returns a new list
#   with unique elements of the first list??


#  METHOD -1
'''
def uni_list(s):
    b=set(s)
    print(type(b))
    c=list(b)
    print(type(c))
    print(c)

s=[11,22,11,34,66,11,22]
uni_list(s)
'''
# METHOD - 2
 
def uni_list(s):
    s1=[]
    for val in s:
        if val not in s1:
            s1.append(val)
    print(s1)

s=[11,22,11,34,66,11,22]
uni_list(s)
