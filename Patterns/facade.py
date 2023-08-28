class Amplifier:
    tuner = None
    player = None

    def __init__(self):
        pass
    
    def on(self):
        print('엠프가 켜졌습니다.')

    def off(self):
        print('엠프가 꺼졌습니다.')

    def setStreamingPlayer(self, player):
        self.player = player
        print('엠프를 스트리밍 플레이어와 연결합니다.')

    def setStereoSound(self):
        pass

    def setSurroundSound(self):
        print('엠프를 서라운드 모드로 설정합니다(5.1채널).')

    def setTuner(self):
        pass

    def setVolume(self, vol):
        print(f'엠프 볼륨을 {vol}로 설정합니다.')

    def __repr__(self):
        pass

class Tuner:
    amplifier = None

    def __init__(self):
        pass

class StreamingPlayer:
    amplifier = None

    def __init__(self):
        pass

    def on(self):
        print('스트리밍 플레이어가 켜졌습니다.')

    def off(self):
        print('스트리밍 플레이어가 꺼졌습니다.')

    def play(self, movie):
        self.movie = movie
        print(f'스트리밍 플레이어에서 \"{self.movie}\"를 재생합니다.')

    def stop(self):
        print(f'스트리밍 플레이어에서 \"{self.movie}\" 재생을 종료합니다.')

class Projecter:
    player =None

    def __init__(self):
        pass

    def on(self):
        print('프로젝터가 켜졌습니다.')

    def off(self):
        print('프로젝터가 꺼졌습니다.')

    def wideScreenMode(self):
        print('프로젝터 화면 비율을 와이드 모드로 설정합니다(16:9 비율).')

class Screen:
    def __init__(self):
        pass

    def up(self):
        print('스크린이 올라갑니다.')

    def down(self):
        print('스크린이 내려옵니다.')

    def __repr__(self):
        pass

class PopcornPopper:
    def __init__(self):
        pass

    def on(self):
        print('팝콘 기계가 켜졌습니다.')

    def off(self):
        print('팝콘 기계가 꺼졌습니다.')

    def pop(self):
        print('팝콘 기계에서 팝콘을 튀기고 있습니다.')

    def __repr__(self):
        pass

class TheaterLights:
    def __init__(self):
        pass

    def on(self):
        print('조명이 켜졌습니다.')

    def off(self):
        print('조명이 꺼졌습니다.')

    def dim(self, light):
        print(f'조명의 밝기를 {light}%로 설정합니다.')

    def __repr__(self):
        pass

class HomeTheaterFacade:
    amp = None
    tuner = None
    player = None
    projector = None
    lights = None
    screen = None
    popper = None

    def __init__(self, amp, tuner, player, projector, screen, lights, popper) :
        self.amp = amp
        self.tuner = tuner
        self.player = player
        self.projector = projector
        self.screen = screen
        self.lights = lights
        self.popper = popper

    def watchMovie(self, movie):
        print('영화 볼 준비 중')
        self.popper.on()
        self.popper.pop()
        self.lights.dim(10)
        self.screen.down()
        self.projector.on()
        self.projector.wideScreenMode()
        self.amp.on()
        self.amp.setStreamingPlayer(self.player)
        self.amp.setSurroundSound()
        self.amp.setVolume(5)
        self.player.on()
        self.player.play(movie)

    def endMovie(self):
        print('홈시어터를 끄는 중')
        self.popper.off()
        self.lights.on()
        self.screen.up()
        self.projector.off()
        self.amp.off()
        self.player.stop()
        self.player.off()

if __name__ == '__main__':
    amp = Amplifier()
    tuner = Tuner()
    player = StreamingPlayer()
    projector = Projecter()
    screen = Screen()
    lights = TheaterLights()
    popper = PopcornPopper()

    homeTheater = HomeTheaterFacade(amp, tuner, player, projector, screen, lights, popper)
    
    homeTheater.watchMovie('인디아나 존스:레이더스')
    homeTheater.endMovie()