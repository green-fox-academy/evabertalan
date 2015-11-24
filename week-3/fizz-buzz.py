a=0

while a<101:
    if (a%3==0 and a%5==0) or ('3' in str(a) and '5' in str(a)):
        print('fizz-buzz')
    elif (a%5==0) or ('5' in str(a)):
        print('buzz')
    elif (a%3==0) or ('3' in str(a)):
        print('fizz')
    else:
        print(a)
    a+=1
