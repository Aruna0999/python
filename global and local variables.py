#global and local variables
#first case of global variable
'''a=4
def check1():
    print("inside value is:",a)
check1()
print("outside value is:",a)'''


#second case of global variables

'''a=2
def check2():
    a=5
    a=a**2
    print("inside value is:",a)
check2()
print("outside value is:",a)'''


#third case of both local and global variables
'''a=6
def check3():
    a=8
    print("inside value is:",a)
    a=10
    print("updated value is:",a+5)
    b=13#local variable
    b=b+a
    print("value of b is",b)
check3()
print("a value is:",a)
print("b value is:",b)'''

#usage of global keyword

'''a=4
def final():
    global a,b
    print("inside value is:",a)
    a=15
    print("updated value is:",a)
    #global b
    b=20
    b=b+a
    print("value of b is:",b)
final()
print("a value is:",a)
print("b value is:",b)'''
