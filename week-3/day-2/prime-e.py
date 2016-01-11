num=79
b=2

prime=True
while b<=(num**0.5):
    if num%b==0:
        prime=False
        print('nem prim')
        break
    else:
        print('prim')
        break
    b+=1
