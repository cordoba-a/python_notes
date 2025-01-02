name = 'Eduardo'
last_name = 'Cordoba'

# concatenación de strings
full_name = name + ' ' + last_name
print(full_name)

# frase
quote = "I`m Eduardo"
print(quote)

# format
template = "Hola, mi nombre es " + name + " y mi apellido es " + last_name
print('v1', template)

template = "Hola, mi nombre es {} y mi apellido es {}".format(name, last_name)
print('v2',template)

# mas usado
template = f"Hola, mi nombre es {name} y mi apellido es {last_name}"
print('v3', template)