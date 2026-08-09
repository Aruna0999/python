#loops()
#for,while,range,break,continue,pass

#forloop()
'''a=[10,20,30,40,50]
for i in a:
    print(i)'''



'''a=[10,20,30,40,50]
for i in a:
    print(a)'''

'''a=[10,20,30,40,50]
for i in a:
    print(i,end=" ")'''

'''a=[10,20,30,40,50]
for i in a:
    print(i)
print(type(a))
print(type(i))'''



'''a=(5,6,7,8,9)
for i in a:
    print(i)
print(type(a))
print(type(i))'''


'''a={5,6,7,8,9}
for i in a:
    print(i)
print(type(a))
print(type(i))'''


'''b={"year":2026,"month":"july","date":9}
for i in b:
    print(i)
    print(type(b))
    print(type(i))
for i in b.keys():
    print(i)
for i in b.values():
    print(type(b))
    print(type(i))
    print(i)
for i in b.items():
    print(i)
    print(type(b))
    print(type(i))'''


'''a="codegnan"
for i in a:'''


'''b=[4.5,6.7,8.9]
for i in b:
    print(i)
    print(type(b))
    print(type(i))'''

'''b=["python","java","c","c++"]
for i in b:
    print(i)
    print(type(b))
    print(type(i))'''

'''b=[4+9j,3+2j]
for i in b:
    print(i)
    print(type(b))
    print(type(i))'''

'''b=[True,False]
for i in b:
    print(i)
    print(type(b))
    print(type(i))'''


'''fruits =["apple","banana","mango"]
b=[]
for i in fruits:
    b.append(i.upper())
print(b)'''


'''a=[1,3,5,7,9,"code"]
a.extend("code")
print(a)'''



#while loop()

'''a=10
while a>1:
    print(a)'''

'''a=10
while a<1:
    print(a)'''

'''a=10
while a>1:
    print(a)
    a=a-1'''

'''a=10
while a>=1:
    print(a)
    a=a-1'''

'''a=20
while a>3:
    a=a-1
print(a)'''


'''a=40
while a>5:
    a=a-1
print(a)'''


'''a=30
while a>1:
    print(a)
    a+=1'''

'''a=10
while a>2:
    print(a)
    a-=1'''

'''a=30
while a>1:
    print(a)
    a-=1'''

'''a=1
while a<25:
    print(a)
    a+=1'''

#while True

'''while True:
    age=int(input())
    if age>=18:
        print("eligible for vote")
    else:
        print("not eligible")'''


'''while True:
    num=int(input())
    if num%2==0:
        print("even")
    else:
        print("odd")'''


#range()
#start-stop-step

'''for i in range(20):
    print(i)'''


'''for i in range(13,35):
    print(i)'''



'''for i in range(0,30,3):
    print(i)'''


'''for i in range(5,50,5):
    print(i)'''


'''for i in range(2,20,2):
    print(i)'''


#grades
'''while True:
    marks=int(input("enter marks"))
    if marks in range(91,101):
        print("Grade-A")
    elif marks in range(81,91):
        print("Grade-B")
    elif marks in range(71,81):
        print("Grade-C")
    elif marks in range(50,71):
        print("Grade-D")
    else:
        print("fail,study well")'''



#break

'''a=10
while a>1:
    print(a)
    a=a-1'''


'''a=10
while a>1:
    print(a)
    a=a-1
    if a==6:
        break'''


'''a=10
while a>1:
    a=a-1
    if a==6:
        break
    print(a)'''


'''for i in range(20):
    if i==13:
        break
    print(i)'''


'''a="python"
if a=="h":
    break
print(a) '''#error


'''a="python"
for i in a:
    if i=="h":
        break
    print(i)'''


#continue
'''a=20
while a>5:
    print(a)
    a=a-1'''


'''a=20
while a>5:
    print(a)
    a=a-1
    if a==10:
        continue'''


'''a=20
while a>5:
    a=a-1
    if a==10:
        continue
    print(a)'''


'''for i in range(15):
    if i==7:
        continue
    print(i)'''

'''a="python"
for i in a:
    if i=="y":
        continue
    print(i)'''


#pass
'''a=30
while a>10:
    print(a)
    a=a-1
    if a==20:
        pass'''

'''for i in range(40):
    if i==10:
        pass
    print(i)'''
