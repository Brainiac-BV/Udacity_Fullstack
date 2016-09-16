#tuple demo
#can contain multple data types
t = ('string', 1, True, [1,2,3])
print(t)

print(len(t))
print(type(t))



#str demo

#format example
n = "The age of {0} is {1}".format('keith', '32')
print(n)

#range demo
#list creation with range
samp_list = list(range(10,21))
print(samp_list)

#iterate through ranged list creating series of tuples with element position
for p in enumerate(samp_list):
    print(p)

#list demos
#half open range example. the following is for the first 3 elements   
print(samp_list[:3])
#half open range slice example for all but the first 3 elements
print(samp_list[3:])
#same as above but full slice meaning entire list
print(samp_list[:])

