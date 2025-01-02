if True:
  print('debería ejecutarse')
if False:
  print('nunca se ejecuta')



pet = input('¿Cuál es tu mascota favorita? ')
if pet == 'perro':
  print('genial, tienes buen gusto')
if pet == 'gato':
  print('espero tengas suerte')



stock = int(input('Digita el stock => '))
if stock >= 100 and stock <= 1000:
  print('el stock es correcto')
else:
  print('el stock es incorrecto')



pet = input('¿Cuál es tu mascota favorita? ')
if pet == 'perro':
  print('genial, tienes buen gusto')
elif pet == 'pez':
  print('espero tengas suerte')
elif pet == 'gato':
  print('eres lo maximo')
else:
  print('no tienes mascota chida')