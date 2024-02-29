from agent import Agent
from human import Human
from game import TicTacToe

finishLoop = False

bot = Agent("Computer", epsilon=0)
bot.loadPolicy("policy_p1")

playerName = input("Enter your name: ")

while not finishLoop:
    human = Human(playerName)

    game = TicTacToe(bot, human)
    game.playWithHuman()

    print("If wish to play another game. Press\n    - 0 to Continue\n    - 1 to Quit")
    index = int(input("Enter your Choice: "))

    finishLoop = index==1