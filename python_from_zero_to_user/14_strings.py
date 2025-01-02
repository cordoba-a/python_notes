text = 'Ella sabe programar en Python'

'''
print('JavaScript' in text)
print('Python' in  text)

if 'JS' in text:
  print('Elegiste bien!')
else:
  print('Tambien elegiste bien')
'''
  
# analizar el tamaño de la cadena de texto
size = len(text)
print(size)

print(text)
# convirte todo el texto en mayusculas
print(text.upper())
# convirte todo el texto en minusculas
print(text.lower())
# cuenta el número de apariciones de una letra dentro el texto
print(text.count('a'))
# el texto que esten en mayusculas lo pasa a minusculas y viseversa
print(text.swapcase())
# pregunta si el texto inicia con algo en especifico
print(text.startswith('Ella'))
print(text.endswith('Rust'))

# reemplaza una cosa por otra
print(text.replace('Python', 'Go'))


text_2 = 'este es un titulo'
print(text_2)
# poner el primer caracter en mayuscula
print(text_2.capitalize())
# poner el inicio de cada palabra en mayuscula
print(text_2.title())
# nos dice si este texto es un digitol
print(text_2.isdigit())
print('398'.isdigit())