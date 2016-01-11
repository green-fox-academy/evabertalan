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


from math import factorial
def zeros(n):
    f=factorial(n)
    n=1
    while n<=1000:
        a=f%(10**n)
        if a==0:
            n+=1
        else:
            b=n-1
            print(b)
            break
zeros(1000)


from math import factorial
def zeros(n):
    b=0
    f=factorial(n)
    for i in str(f)[::-1]:
        if i=="0":
          b+=1
        else:
            print(b)
            break
zeros(1000)
