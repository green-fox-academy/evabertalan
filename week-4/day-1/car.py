def initCar(color, type, km):
    car={'color': "", "type": "", "km":0}
    car['color']=color
    car['type']=type
    car['km']=km
    return car

def ride(car, km):
    car['km']+=km

lada2=initCar('yellow','Lada 1200', 4000)
tesla2=initCar('green', 'Tesla S', 1200)
ifa=initCar('brown', 'Ifa', 30000000)

lada={
'color': 'red',
'type': 'Lada 1200',
'km': 40000
}

tesla={
'color': 'pink',
'type': 'Tesla S',
'km': 1000
}


ride(ifa, 200)
print(ifa)
