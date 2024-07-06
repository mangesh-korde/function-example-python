#Q...Write a python function which print a dictionary
#    where the keys are numbers between 1 to 20.
#    and the values are square of key???

def dict_value():
    d={}
    for i in range(1,21):
        d[i]=i*i
    print(d)


dict_value()
