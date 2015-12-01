my_file = open("2_reversed_zen_lines.txt", "r")
out_file=open("2_reversed_zen_lines_megoldva.txt", "w")

text=my_file.read()
lines=text.split('\n')
for i in lines:
    i=i[::-1]
    out_file.write(i+'\n')

my_file.close()
out_file.close()
