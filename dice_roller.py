import random

def main():
    player_1 = input('Hello! Player 1: what is your name?')
    dice_rolls = int(input('Hi! How many dice would you like to roll? '))
    dice_size = int(input('How many sides are the dice? '))
    dice_sum = 0
    for i in range(0,dice_rolls):
        roll = random.randint(1,dice_size)
        dice_sum = dice_sum + roll
        if roll==1:
            print(f'You rolled a {roll}! Critical Fail')
        elif roll == dice_size:
            print(f'You rolled a {roll}! Critical Success!')
        else:
            print(f'You rolled a {roll}')
    print(f'{player_1}, you have rolled a total of {dice_sum}')

if __name__== "__main__":
  main()
  
  