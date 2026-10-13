Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a=4,b=9
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
a=4;b=9
print(a+b)
13
a,b=2,3
print(a+b)
5
a,b,c=10
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    a,b,c=10
TypeError: cannot unpack non-iterable int object
a=b=c=10
print(a,b,c)
10 10 10
a,b,c=2,3,4
print(a,b,c)
2 3 4
a,b,c=2,3,4,5,6
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    a,b,c=2,3,4,5,6
ValueError: too many values to unpack (expected 3, got 5)
>>> a,b,c=(3,4,5)
>>> print(a,b,c)
3 4 5
>>> first name="aruna"
SyntaxError: invalid syntax
>>> first_name="aruna"
>>> print(first_name)
aruna
>>> firstname="aruna"
>>> print(firstname)
Aruna
>>> fname="Aruna"
>>> lname="Jyothi"
>>> print(fname+lname)
ArunaJyothi
>>> print(fname+" "+lname)
Aruna Jyothi
>>> print(fname,lname)
Aruna Jyothi
>>> name="aruna"
>>> print(name)
aruna
>>> NAME="aruna"
>>> print(NAME)
aruna
>>> Name="Aruna"
>>> print(Name)
Aruna
>>> a=4
>>> print(a)
4
>>> del a
>>> print(a)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    print(a)
NameError: name 'a' is not defined
