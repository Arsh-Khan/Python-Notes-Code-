import os

oldname="sample2.txt"
newname="rename_by_python.txt"

with open(oldname) as f:
    content=f.read()

with open(newname,'w') as f:
    f.write(content)

os.remove(oldname)  #deletes the file using this function imported from os