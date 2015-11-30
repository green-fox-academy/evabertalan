class Car:
    def __init__(self, color, car_type, km):
        if type(color)!=str:
            raise Exception('color is not sting')
        self.color=color
        self.car_type=car_type
        self.km=km

    def ride(self, km):
        self.km+=km

    def getMiles(self):
        return self.km*0.6213


tesla=Car('pink', 'Tesla S', 1200)
lada=Car('green', 'Lada  1200', 40000)

tesla.has_eye_brows=True

tesla.ride(220)

print(tesla.km)
print(tesla.getMiles())
