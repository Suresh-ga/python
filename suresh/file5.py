f=open("sample.txt")
s=f.readline()
print("readline:"+s)
s=f.readline(5)
print("readline:"+s)
s=f.readlines()
print(s)
f.close()