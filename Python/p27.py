def fact(x):
    if x==1:
        return 1
    else:
        return x*fact(x-1)
    
print(fact(8))

def outer(text):
    #text=text
    print(text)
    def inner():
        print(text)
    inner()

outer('Hello Python')


