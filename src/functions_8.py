
# range() function
rng = range(6)
print(rng)
print(list(rng))

rng = range(1, 6, 2)
print(rng)
print(list(rng))
print(set(rng))
print(tuple(rng))


# map() function

strings = ["Hello World, It is a beautiful day", "Python is awesome", "I am learning Python"]
mapped =map(len, strings)
print((mapped))
print(list(mapped))


