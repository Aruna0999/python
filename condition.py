#conditions
#if-condition by using comparision operators
#<,>,<=,>=,!=,==
'''a=10
b=20
if a<b:
    print("true")'''


'''a=10
b=20
if a>b:
    print("true")'''

'''a=5
b=7
if a<=b:
    print("less")'''

'''a=12
b=15
if a>=b:
    print("true")'''

'''a=12
b=15
if a!=b:
    print("true")'''


'''a=10
b=10
if a==b:
    print("true")'''

'''a="python"
if a=="python":
    print("match")'''

'''a=int(input("a value"))
b=int(input("b value"))
if a<b:
    print("less")'''

'''a=int(input("a value"))
if a<50:
    print("less")'''

#if condition by using logical operators
#and,or,not
'''a=3
b=6
if a<b and b>a:
    print("true")'''

'''a=4
b=7
if a<=b and b>=a:
    print("true")'''

'''a=9
b=12
if a!=b and a==b:
    print("true")'''

'''a=2
b=4
if a<b or b>a:
    print("true")'''

'''a=14
b=16
if a<=b or b>=a:
    print("true")'''

'''a=3
b=6
if a!=b or a==b:
    print("true")'''

'''a=5
b=7
if not a<b:
    print("true")'''

'''a=3
b=6
if not a>b:
    print("true")'''

'''a=3
b=6
if not a<b and b>a:
    print("true")'''

'''a=3
b=6
if not a<b or b>a:
    print("true")'''

#if-condition by using identify operators
#is,is-not

'''a=4
if type(a) is int:
    print("is is int")'''

'''a=4
if type(a) is not int:
    print("is is int")'''

'''a=4.3
if type(a) is float:
    print(" is float")'''

'''a=4.3
if type(a) is not float:
    print("is is int")'''

'''a="prasanna"
if type(a) is str:
    print("is string")'''

'''a="prasanna"
if type(a) is not str:
    print("is string")'''

'''a="True"
if type(a) is bool:
    print("is boolean")'''

    
'''a=True
if type(a) is bool:
    print("is boolean")'''
#if-condition by using membership operators
#in,not in

'''a=2,3,4,5,6,7,8
if 8 in a:
    print("true")'''

'''a=2,3,4,5,6,7,8
if 8 not in a:
    print("true")'''

'''a=int(input("a value"))
if 30 in a:
    print("true")'''#error

'''a=2,3,4,5,6,7,8,9,10
b=int(input("value"))
if b in a:
    print("true")'''

#if-else condition using comparision operators
'''a=4
b=8
if a<b:
    print("less")
else:
    print("false")'''

'''a=4
b=8
if a>b:
    print("less")
else:
    print("false")'''

'''a=5
b=8
if a<=b:
    print("less")
else:
    print("false")'''

'''a=4
b=8
if a>=b:
    print("true")
else:
    print("false")'''

'''a=4
b=8
if a!=b:
    print("true")
else:
    print("false")'''

'''a=8
b=8
if a==b:
    print("true")
else:
    print("false")'''


'''a="python"
if a=="python":
    print("match")
else:
    print("not match")'''

'''a=int(input("a value"))
b=int(input("b value"))
if a<b:
    print("less")
else:
    print("greater")'''
#if-else condition by using logical operators
#and,or,not

'''a=3
b=6
if a<b and b>a:
    print("true")
else:
    print("false")'''

'''a=4
b=7
if a<=b and b>=a:
    print("true")
else:
    print("false")'''

'''a=4
b=7
if a!=b and a==b:
    print("true")
else:
    print("false")'''

'''a=5
b=7
if not a<b:
    print("true")
else:
    print("false")'''

'''a=5
b=7
if not a>b:
    print("true")
else:
    print("false")'''

'''a=5
b=7
if not a<b or b>a:
    print("true")
else:
    print("false")'''
#if-else condition by using identify operators
#is,is-not

'''a=4
if type(a) is int:
    print("is is int")
else:
    print("is not int")'''

'''a=4
if type(a) is not int:
    print("is is int")
else:
    print("is not int")'''

'''a=4.5
if type(a) is not float:
    print("is is float")
else:
    print("is not float")'''

'''a=4.5
if type(a) is float:
    print("is is float")
else:
    print("is not float")'''

'''a="prasanna"
if type(a) is not str:
    print("is string")
else:
    print("is not string")'''

'''a=True
if type(a) is  bool:
    print("is boolean")
else:
    print("is not boolean")'''
#if-else condition by using membership operators
#in,not in
'''a=2,3,4,5,6,7,8
if 8 in a:
    print("true")
else:
    print("false")'''

'''a=2,3,4,5,6,7,8
if 8 not in a:
    print("true")
else:
    print("false")'''

'''a=int(input("a value"))
if 30 in a:
    print("true")
else:
    print("false")'''#error

'''a=2,3,4,5,6,7,8,9,10
b=int(input("value"))
if b in a:
    print("true")
else:
    print("false")'''

'''a=2,3,4,5,6,7,8,9,10
b=int(input("value"))
if b not in a:
    print("true")
else:
    print("false")'''

#if-elif-else condition using comparision operators

'''a=4
b=6
if a<b:
    print("less")
elif b>a:
    print("greater")'''


'''a=4
b=6
if a==b:
    print("less")
elif b<a:
    print("greater")
elif a!=b:
    print("not equal")'''

'''a=4
b=6
if a==b:
    print("less")
elif b>a:
    print("greater")
else:
    print("not equal")'''

#if-elif-else condition using logical operators

'''a=3
b=6
if a<b and b>a:
    print("true")
elif a<=b and b>=a :
    print("false")
elif a!=b and a==b:
    print("not equal")'''

'''a=3
b=3
if a<b and b>a:
    print("true")
elif a<=b and b>=a :
    print("false")
elif a!=b and a==b:
    print("not equal")'''


'''a=9
b=4
if a<b or b>a:
    print("true")
elif a<=b or b>=a:
    print("true")
elif a!=b or a==b:
    print("true")'''


'''a=9
b=4
if  not a<b:
    print("less")
elif not a>b:
    print("greater")
elif a!=b or a==b:
    print("not equal")'''
#if-elif-else condition by using identify operators

'''a=5
if type(a) is int:
    print("it is int")
elif type(a) is not int:
    print("false")'''
#if-elif-else condition by using membership operators
'''a=2,3,4,5,6,7,8
if 8 in a:
    print("true")
elif 8 not in a:
    print("false")'''

'''a=2,3,4,5,6,7,8
if 10 in a:
    print("true")
elif 10 not in a:
    print("false")'''

#multiple if conditions
#comparision operators

'''a=20
b=40
if a<b:
    print("less")
if a>b:
    print("greater")
if a!=b:
    print("not equal")'''

'''a=20
b=40
if a==b:
    print("less")
if b>a:
    print("greater")
if a>=b:
    print("not equal")
else:
    print("true")'''

#logical operators
'''a=20
b=40
if a<b and b>a:
    print("less")
if a>b or a!=b:
    print("greater")
if not a!=b:
    print("not equal")
else:
    print("true")'''

#identify operators

'''a=5
if type(a) is int:
    print("it is int")
if type(a) is not int:
    print("not int")
if type(a) is str:
    print("string")
else:
    print("true")'''

#membership operators
'''a=2,3,4,5,6,7,8
if 8 in a:
    print("true")
if 8 not in a:
    print("false")
if 10 in a:
    print("10 in")
else:
    print("not in")'''

#nested-if conditions
'''a=4
b=9
if a<b:
    print("less")
    if b>a:
        print("greater")'''

'''a=4
b=9
if a<b:
    print("less")
    if b>a:
        print("greater")
    else:
        print("false")'''

'''a=7
b=11
if a!=b:
    print("true")
    if b==a:
        print("greater")'''
'''a=7
b=11
if a!=b:
    print("true")
    if b==a:
        print("greater")
    else:
        print("false")'''

'''a=13
b=15
if a==b:
    print("true")
    if b>a:
        print("greater")
else:
    print("false")'''
'''a=7
b=11
if a!=b:
    print("true")
    if(b==a):
        print("greater")
    else:
        print("false")
else:
    print("not true")'''

'''a=20
b=25
if a!=b:
    print("true")
    if b==a:
        print("greater")
    elif a<b:
        print("less")
    else:
        print("false")'''

'''a=int(input())
b=int(input())
if a!=b:
    print("true")
    if b==a:
        print("equal")
    elif b>a:
        print("greater")
    else:
        print("false")
else:
    print("program ends")'''
    

