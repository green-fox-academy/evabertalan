b=2
i=1
prime=True

while i<=100:
    while b<=(i**0.5):
        if i%b==0:
            prime=False
            print(i)
        else:
            print('prim')
        b+=1
    i+1
