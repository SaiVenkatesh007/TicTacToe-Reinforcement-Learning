from agent import Agent
from human import Human
from game import TicTacToe

p1 = Agent("Computer", epsilon=0)
p1.loadPolicy("policy_p1")

p2 = Human("Human")

game = TicTacToe(p1, p2)
game.playWithHuman()
