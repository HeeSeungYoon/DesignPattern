import random

class State:
    def __init__(self) -> None:
        pass

    def insertQuarter(self):
        pass

    def ejectQuarter(self):
        pass

    def turnCrank(self):
        pass

    def dispense(self):
        pass

    def refill(self):
        pass

class SoldState(State):
    def __init__(self, gumballMachine):
        self.gumballMachine = gumballMachine

    def insertQuarter(self):
        print('알맹이를 내보내고 있습니다.')

    def ejectQuarter(self):
        print('이미 알맹이를 뽑으셨습니다.')

    def turnCrank(self):
        print('손잡이는 한 번만 돌려 주세요.')

    def dispense(self):
        self.gumballMachine.releaseBall()
        if self.gumballMachine.getCount() > 0:
            self.gumballMachine.setState(self.gumballMachine.getNoQuarterState())
        else:
            print('더 이상 알맹이가 없습니다.')
            self.gumballMachine.setState(self.gumballMachine.getSoldOutState())

    def __repr__(self) -> str:
        return 'Sold state\n.'

class SoldOutState(State):
    def __init__(self, gumballMachine):
        self.gumballMachine = gumballMachine

    def insertQuarter(self):
        print('죄송합니다. 매진되었습니다.')

    def ejectQuarter(self):
         print('동전을 반환할 수 없습니다. 동전을 넣지 않았습니다.')
    
    def turnCrank(self):
         print('죄송합니다. 매진되었습니다.')
    
    def dispense(self):
         print('알맹이를 내보낼 수 없습니다.')

    def refill(self):
        self.gumballMachine.setState(self.gumballMachine.getNoQuarterState())

    def __repr__(self):
        return '매진\n'

class NoQuarterState(State):
    def __init__(self, gumballMachine):
        self.gumballMachine = gumballMachine

    def insertQuarter(self):
        print('동전을 넣으셨습니다.')
        self.gumballMachine.setState(self.gumballMachine.getHasQuarterState())

    def ejectQuarter(self):
         print('동전을 넣어주세요.')

    def turnCrank(self):
         print('동전을 넣어주세요.')

    def dispense(self):
         print('동전을 넣어주세요.')

    def __repr__(self):
        return '동전 투입 대기 중...\n'

class HasQuarterState(State):
    def __init__(self, gumballMachine):
        self.gumballMachine = gumballMachine

    def insertQuarter(self):
        print('동전은 한 개만 넣어 주세요.')

    def ejectQuarter(self):
        print('동전이 반환됩니다.')
        self.gumballMachine.setState(self.gumballMachine.getNoQuarterState())
    
    def turnCrank(self):
        print('손잡이를 돌리셨습니다.')
        winner = random.randint(1,10)
        if winner == 1 and self.gumballMachine.getCount() > 1:
            print('축하드립니다. 알맹이를 하나 더 받으실 수 있습니다.')
            self.gumballMachine.setState(self.gumballMachine.getWinnerState())
        else:
            self.gumballMachine.setState(self.gumballMachine.getSoldState())
    
    def dispense(self):
        print('알맹이를 내보낼 수 없습니다.')

    def __repr__(self):
        return 'Has quarter state.'

class WinnerState(State):  
    def __init__(self, gumballMachine):
        self.gumballMachine = gumballMachine

    def insertQuarter(self):
        print('알맹이를 내보내고 있습니다.')

    def ejectQuarter(self):
        print('이미 알맹이를 뽑으셨습니다.')

    def turnCrank(self):
        print('손잡이는 한 번만 돌려 주세요.')

    def dispense(self):
        self.gumballMachine.releaseBall()
        if self.gumballMachine.getCount() == 0:
            self.gumballMachine.setState(self.gumballMachine.getSoldOutState())
        else:
            self.gumballMachine.releaseBall()
            if self.gumballMachine.getCount() > 0:
                self.gumballMachine.setState(self.gumballMachine.getNoQuarterState())
            else:
                print('더 이상 알맹이가 없습니다.')
                self.gumballMachine.setState(self.gumballMachine.getSoldOutState())

    def __repr__(self):
        return 'Winner state.'

class GumballMachine:

    def __init__(self, location, numberGumballs):

        self.location = location
        self.soldOutState = SoldOutState(self)
        self.noQuarterState = NoQuarterState(self)
        self.hasQuarterState = HasQuarterState(self)
        self.soldState = SoldState(self)
        self.winnerState = WinnerState(self)

        self.count = numberGumballs
        if numberGumballs > 0:
            self.state = self.noQuarterState
        else:
            self.state = self.soldOutState

    def insertQuarter(self):
        self.state.insertQuarter()

    def ejectQuarter(self):
        self.state.ejectQuarter()

    def turnCrank(self):
        self.state.turnCrank()
        if self.state is self.soldState or self.state is self.winnerState:
            self.state.dispense()

    def refill(self, count):
        self.count += count
        print('알맹이가 리필되었습니다.')
        print(f'남은 개수 : {self.count}')
        self.state.refill()

    def setState(self, state):
        self.state = state
    
    def getSoldState(self):
        return self.soldState
    
    def getSoldOutState(self):
        return self.soldOutState
    
    def getNoQuarterState(self):
        return self.noQuarterState
    
    def getHasQuarterState(self):
        return self.hasQuarterState
    
    def getWinnerState(self):
        return self.winnerState

    def getCount(self):
        return self.count

    def getLocation(self):
        return self.location
    
    def getState(self):
        return self.state

    def releaseBall(self):
        print('알맹이를 내보내고 있습니다.')
        if self.count > 0:
            self.count-=1

    def __repr__(self):
        string = '\n주식회사 왕뽑기\n'
        string += '파이썬으로 돌아가는 최신형 뽑기 기계\n'
        string += f'남은 개수: {self.count}\n'
        if self.count > 0 :
            string += '동전 투입 대기중\n'
        else:
            string += '매진\n'
        
        return string

class GumballMonitor:
    def __init__(self, machine):
        self.machine = machine

    def report(self):
        print('뽑기 기계 위치: ',self.machine.getLocation())
        print(f'현재 재고: {self.machine.getCount()} 개')
        print('현재 상태: ',self.machine.getState())

import sys

if __name__ == '__main__':
    # gumballMachine = GumballMachine(5)

    # print(gumballMachine)

    # gumballMachine.insertQuarter()
    # gumballMachine.turnCrank()

    # print(gumballMachine)

    # gumballMachine.insertQuarter()
    # gumballMachine.turnCrank()
    # gumballMachine.insertQuarter()
    # gumballMachine.turnCrank()

    # print(gumballMachine)

    # gumballMachine.insertQuarter()
    # gumballMachine.turnCrank()
    # print(gumballMachine)
    # if gumballMachine.getCount() == 0:
    #     gumballMachine.refill(5)
    
    # print(gumballMachine)
    # gumballMachine.insertQuarter()
    # gumballMachine.turnCrank()
    # print(gumballMachine)

    args = sys.argv[1:]
    if len(args) < 2:
        print('GumballMachine <name> <inventory>')
        sys.exit()
    
    count = int(args[1])
    gumballMachine = GumballMachine(args[0], count)

    monitor = GumballMonitor(gumballMachine)

    monitor.report()