a={}
a[(1,2,4)]=8
a[(4,2,1)]=10
a[(1,2)]=12
sum=0
for k in a:
    sum+=a[k]
    print(len(a)+sum)


#33

#So, for each key-value pair in the dictionary,
# it will print the same value, which is len(a) + sum. 
# The value of len(a) is 3 (because there are three key-value pairs), and sum is calculated by adding up the values in the dictionary, which is 8 + 10 + 12 = 30. So, it will print 3 + 30, which is 33,
#  for each key-value pair.

