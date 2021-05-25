name = input("Enter your name :")
age = input("Enter your age : ")


try:
    age = int(age)
    print(type(age),age)
    print("Hello {}, your age is {}".format(name,age))
except ValueError:
    print("entered age is must be number")