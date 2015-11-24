def greet(name):
    print('Hello '+ name + '!')

greet('Tomi')
greet('Sanyi')



def add(a,b):
    return a+b

num=add(3,4)

print(num)



def is_even(num):
    return num%2

a=is_even(13)

if a==0:
    print('even')
else:
    print('odd')



def is_odd(a):
    if a%2!=0:
        return 'odd'
    else:
        return 'even'

print(is_odd(8))
