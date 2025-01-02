x = 3.3
print(x)
y = 1.1 + 2.2
print(y)
print(x == y)

#si  no tenemos esto en cuenta tendremos algunos errores

#comparar flotantes como str
y_str = format(y, ".2g")
print('str => ', y_str)
print(y_str == str(x))

#comparar flotantes como mat
print('*' * 10)
print(y, x)
tolerance = 0.000001
print(abs(x-y)<tolerance) #abs = absoluto