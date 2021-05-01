from random import choice
from time import sleep
def flip():
    choices = ['HEADS', 'TAILS']
    return choice(choices)
def main(rounds):
    score = 0
    for round in range(1,rounds + 1):
        print('Round:', round)
        choice = input('Heads or Tails?').upper()
        if choice == 'H':
            choice = 'HEADS'
        if choice == 'T':
            choice = 'TAILS'
        flips = flip()
        if choice == flips:
            print('You got it! The coin landed on:', flips)
            score += 1
        else:
            print('Oof, you got it wrong. The coin landed on:', flips)
    print('Your score: ' + str(score) + '/'+ str(rounds))
main(5)