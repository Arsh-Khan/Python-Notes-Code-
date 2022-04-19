with open('log.txt') as f:
    content = f.read()

if 'python' in content.lower(): #converts the string to lower caps
    print("Yes Python is present")
else:
    print("No Python is not present")    