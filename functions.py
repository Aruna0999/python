'''a=10
b=20
print("the sum is:",a+b)
print("the diff is:",a-b)
print("the product is:",a*b)

a=100
b=200
print("the sum is:",a+b)
print("the diff is:",a-b)
print("the product is:",a*b)

a=1000
b=2000
print("the sum is:",a+b)
print("the diff is:",a-b)
print("the product is:",a*b)'''


'''def calculate(a,b):
    print("the sum is:",a+b)
    print("the diff is:",a-b)
    print("the product is:",a*b)
calculate(10,20)
calculate(100,200)
calculate(1000,2000)'''


'''def calculate(a,b):
    print("the int div is:",a//b)
    print("the dmod is:",a%b)
    print("the pow is:",a**b)
calculate(4,2)
calculate(10,20)
calculate(3,5)'''


'''def add(a,b):
    print(a+b)
add(4,5)'''

'''while True:
    def cal():
        a=int(input("a value"))
        b=int(input("b value"))
        print(a+b)
    cal()'''

'''def cal():
        a=int(input("a value"))
        b=int(input("b value"))
        print(a+b)
        cal()
cal()'''


'''def fullname():
    fname=input("first name")
    lname=input("last name")
    print((fname+" "+lname).title())
fullname()'''

'''def mul(a,b):
    print(a*b)
mul(3,5)'''

'''def mul(a,b):
    return(a*b)
print(mul(3,5))'''

#print v/s return
'''def add(a,b):
    c=a+b
    d=a-b
    e=a*b
    print(c)
    print(d)
    print(e)
add(5,6)'''

'''def add(a,b):
    c=a+b
    d=a-b
    e=a*b
    #return c
    #return d
    #return e
    return(c,d,e)
print(add(6,8))'''


#splitbill()

'''def splitbill():
    bill=int(input("enter the bill:"))
    persons=int(input("enter the persons:"))
    print(bill//persons)
splitbill()'''


'''def splitbill():
    bill=int(input("enter the bill:"))
    persons=int(input("enter the persons:"))
    c=bill//persons
    #.format()
    print("perhead bill is {}".format(c))
    #fstring()
    print(f"perhead bill is {c}")
splitbill()'''


    
'''def splitbill():
    bill=int(input("enter the bill:"))
    persons=int(input("enter the persons:"))
    c=bill//persons
    #.format()
    print("perhead bill is {}".format(bill//persons))
    #fstring()
    print(f"perhead bill is {bill//persons}")
splitbill()'''



'''def operations():
    a=int(input("enter a value:"))
    b=int(input("enter b value:"))
    option=int(input("1.add    #triple cotes
                        2.sub
                        3.mul"))
    if option==1:
        print(a+b)
    elif option==2:
        print(a-b)
    else:
        print(a*b)
operations()'''



#multiple def keyword

'''def add():
    print(a+b)
def sub():
    print(a-b)
def mul():
    print(a*b)
while True:
    a=int(input("a value"))
    b=int(input("b value"))
    option=int(input("choose the option
                         1.aa
                         2.sub
                         3.mul"))
    if option==1:
        add()
    elif option==2:
        sub()
    elif option==3:
        mul()'''


#keyword and positional arguments
'''def Details(id,name,mailid):
    id=10
    name="prasanna"
    mailid="prasannatalla18@gmail.com"
    print(id,name,mailid)
Details(id="id",name="name",mailid="mailid")'''


'''def Details(id,name,mailid):
    print(id,name,mailid)
Details(id="id",name="name",mailid="mailid")
Details(id=20,name="prasanna",mailid="prasanna@gmail.com")
Details(id=30,name="lakshmi",mailid="lakshmi@gmail.com")
Details(40,"chitra","c@gmail.com")
Details("d@gmail.com",50,"sri")
Details(mailid="p@gmail.com",id=60,name="priya")'''


#default arguments

'''def Grocery(item,price):
    print("item is %s" %item)
    print("price is %.2f" %price)
Grocery("sugar",100)'''

                    
'''def Grocery(item="rice",price=1500):
    print("item is %s" %item)
    print("price is %.2f" %price)
Grocery()'''    
            

'''def Grocery(item,price=200):
    print("item is %s" %item)
    print("price is %.2f" %price)
Grocery("dhal")'''


'''def Grocery(item="ghee",price):
    #non def arg follows def arg
     print("item is %s" %item)
     print("price is %.2f" %price)
Grocery(300)'''


#cake

'''def Cake(cake_name,price,qty):
    print("cake_name is %s" %cake_name)
    print("price is %.2f" %price)
    print("qty is %s" %qty)
Cake("butterscotch",600,"1kg")'''


'''def Cake(cake_name="butterscotch",price=600,qty="1kg"):
    print("cake_name is %s" %cake_name)
    print("price is %.2f" %price)
    print("qty is %s" %qty)
Cake()'''



'''def Cake(cake_name,price=600,qty="1kg"):
    print("cake_name is %s" %cake_name)
    print("price is %.2f" %price)
    print("qty is %s" %qty)
Cake("butterscotch")'''


'''def Cake(cake_name,price=600,qty):
    #non def arg follows def arg
    print("cake_name is %s" %cake_name)
    print("price is %.2f" %price)
    print("qty is %s" %qty)
Cake("1kg")'''




#* arguments(* is used to unpack the elements)
'''a=[2,3,4,5,6]
print(a)
print(*a)'''

'''a=(2,3,4,5,6)
print(a)
print(*a)'''


'''a={2,3,4,5,6}
print(a)
print(*a)'''


'''b={"name":"prasanna","city":"vja"}
print(b)
print(*b)'''


'''c="python"
print(c)
print(*c)'''


'''a,b,c=2,3,4,5,6,7,8,9,10
print(a)
print(b)
print(c)''' #error

'''a,b,c=2,3,4
print(a)
print(b)
print(c)'''


'''*a,b,c=2,3,4,5,6,7,8,9,10
print(*a)
print(b)
print(c)'''


'''a,*b,c=2,3,4,5,6,7,8,9,10
print(a)
print(*b)
print(c)'''

'''a,b,*c=2,3,4,5,6,7,8,9,10
print(a)
print(b)
print(*c)'''

'''a,b,c="codegnan"
print(a)
print(b)
print(c)''' #error


'''a,b,c="cod"
print(a)
print(b)
print(c)'''


'''a,b,*c="codegnan"
print(*a)
print(b)
print(*c)'''



#variable length arguments

'''def check(*a):
    print(a)
    print(type(a))
check()
check(2,3,4,5,6,7,8)
b=[4,5,6,7,8]
check(*b)
c={5,6,7,8,9,10}
check(*c)
d={"name":"prasanna","age":21,"place":"vja"}
check(*d)'''


'''def check1(*a):
    d=1#creating a variable
    print(a)
    print(type(a))
    for i in a:
        if type(a) in (int,float):
            d=d+i
            print(d)
check1()
check1(2,3,4,5,6)
check1(1,3,4,5,2.3,4.3)
check1(4,3,6,2,3.4,2.3,"python")'''



#**(kwargs)
'''def check2(**a):
    print(a)
    print(type(a))
check2()
details={"names":["sweety","cuty","hearty"],
         "marks":[60,70,80],
         "statue":["p","a","p"]}
check2(**details)'''


'''def check2(**a):
    print(a)
    print(type(a))

    for i in a:
        print(i) #keys
    for i in a.keys():
        print(i)#keys
    for i in a:
        print(a[i]) #values
    for i in a.values():
        print(i) #values
    for i in a:
        print(i,a[i]) #keys,values
    for i in a.items():
        print(i)   #keys,values
check2()
details={"names":["sweety","cuty","hearty"],
         "marks":[60,70,80],
         "status":["p","a","p"]}
check2(**details)'''


#both * and ** usage

'''def final(*a,**b):
    d=2
    print(a)
    print(b)
    print(type(a))
    print(type(b))
    for i in a:
        d=d+i
        print(d)
    for i,j in b.items():
        print("keys is:",i)
        print("values is:",j)
final()
data=(2,3,4,5,6,2.3,4.5)
final(*data)
details={"years":[2004,2005,2006],
         "month":["june","july","august"]}
final(**details)
final(*data,**details)'''



                  
