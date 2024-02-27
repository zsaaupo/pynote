'''Decorator'''
print(__doc__)

### One ###
def decorator(func):
    print("start")
    return func
    
@decorator
def helloWorld():
    return "Hello World!"


### Two ###
def decorator(func):
    def wapper():
        print("start")
        print(func())
        print("end")
        return func
    return wapper
    
@decorator
def helloWorld():
    return "Hello World!"
