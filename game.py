import random
def game():
    
    while True:
        user = input("Enter a Number( 1 to 10) and q(Quit) = ")
        computer = random.randrange(1,11)
        if user == str(computer):
            print("You Win!\n Horray \n Well Done")
            break
        elif int(user) != computer:
            print("Try Again")
            print("the number was ",computer)
        else:
            print("Invalid Input")

if __name__ == '__main__':
    game()



