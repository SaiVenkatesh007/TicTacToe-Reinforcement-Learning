from agent import Agent
from game import TicTacToe

# Creating Agents
p1 = Agent("p1")
p2 = Agent("p2")

# Creating Game
game = TicTacToe(p1, p2)

# Training the Agents
print("Training: ")
game.playWithBot(50000)

# Saving Policies
p1.savePolicy()
p2.savePolicy()
