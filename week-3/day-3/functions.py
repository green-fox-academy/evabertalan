#def get_fizz(number):
    if number%3==0:
        return 'fizz'
    else:
        return number




#def fizz_buzz(minimum, maximum=100):
#    n=minimum
#    while n<=maximum:
#        if n%3==0:
#            print('fizz')
#        else:
#            print(n)
#        n+=1

#fizz_buzz(1,10)


def fizz_buzz(minimum, maximum=100):
    n=minimum
    while n<=maximum:
        print(get_fizz(n))
        n+=1

fizz_buzz(1,30)

#def is_big_number(number):
#    return number>100

#print(is_big_number(104))


#def is_big_number(number):
#    return number>100

#if is_big_number(104):
#    print('sooooo big')
#else:
    #print('nope')

#def is_big_number(number):
#    return number>100

#def print_bigness(number):
#    print('kis')
#    print(number)
#i#f is_big_number(104):
#    print('sooooo big')
#else:
#    print('nope')

#print_bigness(5)
#print_bigness(123)
