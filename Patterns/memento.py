class MasterGameObject:
    def __init__(self) -> None:
        self.gameState = None

    def getCurrentState(self):
        return self.gameState
    
    def restoreState(self, savedState):
        self.gameState = savedState

class GameMemento(MasterGameObject):
    def __init__(self) -> None:
        self.savedGameState = super().getCurrentState()

if __name__ == '__main__':
    saved = MasterGameObject().getCurrentState()

    MasterGameObject().restoreState(saved)
