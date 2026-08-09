Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #dict{}
>>> a={"name":"pooja","city":"vja"}
>>> print(a)
{'name': 'pooja', 'city': 'vja'}
>>> type(a)
<class 'dict'>
>>> b={5,6,7,8,9,"name"}
>>> type(b)
<class 'set'>
>>> c={"name":"prasanna","mailid":"prasanna@gmail.com","mobileno":7330911992}
>>> print(c)
{'name': 'prasanna', 'mailid': 'prasanna@gmail.com', 'mobileno': 7330911992}
>>> c.keys()
dict_keys(['name', 'mailid', 'mobileno'])
>>> c.values()
dict_values(['prasanna', 'prasanna@gmail.com', 7330911992])
>>> c.items()
dict_items([('name', 'prasanna'), ('mailid', 'prasanna@gmail.com'), ('mobileno', 7330911992)])
>>> d={"course":"python","institute":"codegnan"}
>>> d.update({"name":"prasanna"})
>>> d
{'course': 'python', 'institute': 'codegnan', 'name': 'prasanna'}
>>> d.update({"year":2026},{"month":7})
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    d.update({"year":2026},{"month":7})
TypeError: update expected at most 1 argument, got 2
>>> d.update({"year":2026,{"month":7})
...          
SyntaxError: closing parenthesis ')' does not match opening parenthesis '{'
>>> d.update({"year":2026,"month":7})
...          
>>> d
...          
{'course': 'python', 'institute': 'codegnan', 'name': 'prasanna', 'year': 2026, 'month': 7}
>>> e={"year":2026,"month":"july"}
...          
>>> e.setdefault("date",2)
...          
2
>>> e
...          
{'year': 2026, 'month': 'july', 'date': 2}
>>> e.
...          
SyntaxError: invalid syntax
a={"time":12,"hour":1,"min":3}
         
a.pop()
         
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    a.pop()
TypeError: pop expected at least 1 argument, got 0
a.pop("time")
         
12
a
         
{'hour': 1, 'min': 3}
a.popitem()
         
('min', 3)
a
         
{'hour': 1}
a={"college":"scet","branch":"cse"}
         
a.get("college")
         
'scet'
a["branch"]
         
'cse'
a
         
{'college': 'scet', 'branch': 'cse'}
a.get("cse")
         
a
         
{'college': 'scet', 'branch': 'cse'}
a["cse"]
         
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    a["cse"]
KeyError: 'cse'
a={"hour":12,"min":3,"sec":60}
         
a.copy()
         
{'hour': 12, 'min': 3, 'sec': 60}
a
         
{'hour': 12, 'min': 3, 'sec': 60}
a.clear()
         
a
         
{}
b={}
         
b.update({"name":"prasanna"})
         
b
         
{'name': 'prasanna'}
a={"name":"prasanna","course":"python","year":2026}
         
len(a)
         
3
a={"name":"prasanna","city":"vja","name":"prasanna"}
         
print(a)
         
{'name': 'prasanna', 'city': 'vja'}
a={"name":"prasanna","city":"vja","name":"priya"}
         
print(a)
         
{'name': 'priya', 'city': 'vja'}
a={"name1":"prasanna","city":"vja","name2":"prasanna"}
         
print(a)
         
{'name1': 'prasanna', 'city': 'vja', 'name2': 'prasanna'}
a={"idnos":[10,20,30],"names":["prasanna","rama","aruna"],"marks":[60,70,80]}
         
print(a)
         
{'idnos': [10, 20, 30], 'names': ['prasanna', 'rama', 'aruna'], 'marks': [60, 70, 80]}
type(a)
         
<class 'dict'>
a.keys()
         
dict_keys(['idnos', 'names', 'marks'])
a.values()
         
dict_values([[10, 20, 30], ['prasanna', 'rama', 'aruna'], [60, 70, 80]])
a.items()
         
dict_items([('idnos', [10, 20, 30]), ('names', ['prasanna', 'rama', 'aruna']), ('marks', [60, 70, 80])])
