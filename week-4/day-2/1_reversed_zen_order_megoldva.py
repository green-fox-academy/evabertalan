my_file = open("1_reversed_zen_order.txt", "r")
out_file=open("1_reversed_zen_order_megoldva.txt", "w")


lines=my_file.readlines()
lines=lines[::-1]
x=''
for i in lines:
    x=x+i
out_file.write(x)

my_file.close()
out_file.close()
