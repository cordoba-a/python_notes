# indexing = los textos tienen un indicador, al cual se puede acceder a nivel de posición
text = 'Ella sabe Python'
print(text[0])
print(text[1])

# ingresar al ultimo caracter del texto

# forma 1
size = len(text)
print('size => ', size)
print(text[size -1 ])
# forma 2
print(text[-1])


# slicing = basado en la posición de los caracteres del string se pueden sacar partes del texto
print(text[0:5])
print(text[10:16])
# se obvia que se inicia del 0
print(text[:10])

# desde el punto 5 hasta el final
print(text[5:])

# saltos = puedo darle un inicio y un fin, más el salto

print(text[10:16:1])
print(text[10:16:2])

element = ['eater','fiAAtr','wind']
for element in element:
  print(element)

lower(element)

print((8 / 2) + 4 * 8)