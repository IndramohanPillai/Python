def my_function():
    print("Hello World..!")

def my_parameterized_function(name, age):
    print("Hi I am", name, "my age is", age)

def my_parameterized_arbitrary_arguments_function(*persons):
    print(persons[0])
    for p in persons:
        print(p)

def my_keyword_arguments_function(name,age,city):
    message = "Hello {}, you are {} years old and lives in {}".format(name,age,city)
    print(message)

def my_parameterized_keyvalue_arbitrary_arguments_function(**persons):
    print("___________________________________________________________")
    for key in persons:
        print(key,'=',persons[key])

def my_keyword_arguments_defaultvalue_function(name,age,city='Pune'):
    message = "Hello {}, you are {} years old and lives in {}".format(name,age,city)
    print(message)

def my_collections_type_function(fruits):
    for f in fruits:
        print(f)

def my_return_function(name,age,city='Mumbai'):
    #return "Hello {}, you are {} years old and lives in {}".format(name,age,city)
    #or
    message = "Hello {}, you are {} years old and lives in {}".format(name, age, city)
    return message

def my_empty_functions():
    pass #If I dont give pass it throws indentation error.

my_function()
my_parameterized_function("Indramohan", 30)
my_parameterized_arbitrary_arguments_function('Indramohan','Indramohan','Indramohan','Sonali','Arpita','Madhavi')

my_keyword_arguments_function("Indramohan", 30, "Hoofddorp, Netherlands")
# or with by key value pair
my_keyword_arguments_function(name="Indramohan", age=30, city="Hoofddorp, Netherlands")
# or with not in sequence with key value pair
my_keyword_arguments_function(city="Hoofddorp, Netherlands", name="Indramohan", age=30)

my_parameterized_keyvalue_arbitrary_arguments_function(city="Hoofddorp, Netherlands", name="Indramohan", age=30)

my_keyword_arguments_defaultvalue_function('Indramohan',30)
my_keyword_arguments_defaultvalue_function('Indramohan',30,'Amsterdam')

my_collections_type_function(['apple','pineapple','kiwi'])
my_collections_type_function({'apple','pineapple','kiwi'})
my_collections_type_function(('apple','pineapple','kiwi'))

print(my_return_function('Indramohan',30))