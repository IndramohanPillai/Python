#String data type
nameStr = 'Indramohan'
print(type(nameStr))
nameCharAsStr = 'a'
print(type(nameCharAsStr))

#Integer data type
dataInt = 100
print(type(dataInt))

#Float data type
dataFloat = 10.23
print(type(dataFloat))

#ComplexNumber data type
dataComplex = 10 + 10J
print(type(dataComplex))

#List data type
namesList = ['Indramohan','Indramohan','Indramohan','Sonali','Arpita','Madhavi']
print(type(namesList))

#Tuple data type
namesTuple = ('Indramohan','Indramohan','Indramohan','Sonali','Arpita','Madhavi')
print(type(namesTuple))

#Range data type
numbers = range(10)
print(type(numbers))

#Dictonary data type
fruitsRate = {
    'Apple' : 100,
    'Grapes' : 400,
    'Kiwi' : 800
}
print(type(fruitsRate))

#Set data type
namesSet = {'Indramohan','Indramohan','Indramohan','Sonali','Arpita','Madhavi'}
print(type(namesSet))

#FrozenSet data type
namesFrozenSet = frozenset(namesSet)
print(type(namesFrozenSet))

#Boolean data type
x = True
print(type(x))

#Byte data type
x = b'IP'
print(type(x))

#ByteArray
br = bytearray(10)
print(type(br))

#MemoryView data type
mv = memoryview(bytes(100))
print(type(mv))

#NoneType data type (its a kind of NULL)
n = None
print(type(n))