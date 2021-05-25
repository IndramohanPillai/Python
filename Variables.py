#1. Variable name must start with a letter or a underscore and not a number
#2. Variable names can contains only alpha-numeric values and underscores
#3. Varaible names are case sensitive(name, Name, nAme, NAME all the different variables)

name = 'Aaaaaaaa'
Name = 'Baaaaaaaa'
nAme = 'Caaaaaaaaaaa'
NAME = 'Daaaaaaaaaaaaaa'
person_name = 'Indramohan'
personLocation = 'Netherlands'
_personPostal = '2132BH'
print(name)
print(nAme)
print(Name)
print(NAME)
print(personLocation)
print(person_name)
print(_personPostal)

data = 100
print(type(data))
data = 100.12331
print(type(data))
data = 'IP'
print(type(data))


x = str('65')
print(type(x))