a = []
for i in range(10):
    a.append(i * ++i)
print(a)
for a[i] in a:
    print(a[i])