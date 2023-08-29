class CaffeineBeverage:
    def __init__(self):
        pass

    def prepareRecipe(self):
        self.boilWater()
        self.brew()
        self.pourInCup()
        if self.customerWantsCondiments():
            self.addCondiments()

    def boilWater(self):
        print('물 끓이는 중')

    def pourInCup(self):
        print('컵에 따르는 중')

    def brew(self):
        pass

    def addCondiments(self):
        pass

    # hook
    def customerWantsCondiments(self):
        return True

class CoffeeWithHook(CaffeineBeverage):

    def brew(self):
        print('필터로 커피를 우려내는 중')

    def addCondiments(self):
        print('설탕과 우유를 추가하는 중')

    def customerWantsCondiments(self):
        answer = self.getUserInput()
        if answer == 'y':
            return True
        else:
            return False
        
    def getUserInput(self):
        answer = input('커피에 우유와 설탕을 넣을까요(y/n)?')
        return answer

class TeaWithHook(CaffeineBeverage):

    def brew(self):
        print('찻잎을 우려내는 중')

    def addCondiments(self):
        print('레몬을 추가하는 중')

    def customerWantsCondiments(self):
        answer = self.getUserInput()
        if answer == 'y':
            return True
        else:
            return False
        
    def getUserInput(self):
        answer = input('차에 레몬을 넣을까요(y/n)?')
        return answer


if __name__ == '__main__':
    teaHook = TeaWithHook()
    coffeeHook = CoffeeWithHook()

    print('\n홍차 준비 중...')
    teaHook.prepareRecipe()

    print('\n커피 준비 중...')
    coffeeHook.prepareRecipe()