f=open("sample.txt","r+")
print("name of the file:",f.name)
line=f.readline()

print("readline:%s"%(line))
f.truncate(7)
line=f.readlines()
print("readline:%s"%(line))
f.close()




