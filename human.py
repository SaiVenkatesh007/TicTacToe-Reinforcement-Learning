class Human:
    def __init__(self, name):
        self.name = name

    def actionChoice(self, positions):
        while True:
            print("Provide input co-ord (0-2)")
            row = int(input("Row: "))
            col = int(input("Column: "))
            action = (row, col)
            if action in positions:
                return action

    def addState(self, state):
        pass

    def feedReward(self):
        pass

    def reset(self):
        pass
