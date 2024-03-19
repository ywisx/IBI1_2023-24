#Suppose you can leave the lab for i days
i=1
a=5
#Plug in the reproduction rules given.
while(a<=90):
    a=a*2
    i=i+1
#So we can print out the number of days away from the lab
print(i-1)
#We know from the results that we can leave the lab for five days. 
#You must return at day6, which is the fifth day after leaving for five days.

