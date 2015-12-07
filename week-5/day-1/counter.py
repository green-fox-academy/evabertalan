def count_letters(input_str):
    output={}
    for char in input_str:
        if char in output:
            output[char]+=1
        else:
            output[char]=1
    return output
