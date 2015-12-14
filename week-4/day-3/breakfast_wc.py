filename="breakfast.txt"

def wc(filename):
    input_file=open(filename)
    text=input_file.read()
    lines=len(text.split())
    input_file.close()
    return len(text), lines

print(wc(filename))
