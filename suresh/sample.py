
f= open("sample.txt","r")
print(f.name)
print(f.tell())
print(f.seek(10,0))
print(f.tell())
print(f.read())
f.close()