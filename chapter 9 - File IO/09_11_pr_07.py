content = True
i=1
with open('log.txt') as f:
    while content:
        content = f.readline()
        if 'python' in content.lower():
            print(content)
            print(f"Yes Python is present on line {i}")
        i+=1 