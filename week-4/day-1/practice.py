af=123

def double(number):
    return number*2

af=double(af)

print(af)



ag="kuty"
def adder(word):
    return word+"a"

ag=adder(ag)

print(ag)




ag2=['rep', 'macsk', 'cic', 'alm', 'Ann', 'kacs']

for i in range(len(ag2)):
    ag2[i]=adder(ag2[i])

print(ag2)


numbers=[4,5,6,7,8,9,10]

def list_sum(n):
    summ=0
    for i in range(len(n)):
        summ=n[i]+summ
    return summ

numbers=list_sum(numbers)
print(numbers)
