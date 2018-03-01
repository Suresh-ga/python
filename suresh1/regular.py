import re
patterns=['this','that']
text="this is pen and that is table"
for pattern in patterns:
    print("looking for '%s' in '%s'--->"%(pattern ,text))
    if re.search(pattern,text):
        print('found the match')
    else:
        print('no match found')
pattern='this'
match=re.search(pattern,text)
s=match.start()
e=match.end()
print('pattern found at "%s" and "%s"--'%(s,e))