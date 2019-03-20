# ## list comprehension

l = [x*x for x in range(100)]  # simple list comprhension
print(l)

l = [x for x in range(100) if x%2 == 0]  # with conditions
print(l)

l = [(x,y,z) for x in range(101) for y in range(101) for z in range(101) if x**2 + y**2 == z**2]  # multiple variable
print(l)

l = (x**3 for x in range(11))  # generator: it returns generator (iterator) object instead of list
print(l)
print(list(l))

noprimes = [j for i in range(2, 8) for j in range(i*2, 100, i)]  # sieve of Eratosthenes
primes = [x for x in range(2, 100) if x not in noprimes]
print(primes)

# ## set comprehnsion  --> same as list comprehension but with set ( no element can have duplicate

l = {x*x for x in range(100)}
print(l)

