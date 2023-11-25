import random

print("Hello to my first game: rock , paper , scissors")

player = input("Choose your move rock , paper and  scissor: \n").lower()
pc = random.choice(['rock' , 'paper' , 'scissor'])
print("player played: " + player)
print("pc played: " + pc)

if player == pc:
    print("it's a tie")
elif ((player == 'rock' and pc == 'scissor' ) or (player == 'paper' and pc == 'rock') or (player == 'scissor' and pc == 'paper') ):
    print("you won")
else:
    print("you lose / pc won")

