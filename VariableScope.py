#Local and Global Scope

data1 = 50000
data = 10
def myFun():
    data = 100
    print(data)
    def myInnerFun():
        print(data)

    myInnerFun()

myFun()
print(data)

def myFunction():
    data1 = 1
    print("Local Variable : " ,data1)

myFunction()
print("Global Variable : ", data1)