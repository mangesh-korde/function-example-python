#Q..Define a function that accept a Two string as input
#   and find union and intersection of them???

def union_intersection(s,s1):
    t=set(s)
    t1=set(s1)
    print(type(t))
    print(type(t1))
    c=t.union(t1)
    print("union of two string=",c)
    d=t.intersection(t1)
    print("intersection of two string=",d)


s=input("Enter first string:")
s1=input("Enter second string:")
union_intersection(s,s1)
