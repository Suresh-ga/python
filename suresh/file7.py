f=open("sample.txt","r+")
f.seek(0,2)
line=f.write("axness")
print(line)
