day = 14
while True:
    guess_of_the_user = int(input("Guess the day I was born in November: "))
    if guess_of_the_user == 14:
        print("Congrats!! your correct!! <3 ")
        break   
    else:
        print("Fake friend! try again!")