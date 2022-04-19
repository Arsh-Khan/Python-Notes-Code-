#creating a tuple using ()
t = (1,2,4,5)
# t1 = ()#empty tuple

# t1=(1) -->this is not a tuple with single element this is wrong way ,compiler ko() time pass me lagaya lagega
t1 =(1,)#perfect way of tuple with single element
print(t1)

#printing the elements of tuples
print(t[0])
#cannot update the values of tuple (immutable)
# t[0]=34 --> throws an error