#anonymous functions

#write a function to calculate 2*x+5 where x=5

'''def calculate(x):
    print(2*x+5)
calculate(5)'''

'''def f():
    x=int(input("value"))
    print(2*x+5)
f()'''


#syntax
#a=lambda ard:expr

'''a=lambda x:2*x+5
print(a(5))'''


'''a=int(input())
b=lambda x:2*x+5
print(b(a))'''


'''x=int(input("enter x"))
y=int(input("enter y"))
c=lambda x,y:x*y
print(c(a,b))'''


'''a=lambda x,y:x*y
print(a(3,5))'''


#codegnan
#CODEGNAN

'''a="codegnan"
b=lambda a:a.upper()
print(b(a))'''

'''a=lambda a:a.upper()
print(a("codegnan"))'''

#python course
#Python Course

'''a="python course"
b=lambda a:a.title()
print(b(a))'''

#firstname+lastname=fullname

'''fname=input("enter fname")
lname=input("enter lname")
c=lambda fname,lname:(fname+" "+lname).title()
print(c(fname,lname))'''


#using generator
'''fname,lname=[x for x in input("enter the names").split(",")]
c=lambda fname,lname:(fname+" "+lname).title()
print(c(fname,lname))'''


#filter()
'''a=[10,30,50,100,127,39,45,67,200]
for i in a:
    if i%2==0:
        print(i)'''
'''b=list(filter(lambda x:x%2==0,a))
print(b)'''

'''a=[[],(),set(),{}," ",None,5,8.9,"python",5+9j,True,False]
b=list(filter(None,a))
print(b)'''

'''a=[]
print(type(a))

b=()
print(type(b))

c={}
print(type(c))

d=set()
print(type(d))'''



