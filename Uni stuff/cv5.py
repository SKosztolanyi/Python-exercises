#aliasing listu

values = []
values.append(3)
values.append(11)
values.append(6)
values[0] = 2
a = values
a[0] = 4
a.append(5)

print a
print values

# kopie listu
values = [3, 11, 6]
a = list(values) # kopiruje zoznam
a[0] = 4
a.append(5)