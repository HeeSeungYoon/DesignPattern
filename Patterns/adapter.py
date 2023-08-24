from strategy import Duck, MallardDuck

class Turkey :

    def __init__(self):
        pass

    def gobble(self):
        pass

    def fly(self):
        pass

class WildTurkey(Turkey):

    def gobble(self):
        print('골골')
    
    def fly(self):
        print('짧은 거리를 날고 있어요!')
    
class TurkeyAdapter(Duck):
    turkey = Turkey()

    def __init__(self, turkey):
        self.turkey = turkey

    def quack(self):
        self.turkey.gobble()

    def fly(self):
        for _ in range(5):
            self.turkey.fly()

class DuckAdapter(Turkey):
    duck = Duck()

    def __init__(self, duck):
        self.duck = duck

    def gobble(self):
        self.duck.quack()

    def fly(self):
        self.duck.fly()

# 오리인지 칠면조인지 구분하지 못함
def testDuck(duck):
    duck.quack()
    duck.fly()

if __name__ == "__main__":
    duck = MallardDuck()

    turkey = WildTurkey()
    turkeyAdapter = TurkeyAdapter(turkey)

    print('칠면조가 말하길')
    turkey.gobble()
    turkey.fly()

    print('\n오리가 말하길')
    testDuck(duck)

    print('\n칠면조 어댑터가 말하길')
    testDuck(turkeyAdapter)