def create_palindrome(input):
    output = input[::-1]
    print(input + output)

create_palindrome("almb")


def search_palindromes(word_list):
    a=word_list.split()
    b=[]
    for i in a:
        k=3
        while k <= len(i):
            n=0
            while (n+2)<len(i):
                if i[n:(n+k)] == i[n:(n+k)][::-1]:
                    b.append(i[n:(n+k)])
                n += 1
            k += 1
    print(b)
search_palindromes("dog goat dad duck doodle never")
