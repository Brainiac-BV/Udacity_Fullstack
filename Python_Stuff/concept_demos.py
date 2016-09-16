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

#set demos
s = {2,3,4,5,6,7,8}
print(s)
print(type(s))
#new set from list
s2 = set(samp_list)
print(s2)
#print shared values between two sets
print(s2.intersection(s))
#prints differences between two sets
print(s2.difference(s))

#comprehension demos
#list comprehension syntax [expr(item) for item iterable]
print([len(str(samp)) for samp in samp_list])
#dictionary comprehension syntax {key_expr(key names):value_expr(value names) for item(the names) in iterable(the variable)}
country_to_capital = {'UK':'London', 'Brazil':'Brazilia', 'Sweeden':'Stockholm', 'Morocco':'Rabat'}
print(country_to_capital['UK'])
capital_to_country = {capital: country for country, capital in country_to_capital.items()}
print(capital_to_country)
#comprehensions can be filtered with if statements

# simple generator example
def gen123():
	yield 1
	yield 2
	yield 3

g = gen123()
#access each yield point with Next()
print(next(g))	
#stateful generator
def take(count, iterable):
    counter = 0
    for item in iterable:
        counter += 1
        yield item

f = take(3, samp_list)
print(f)
print(next(f))
print(list(f))
#generator comprehension
print(sum(x*x for x in range(1, 1000001)))
