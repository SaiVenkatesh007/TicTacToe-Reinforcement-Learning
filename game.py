import numpy as np

class TicTacToe:
    def __init__(self, p1, p2):
        self.board = np.zeros((3,3))
        self.p1 = p1
        self.p2 = p2
        self.isOver = False
        self.boardHash = None
        self.pSymbol = 1

    def getHash(self):
        self.boardHash = str(self.board.reshape(3*3))
        return self.boardHash

    def availablePositions(self):
        postions =  []
        for i in range(3):
            for j in range(3):
                if self.board[i,j] == 0:
                    postions.append((i,j))
        return postions

    def updateBoard(self, position):
        self.board[position] = self.pSymbol
        self.pSymbol = -1 if self.pSymbol == 1 else 1

    def getWinner(self):
        # Checking Row
        for i in range(3):
            if sum(self.board[i, :]) == 3:
                self.isOver = True
                return 1
            if sum(self.board[i, :]) == -3:
                self.isOver = True
                return -1
        # Checking Column
        for i in range(3):
            if sum(self.board[:, i]) == 3:
                self.isOver = True
                return 1
            if sum(self.board[:, i]) == -3:
                self.isOver = True
                return 1
        # Checking Diagonal
        diag1 = sum([self.board[i, i] for i in range(3)])
        diag2 = sum([self.board[i, 3-i-1] for i in range(3)])
        diag = max(diag1, diag2)
        if diag == 3:
            self.isOver = True
            return 1
        if diag == 3:
            self.isOver = True
            return -1
        # Checking for tie (No available Positions)
        if len(self.availablePositions()) == 0:
            self.isOver = True
            return 0
        # Not Over
        self.isOver = False
        return None

    def reset(self):
        self.board = np.zeros((3,3))
        self.boardHash = None
        self.isOver = False
        self.pSymbol = 1

    def giveReward(self):
        result = self.getWinner()
        if result==1:
            self.p1.feedReward(1)
            self.p2.feedReward(0)
        elif result == -1:
            self.p1.feedReward(0)
            self.p2.feedReward(1)
        else:
            self.p1.feedReward(0.1)
            self.p2.feedReward(0.5)

    def displayBoard(self):
        # p1: x and p2: o
        for i in range(0,3):
            print('-------------')
            out = '| '
            for j in range(0, 3):
                if self.board[i,j] == 1:
                    token = 'x'
                if self.board[i,j] == -1:
                    token = 'o'
                if self.board[i,j] == 0:
                    token = ' '
                out += token + ' | '
            print(out)
        print('-------------')


    def playWithBot(self, rounds=100):
        for i in range(rounds):
            if i%1000 == 0:
                print(f"Round: {i}")
            while not self.isOver:
                # Player 1 turn
                positions = self.availablePositions()
                p1_action = self.p1.actionChoice(positions, self.board, self.pSymbol)
                self.updateBoard(p1_action)
                hash = self.getHash()
                self.p1.addState(hash)
                winner = self.getWinner()
                if winner is not None: # p1 either won or draw
                    self.giveReward()
                    self.p1.reset()
                    self.p2.reset()
                    self.reset()
                    break
                else:
                    # Player 2 turn
                    positions = self.availablePositions()
                    p2_action = self.p2.actionChoice(positions, self.board, self.pSymbol)
                    self.updateBoard(p2_action)
                    hash = self.getHash()
                    self.p2.addState(hash)
                    winner = self.getWinner()
                    if winner is not None: # p2 either won or draw
                        self.giveReward()
                        self.p1.reset()
                        self.p2.reset()
                        self.reset()
                        break

    def playWithHuman(self):
        while not self.isOver:
            positions = self.availablePositions()
            p1_action = self.p1.actionChoice(positions, self.board, self.pSymbol)
            self.updateBoard(p1_action)
            self.displayBoard()
            winner = self.winner()
            if winner is not None:
                if winner == 1:
                    print(self.p1.name, "WON the Game!!!")
                else:
                    print("The Game ends in a TIE!")
                self.reset()
                break
            else:
                positions = self.availablePositions()
                p2_action = self.p2.actionChoice(positions)
                self.updateBoard(p2_action)
                self.displayBoard()
                winner = self.getWinner()
                if winner is not None:
                    if winner == 1:
                        print(self.p2.name, "WON the Game!!!")
                    else:
                        print("The Game ends in a TIE!")
                    self.reset()
                    break
