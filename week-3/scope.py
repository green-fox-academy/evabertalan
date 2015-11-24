#global scope
#n=2
#
#def f():
#    #n=1
#    print("local", n)
#
#f() #-->1
#print("global", n)


#curr_room="Hall"

#def moove(dir, room):
#    if dir=="north" and room=="Hall":
#        return "Living Room"
#    elif dir=="south":
#        return "Kitchen"
#    else:
#        return None

#curr_room=move("north")


def c():
    r=1
    print(r) #ey csak lokalis r

c()
print(r) #ide amiatt nem ir ki ertelmet, mert globalis r es nem volt global megadva
