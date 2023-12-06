def cal(a,b):
    """This is Docstring"""
    sum=a+b
    sub=a-b
    mul=a*b
    div=a//b
    return sum,sub,mul,div
t=cal(20,30)
print(t)
print(cal.__doc__)
