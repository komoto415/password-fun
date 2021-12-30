# refactor for input or command line arguments c:

from random import seed, choice
counter = 1
coin_throws = 0b1
lottery_numbers = 13454443315
seed((coin_throws^lottery_numbers)*counter)
choices = range(1,7)
print("You rolled a", choice(choices))