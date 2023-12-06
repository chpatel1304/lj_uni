def armstrong(num):
    order = len(str(num))
    sum = 0
    temp = num
    while temp > 0:
           digit = temp % 10
           sum += digit ** order
           temp //= 10
    if num == sum:
        print(num,"is an Armstrong number")
    else:
        print(num,"is not an Armstrong number")
num=int(input("Enter Number To check ?"))
armstrong(num)
