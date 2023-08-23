class Light:
    def __init__(self, pos):
        self.pos = pos

    def on(self):
        print(f'{self.pos} 조명이 켜졌습니다.')
    
    def off(self):
        print(f'{self.pos} 조명이 꺼졌습니다.')

class CeilingFan:
    def __init__(self, pos):
        self.pos = pos
        self.speed = 0

    def high(self):
        print(f'{self.pos} 선풍기 속도가 HIGH로 설정되었습니다.')
        self.speed = 3

    def medium(self):
        print(f'{self.pos} 선풍기 속도가 MEDIUM으로 설정되었습니다.')
        self.speed = 2

    def low(self):
        print(f'{self.pos} 선풍기 속도가 LOW로 설정되었습니다.')
        self.speed = 1

    def off(self):
        print(f'{self.pos} 선풍기가 꺼졌습니다.')
        self.speed = 0

    def getSpeed(self):
        return self.speed

class GarageDoor:
    def __init__(self, pos):
        self.pos = pos

    def up(self):
        print(f'{self.pos} 문이 열렸습니다.')
    
    def down(self):
        print(f'{self.pos} 문이 닫혔습니다.')
    
    def stop(self):
        print(f'{self.pos} 문이 멈췄습니다.')

    def lightOn(self):
        print(f'{self.pos} 조명이 켜졌습니다.')
    
    def lightOff(self):
        print(f'{self.pos} 조명이 꺼졌습니다.')

class Stereo:
    def __init__(self, pos):
        self.pos = pos
        self.vol = 0

    def on(self):
        print(f'{self.pos} 오디오가 켜졌습니다.')

    def off(self):
        print(f'{self.pos} 오디오가 꺼졌습니다.')

    def setCd(self):
        print(f'{self.pos} 오디오에서 CD가 재생됩니다.')

    def setDvd(self):
        print(f'{self.pos} 오디오에서 DVD가 재생됩니다.')

    def setRadio(self):
        print(f'{self.pos} 오디오에서 라디오가 재생됩니다.')

    def setVolume(self, vol):
        self.vol = vol
        print(f'{self.pos} 오디오의 볼륨이 {self.vol}로 설정되었습니다.')

    def getVolume(self):
        return self.vol
    
class TV:
    def __init__(self, pos):
        self.pos = pos
        self.channel = 0
        self.vol = 0

    def on(self):
        print(f'{self.pos} TV가 켜졌습니다.')
    
    def off(self):
        print(f'{self.pos} TV가 꺼졌습니다.')

    def setInputChannel(self, channel):
        self.channel = channel
        print(f'TV 채널이 {self.channel}로 설정되었습니다.')

    def setVolume(self, vol):
        self.vol = vol
        print(f'TV 볼륨이 {self.vol}로 설정되었습니다.')

    def getChannel(self):
        return self.channel
    
    def getVolume(self):
        return self.vol

class Hottub:
    def __init__(self):
        self.isOn = False
        self.temperature = 36

    def on(self):
        self.isOn = True
    
    def off(self):
        self.isOn = False

    def circulate(self):
        pass
    
    def jetsOn(self):
        pass
    
    def jetsOff(self):
        pass

    def setTemperature(self, temperature):
        if self.isOn :
            self.temperature = temperature
            print(f'욕조 온도를 {self.temperature}도로 설정합니다.')
            print(f'현재 욕조 온도: {self.temperature}도')
        else :
            self.temperature = temperature
            print(f'욕조 온도를 {self.temperature}도로 설정합니다.')
    
    def getTemperature(self):
        return self.temperature