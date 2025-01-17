import array as arr

# creating array
a = arr.array('i', [1, 2, 3])
a.insert(1,4)

# iterating and printing each item
for i in range(0, 3):
    print(a[i], end=" ")