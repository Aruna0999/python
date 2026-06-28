Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a=2
b=7
a&b
2
a=7
b=8
a&b
0
a=5
b=7
a&b
5
bin(2)
'0b10'
bin(4)
'0b100'
bin(5)
'0b101'
bin(7)
'0b111'

a=3
b=6
a|b
7
a=4
b=8
a|b
12
a=5
-(a+1)
-6
~a
-6
b=-9
~b
8
c=-12
~c
11

a=3
b=5
a^b
6
a=7
b=9
a^b
14
a=3
a<<2
12
b=4
b<<4
64
b<<3
32
a="vijayawada"
a[0]
'v'
a[7]
'a'
a[5]
'a'
a[0]
'v'
a[0]+a[1]+a[2]
'vij'
a[0]+a[1]+a[2]+a[3]+a[4]+a[5]+a[6]+a[7]+a[8]+a[9]
'vijayawada'
>>> a="i am in class"
>>> a(8)+a(9)+a(10)+a(11)+a(12)
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    a(8)+a(9)+a(10)+a(11)+a(12)
TypeError: 'str' object is not callable
>>> a[8]+a[9]+a[10]+a[11]+a[12]
'class'
>>> a="i am learning python course"
>>> a[14]+a[15]+a[16]+a[17]+a[18]+a[19]
'python'
>>> a[5]+a[6]+a[7]+a[8]+a[9]+a[10]+a[11]+a[12]
'learning'
>>> a[21]+a[22]+a[23]+a[24]+a[25]+a[26]
'course'
>>> a="time is very precious"
>>> a[13]+a[14]+a[15]+a[16]+a[17]+a[18]+a[19]+a[20]
'precious'
>>> a[8]+a[9]+a[10]+a[11]
'very'
>>> a[0]+a[1]+a[2]+a[3]
'time'
>>> a="simple is better than complex"
>>> a[-29]+a[-28]+a[27]+a[26]+a[25]+a[24]
'sielpm'
>>> a[-29]+a[-28]+a[-27]+a[-26]+a[-25]+a[-24]
'simple'
>>> a[-12]+a[-11]+a[-10]+a[-9]
'than'
>>> a[-7]+a[-6]+a[-5]+a[-4]+a[-3]+a[-2]+a[-1]
'complex'
>>> a[-19]+a[-18]+a[-17]+a[-16]+a[-15]+a[-14]
'better'
>>> a="i love python"
>>> a[-11]+a[-10]+a[-9]+a[-8]
'love'
>>> a[-6]+a[-5]+a[-4]+a[-3]+a[-2]+a[-1]
'python'
