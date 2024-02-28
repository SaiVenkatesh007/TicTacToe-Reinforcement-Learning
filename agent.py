import numpy as np
import pickle

class Agent:
    def __init__(self, name, epsilon=0.3):
        self.name = name
        self.states = [] # all positions record
        self.alpha = 0.2
        self.epsilon = epsilon
        self.gamma = 0.9
        self.stateValueDict = {}

    def getHash(self, board):
        hash = str(board.reshape(3*3))
        return hash

    def actionChoice(self, postions, current_board, symbol):
        if np.random.uniform(0,1) <= self.epsilon:
            index = np.random.choice(len(postions))
            action = postions[index]
        else:
            value_max = -999
            for position in postions:
                next_board = current_board.copy()
                next_board[position] = symbol
                next_hash = self.getHash(next_board)
                value = 0 if self.stateValueDict.get(next_hash) is None else self.stateValueDict.get(next_hash)
                if value>= value_max:
                    value_max = value
                    action = position
        return action

    def addState(self, state):
        self.states.append(state)

    def feedReward(self, reward):
        for state in reversed(self.states):
            if self.stateValueDict.get(state) is None:
                self.stateValueDict[state] = 0
            self.stateValueDict[state] += self.alpha*(self.gamma*reward - self.stateValueDict[state])
            reward = self.stateValueDict[state]

    def reset(self):
        self.states = []

    def savePolicy(self):
        fileWrite = open('policy_' + str(self.name), 'wb')
        pickle.dump(self.stateValueDict, fileWrite)
        fileWrite.close()

    def loadPolicy(self, file):
        fileRead = open(file, 'rb')
        self.stateValueDict = pickle.load(fileRead)
        fileRead.close()
