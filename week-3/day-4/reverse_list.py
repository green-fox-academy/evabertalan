def reverse(in_list):
    n = len(in_list)-1
    output = []
    while n >= 0:
        output.append(in_list[n])
        n -= 1
    return output

output=reverse([1, 2, 3, 7, 8])
print(output)
