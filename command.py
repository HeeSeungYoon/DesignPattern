from device import *

class Command:
    def execute(self):
        pass

    def undo(self):
        pass

class NoCommand(Command):
    def execute(self):
        pass

    def undo(self):
        pass

class MacroCommand(Command):
    commands = []

    def __init__(self, commands):
        self.commands = commands

    def execute(self):
        for i in range(len(self.commands)):
            self.commands[i].execute()

    def undo(self):
        for i in range(len(self.commands)):
            self.commands[i].undo()

class LightOnCommand(Command):
    light = None
    
    def __init__(self, light):
        self.light = light        

    def execute(self):
        self.light.on()

    def undo(self):
        self.light.off()

class LightOffCommand(Command):
    light = None

    def __init__(self, light):
        self.light = light        

    def execute(self):
        self.light.off()
    
    def undo(self):
        self.light.on()

class CeilingFanHighCommand(Command):
    ceilingFan = None
    prevSpeed = 0

    def __init__(self, ceilingFan):
        self.ceilingFan = ceilingFan

    def execute(self):
        self.prevSpeed = self.ceilingFan.getSpeed()
        self.ceilingFan.high()

    def undo(self):
        if self.prevSpeed == 3:
            self.ceilingFan.high()
        elif self.prevSpeed == 2:
            self.ceilingFan.medium()
        elif self.prevSpeed == 1:
            self.ceilingFan.low()
        elif self.prevSpeed == 0:
            self.ceilingFan.off()

class CeilingFanMediumCommand(Command):
    ceilingFan = None
    prevSpeed = 0

    def __init__(self, ceilingFan):
        self.ceilingFan = ceilingFan

    def execute(self):
        self.prevSpeed = self.ceilingFan.getSpeed()
        self.ceilingFan.medium()

    def undo(self):
        if self.prevSpeed == 3:
            self.ceilingFan.high()
        elif self.prevSpeed == 2:
            self.ceilingFan.medium()
        elif self.prevSpeed == 1:
            self.ceilingFan.low()
        elif self.prevSpeed == 0:
            self.ceilingFan.off()

class CeilingFanLowCommand(Command):
    ceilingFan = None
    prevSpeed = 0

    def __init__(self, ceilingFan):
        self.ceilingFan = ceilingFan

    def execute(self):
        self.prevSpeed = self.ceilingFan.getSpeed()
        self.ceilingFan.low()

    def undo(self):
        if self.prevSpeed == 3:
            self.ceilingFan.high()
        elif self.prevSpeed == 2:
            self.ceilingFan.medium()
        elif self.prevSpeed == 1:
            self.ceilingFan.low()
        elif self.prevSpeed == 0:
            self.ceilingFan.off()


class CeilingFanOffCommand(Command):
    ceilingFan = None
    prevSpeed = 0

    def __init__(self, ceilingFan):
        self.ceilingFan = ceilingFan

    def execute(self):
        self.prevSpeed = self.ceilingFan.getSpeed()
        self.ceilingFan.off()
    
    def undo(self):
        if self.prevSpeed == 3:
            self.ceilingFan.high()
        elif self.prevSpeed == 2:
            self.ceilingFan.medium()
        elif self.prevSpeed == 1:
            self.ceilingFan.low()
        elif self.prevSpeed == 0:
            self.ceilingFan.off()

class GarageDoorUpCommand(Command):
    garageDoor = None

    def __init__(self, garageDoor):
        self.garageDoor = garageDoor

    def execute(self):
        self.garageDoor.up()
        self.garageDoor.lightOn()

class GarageDoorDownCommand(Command):
    garageDoor = None

    def __init__(self, garageDoor):
        self.garageDoor = garageDoor

    def execute(self):
        self.garageDoor.down()
        self.garageDoor.lightOff()

class StereoOnWithCDCommand(Command):
    stereo = None

    def __init__(self, stereo):
        self.stereo = stereo

    def execute(self):
        self.stereo.on()
        self.stereo.setCd()
        self.stereo.setVolume(11)

    def undo(self):
        self.stereo.off()

class StereoOffCommand(Command):
    stereo = None
    prevVol = 0

    def __init__(self, stereo):
        self.stereo = stereo

    def execute(self):
        self.prevVol = self.stereo.getVolume()
        self.stereo.off()

    def undo(self):
        self.stereo.on()
        self.stereo.setCd()
        self.stereo.setVolume(self.prevVol)

class TVOnCommand(Command):
    tv = None

    def __init__(self,tv):
        self.tv = tv

    def execute(self):
        self.tv.on()
        self.tv.setInputChannel(1)
        self.tv.setVolume(10)
    
    def undo(self):
        self.tv.off()
    

class TVOffCommand(Command):
    tv = None
    prevChannel = 0
    prevVol = 0

    def __init__(self,tv):
        self.tv = tv

    def execute(self):
        self.prevChannel = self.tv.getChannel()
        self.prevVol = self.tv.getVolume()
        self.tv.off()

    def undo(self):
        self.tv.on()
        self.tv.setInputChannel(self.prevChannel)
        self.tv.setVolume(self.prevVol)

class HottubOnCommand(Command):
    hottub = None

    def __init__(self, hottub):
        self.hottub = hottub

    def execute(self):
        self.hottub.on()
        self.hottub.setTemperature(40)

    def undo(self):
        self.hottub.off()
        self.hottub.setTemperature(36)

class HottubOffCommand(Command):
    hottub = None
    prevTemperature = 0

    def __init__(self, hottub):
        self.hottub = hottub

    def execute(self):
        self.prevTemperature = self.hottub.getTemperature()
        self.hottub.off()
        self.hottub.setTemperature(36)

    def undo(self):
        self.hottub.on()
        self.hottub.setTemperature(self.prevTemperature)

# Invoker 클래스
class RemoteControl:
    onCommands = []
    offCommands = []
    undoCommand = None

    def __init__(self):
        for _ in range(7):
            self.onCommands.append(NoCommand())
            self.offCommands.append(NoCommand())
        self.undoCommand = NoCommand()

    def setCommand(self, slot, onCommand, offCommand):
        self.onCommands[slot] = onCommand
        self.offCommands[slot] = offCommand
    
    def onButtonWasPushed(self, slot):
        self.onCommands[slot].execute()
        self.undoCommand = self.onCommands[slot]

    def offButtonWasPushed(self, slot):
        self.offCommands[slot].execute()
        self.undoCommand = self.offCommands[slot]
        
    def undoButtonWasPushed(self):
        self.undoCommand.undo()

    def __repr__(self):
        string = '\n----------리모컨----------\n'
        for i in range(len(self.onCommands)):
            string += f'[slot {i}] {self.onCommands[i].__class__.__name__} \
                  {self.offCommands[i].__class__.__name__}\n'
        string += f'[undo] {self.undoCommand.__class__.__name__}\n'
        return string
    
if __name__ == "__main__":
    remoteControl = RemoteControl()

    light = Light('거실')
    tv = TV('거실')
    stereo = Stereo('거실')
    hottub = Hottub()

    lightOn = LightOnCommand(light)
    stereoOn = StereoOnWithCDCommand(stereo)
    tvOn = TVOnCommand(tv)
    hottubOn = HottubOnCommand(hottub)

    lightOff = LightOffCommand(light)
    stereoOff = StereoOffCommand(stereo)
    tvOff = TVOffCommand(tv)
    hottubOff = HottubOffCommand(hottub)

    partyOn = [lightOn, stereoOn, tvOn, hottubOn]
    partyOff = [lightOff, stereoOff, tvOff, hottubOff]

    partyOnMacro = MacroCommand(partyOn)
    partyOffMacro = MacroCommand(partyOff)

    remoteControl.setCommand(0, partyOnMacro, partyOffMacro)

    print(remoteControl)
    print('----- 매크로 ON -----')
    remoteControl.onButtonWasPushed(0)
    print('----- 매크로 OFF -----')
    remoteControl.offButtonWasPushed(0)
    
    print(remoteControl)
    print('----- 매크로 UNDO -----')
    remoteControl.undoButtonWasPushed()