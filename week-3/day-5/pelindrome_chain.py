def palindrome_chain_length(n):
    if str(n)==str(n)[::-1]:
       print(0)
    else:
        a=[]
        a.append(n)
        for i in a:
            invers=str(i)[::-1]
            b=i+int(invers)
            if str(b)==str(b)[::-1]:
                print((len(a)))
            else:
                a.append(b)

palindrome_chain_length(3)
