my_file = open("3_duplicated_chars.txt", "r")
out_file=open("3_duplicated_chars_megoldva.txt", "w")

text=my_file.read()
lines=text.split('\n')
for i in lines:
    i=i[::2]
    out_file.write(i+'\n')

my_file.close()
out_file.close()
