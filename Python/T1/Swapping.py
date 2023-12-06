def swap(input_val):
    input_val = [i for i in str(input_val)]
    hold = input_val[0]
    input_val[0] = input_val[-1]
    input_val[-1] = hold
    input_val = ''.join(input_val)
    return int(input_val)

n=int(input("Enter Number : "))
print(swap(n))

