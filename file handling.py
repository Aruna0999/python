#file handling
#write()
'''a=open("prasanna.txt","w")
a.write("codegnan")
a.close()'''

'''a=open("prasanna.txt","w")
a.write("\tpython fullstack")
a.close()'''

#append
'''a=open("prasanna.txt","a")
a.write("\tdata science")
a.close()'''


'''a=open("prasanna.txt","w")
a.write(input("data"))
a.close()'''

#display data in single line
'''a=open("prasanna.txt","w")
b=input("data")
a.write(b)
a.close()'''

#read()
'''a=open("prasanna.txt")
#print(a.read())   #it will display entire content
#print(a.readline())  #it will display first line
#print(a.readlines()) #it will display in list with \n for nwe line      
print(a.read(10))     #it will displays number of characters '''


#writelines()  #it makes every object side by side

'''a=open("chitra.txt","w")
b=["prasanna","rama","aruna","chitra","mouni"]
a.writelines("\n".join(b))
a.close()'''

'''a=open("sample.py")
print(a.read())'''

