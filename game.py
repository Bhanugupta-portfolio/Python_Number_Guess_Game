import random
r = random.randint(1 , 30)
print('\nLets start the Game: Guess the Correct Number........\n')
while True:
    inp = int(input("Enter the number you think will be Guess By computer  Between( 1 to 30 ) = \n"))
    if inp < r:
        print('\nTry , Greater number Then This\n')
        print("-----------------------------------------------------\n")
    elif inp > r:
        print('\nTry Try dont cry,small number Then This\n')
        print("-----------------------------------------------------\n")
    else:
        print('\n....Congrats You Guess the  Correct Number')

        break



