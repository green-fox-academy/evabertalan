def create_palindrome(input):
    output = input[::-1]
    print(input + output)

create_palindrome("alma")




def create_palindrome2(input2):
    n = len(input2)
    reversed=''
    for i in range(n):
        reversed = input2[i] + reversed
    print(input2 + reversed)

create_palindrome2("kutya")




def search_palindromes(word_list):
    search=word_list.split()
    palindromes=[]
    for word in search:
        k=3
        while k <= len(word):
            index=0
            while (index+2)<len(word):
                if word[index:(index+k)] == word[index:(index+k)][::-1]:
                    palindromes.append(word[index:(index+k)])
                index += 1
            k += 1
    print(palindromes)
search_palindromes("dog goat dad duck doodle never")
