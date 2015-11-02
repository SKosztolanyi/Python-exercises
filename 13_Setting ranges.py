# Examples of setting ranges
>>> range(10)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> range(1, 11)
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> range(0, 30, 5)
[0, 5, 10, 15, 20, 25]
>>> range(0, 10, 3)
[0, 3, 6, 9]
>>> range(0, -10, -1)
[0, -1, -2, -3, -4, -5, -6, -7, -8, -9]
>>> range(0)
[]
>>> range(1, 0)
[]

## This is how the range looks like:
range(start, stop, stepSize), like this:
>>> range(2, 10, 2)
[2, 4, 6, 8]

>>> s = "Hello, world!"
>>> s[1:] # s[start:]
ello, world!
>>> s[1:10] # s[start:stop]
ello, wor
>>> s[1:10:3] # s[start:stop:stepSize]
eow