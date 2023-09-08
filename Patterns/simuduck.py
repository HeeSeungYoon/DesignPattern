# 팩토리 패턴
class AbstractDuckFactory:
    def createMallardDuck(self):
        pass

    def createRedHeadDuck(self):
        pass

    def createDuckCall(self):
        pass

    def createRubberDuck(self):
        pass

class GooseFactory:
    def createGoose(self):
        return GooseAdapter(Goose())

class CountingDuckFactory(AbstractDuckFactory):
    def createDuckCall(self):
        return QuackCounter(DuckCall())
    
    def createMallardDuck(self):
        return QuackCounter(MallardDuck())
    
    def createRedHeadDuck(self):
        return QuackCounter(RedheadDuck())
    
    def createRubberDuck(self):
        return QuackCounter(RubberDuck())

# 옵저버 패턴
class QuackObservable:
    def __init__(self) -> None:
        pass

    def registerObserver(self, observer):
        pass

    def notifyObservers(self):
        pass

class Quackable(QuackObservable):
    def __init__(self) -> None:
        pass

    def quack(self):
        pass

class Observable(QuackObservable):
    def __init__(self, duck) -> None:
        self.duck = duck
        self.observers = []

    def registerObserver(self, observer):
        self.observers.append(observer)

    def notifyObservers(self):
        for observer in self.observers:
            observer.update(self.duck)

class Observer:
    def update(self, duck):
        pass

class Quackologist(Observer):
    def update(self, duck):
        print(f'꽥꽥학자: {duck}가 방금 소리냈다.')

# 컴포지트 패턴
class Flock(Quackable):
    def __init__(self):
        self.quackers = []

    def add(self,quacker):
        self.quackers.append(quacker)

    def quack(self):
        for quacker in self.quackers:
            quacker.quack()

    def registerObserver(self, observer):
        for quacker in self.quackers:
            quacker.registerObserver(observer)
    
    def notifyObservers(self):
        return super().notifyObservers()

class MallardDuck(Quackable):

    def __init__(self) -> None:
        self.observable = Observable(self)

    def quack(self):
        print('꽉꽉')
        self.notifyObservers()
    
    def registerObserver(self, observer):
        self.observable.registerObserver(observer)

    def notifyObservers(self):
        self.observable.notifyObservers()

    def __repr__(self) -> str:
        return '물오리'

class RedheadDuck(Quackable):

    def __init__(self) -> None:
        self.observable = Observable(self)

    def quack(self):
        print('꽥꽥')
        self.notifyObservers()
    
    def registerObserver(self, observer):
        self.observable.registerObserver(observer)

    def notifyObservers(self):
        self.observable.notifyObservers()

    def __repr__(self) -> str:
        return '붉은머리오리'

class DuckCall(Quackable):
    
    def __init__(self) -> None:
        self.observable = Observable(self)

    def quack(self):
        print('꽉꽉')
        self.notifyObservers()
    
    def registerObserver(self, observer):
        self.observable.registerObserver(observer)

    def notifyObservers(self):
        self.observable.notifyObservers()

    def __repr__(self) -> str:
        return '오리 호출기'

class RubberDuck(Quackable):

    def __init__(self) -> None:
        self.observable = Observable(self)

    def quack(self):
        print('삑삑')
        self.notifyObservers()
    
    def registerObserver(self, observer):
        self.observable.registerObserver(observer)

    def notifyObservers(self):
        self.observable.notifyObservers()

    def __repr__(self) -> str:
        return '고무 오리'

class Goose:
    def __init__(self) -> None:
        pass

    def honk(self):
        print('끽끽')

    def __repr__(self) -> str:
        return '거위'

# 데코레이터 패턴
class QuackCounter(Quackable):
    numberOfQuacks = 0

    def __init__(self, duck) -> None:
        self.duck = duck

    def quack(self):
        self.duck.quack()
        self.__class__.numberOfQuacks+=1

    @classmethod
    def getQuacks(cls):
        return cls.numberOfQuacks
    
    def registerObserver(self, observer):
        self.duck.registerObserver(observer)

    def notifyObservers(self):
        self.duck.notifyObservers()

# 어댑터 패턴
class GooseAdapter(Quackable):

    def __init__(self, goose) -> None:
        self.goose = goose
        self.observable = Observable(self)

    def quack(self):
        self.goose.honk()
        self.notifyObservers()

    def registerObserver(self, observer):
        self.observable.registerObserver(observer)

    def notifyObservers(self):
        self.observable.notifyObservers()

    def __repr__(self) -> str:
        return '거위'

class DuckSimulator:
    def simulate(self, duckFactory):
        self.mallardDuck = duckFactory.createMallardDuck()
        self.redheadDuck = duckFactory.createRedHeadDuck()
        self.duckCall = duckFactory.createDuckCall()
        self.rubberDuck = duckFactory.createRubberDuck()
        self.gooseDuck = GooseFactory().createGoose()

        print('\n오리 시뮬레이션 (+ 옵저버)')

        flockOfDucks = Flock()

        flockOfDucks.add(self.redheadDuck)
        flockOfDucks.add(self.duckCall)
        flockOfDucks.add(self.rubberDuck)
        flockOfDucks.add(self.gooseDuck)

        flockOfMallards = Flock()

        mallardOne = duckFactory.createMallardDuck()
        mallardTwo = duckFactory.createMallardDuck()
        mallardThree = duckFactory.createMallardDuck()
        mallardFour = duckFactory.createMallardDuck()

        flockOfMallards.add(mallardOne)
        flockOfMallards.add(mallardTwo)
        flockOfMallards.add(mallardThree)
        flockOfMallards.add(mallardFour)

        flockOfDucks.add(flockOfMallards)

        quackologist = Quackologist()
        flockOfDucks.registerObserver(quackologist)

        self.simulateQ(flockOfDucks)

        print(f'오리가 소리 낸 횟수: {QuackCounter.getQuacks()} 번')

    def simulateQ(self,duck):
        duck.quack()

if __name__ == '__main__':
    simulator = DuckSimulator()
    duckFactory = CountingDuckFactory()
    simulator.simulate(duckFactory)