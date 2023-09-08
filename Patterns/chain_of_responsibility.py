class RemoteControl:
    def __init__(self) -> None:
        self.successor = self

    def handleRequest(self):
        pass

class SpamHandler(RemoteControl):
    def handleRequest(self):
        return super().handleRequest()
    
class FanHandler(RemoteControl):
    def handleRequest(self):
        return super().handleRequest()
    
class ComplateHandler(RemoteControl):
    def handleRequest(self):
        return super().handleRequest()
    
class NewLocHandler(RemoteControl):
    def handleRequest(self):
        return super().handleRequest()