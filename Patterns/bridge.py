class RemoteControl:
    def on(self):
        pass

    def off(self):
        pass

    def setChannel(self):
        pass

class ConcreteRemote(RemoteControl):
    def on(self):
        return super().on()
    
    def off(self):
        return super().off()
    
    def setChannel(self, channel):
        self.channel = channel
    
    def nextChannel(self):
        self.setChannel(self.channel+1)
    
    def previousChannel(self):
        self.setChannel(self.channel-1)

class TV(RemoteControl):
    def on(self):
        return super().on()
    
    def off(self):
        return super().off()
    
    def turnChannel(self, channel):
        self.channel = channel

class RCA(TV):
    def on(self):
        return super().on()
    
    def off(self):
        return super().off()
    
    def turnChannel(self, channel):
        return super().turnChannel(channel)
    
class Sony(TV):
    def on(self):
        return super().on()
    
    def off(self):
        return super().off()
    
    def turnChannel(self, channel):
        return super().turnChannel(channel)