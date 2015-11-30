def factorial(numb):
    f=1
    for i in range(1,numb+1):
        f=i*f
    return f

print(factorial(6))


def factorial_recursive(num):
    if num==1:
        return 1
    else:
        return factorial_recursive(num-1)*num

print(factorial_recursive(8))
