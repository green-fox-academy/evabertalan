my_file = open("4_encoded_zen_lines.txt", "r")
out_file=open("4_encoded_zen_lines_megoldva.txt", "w")

text=my_file.read()
decode=""

for i in text:
    if i=='\n' or i==' ':
        character=i
        decode+=character
    else:
        character=chr(ord(i)-1)
        decode+=character

out_file.write(decode)

my_file.close()
out_file.close()
