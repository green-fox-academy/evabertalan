#def f(n):
#    if n==0:
#        return

#    print("hello")
#    f(n-1)

#f(5)
#ez olyan mint egy for ciklus


#fibonacci
#R(0)=0
#R(1)=1
#R(n)=R(n-1)+R(n-2)


#def fibo(n):
#    if n==0:
#        print(0)
#        return
#    elif n==1:
#        print(1)
#    else:
#        print((n-1)+(n-2))
#        return fibo(n-1)

#fibo(11)


def fibo(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return fibo(n-1) + fibo(n-2)

res=fibo(21)
print(res)
