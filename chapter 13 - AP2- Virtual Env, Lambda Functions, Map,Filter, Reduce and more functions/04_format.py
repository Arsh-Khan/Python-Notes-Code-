#f strings were introduced in python 3.6
# before for doing the same task we used to use format method 

name = "Harry"
channel = "CodeWithHarry"
type = "coding"
# a = f"This is {name}"

# a = "This is {}".format(name)
#  a = "This is {} and his channel name is {}".format(name,channel) # ---> in order apperance
a = "This is {1} and his {2} channel name is {0}".format(name,channel,type) #in this we are deliberately changing position of apperance
 
print(a)
