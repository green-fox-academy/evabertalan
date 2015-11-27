from random import randint

def get_integer():
    number = int(input("Enter an integer (0-10): "))
    return number

number_to_guess = randint(0, 10)
number_of_guessis = 5

while number_of_guessis >= 0:
    if number_of_guessis == 0:
        print("nyomi vagy")
        break
    else:
        try:
            guess=get_integer()
        except ValueError:
            print("You entered a wrong value.")
        else:
            if guess == number_to_guess:
                print("eltalaltad")
                break
            elif guess < number_to_guess:
                print("nem talalt, nagyobb szam kell")
                number_of_guessis -= 1
            else:
                print("nem talalt, kisebb szam kell")
                number_of_guessis -= 1
