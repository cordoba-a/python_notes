user_option = input('elige piedra, papel o tijera => ')

import random
opciones = ['piedra','papel','tijera']
computer_option = random.choice(opciones)
print('computer_option => '+ computer_option)

if user_option == computer_option:
  print('Empate')
elif user_option == 'piedra':
  if computer_option == 'tijera':
    print('piedra gana a tijera')
    print('user gano!')
  else:
    print('papel gana a la piedra')
    print('computer gano!')
elif user_option == 'papel':
  if computer_option == 'piedra':
    print('papel gana a piedra')
    print('user gano')
  else:
    print('tijera gana a papel')
    print('computer gano')
elif user_option == 'tijera':
  if computer_option == 'papel':
    print('tijera gana a papel')
    print('user gana')
  else:
    print('piedra gana a tijera')
    print('computador gano!')