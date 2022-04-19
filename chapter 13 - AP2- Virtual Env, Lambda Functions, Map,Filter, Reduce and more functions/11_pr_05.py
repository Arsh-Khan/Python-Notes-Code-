from functools import reduce

# method 1:
# def maximum(a,b):
#     if a>b:
#         return a
#     else:
#         return b    

# l = [3, 8, 456, 2, 5, 45]
# val = reduce(maximum, l)

#method 2
l = [3, 8, 456, 2, 5, 45]
val = reduce(max,l) #max is build in funcn
print(val)
