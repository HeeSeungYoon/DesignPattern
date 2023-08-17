# 추상 클래스
class Pizza:

    def __init__(self):
        self.name = '피자'
        self.dough = '도우'
        self.sauce = '소스'
        self.toppings = []

    def prepare(self):
        print(f'준비 중: {self.name}')
        print(f'{self.dough}를 돌리는 중...')
        print(f'{self.sauce}를 뿌리는 중...')
        print('토핑을 올리는 중 : ')
        for topping in self.toppings:
            print(f"\t{topping}")

    def bake(self):
        print("175도에서 25분간 굽기")

    def cut(self):
        print('피자를 8등분으로 자르기')

    def box(self):
        print('상자에 피자 담기')

    def getName(self):
        return self.name

# CheesePizza, ClamPizza, PepperoniPizza, VeggiePizza : 구상 클래스 
class CheesePizza(Pizza):
    pass

class ClamPizza(Pizza):
    pass

class PepperoniPizza(Pizza):
    pass

class VeggiePizza(Pizza):
    pass

class NYStyleCheesePizza(Pizza):
    def __init__(self):
        self.name = '뉴욕 스타일 소스와 치즈 피자'
        self.dough = '씬 크러스트 도우'
        self.sauce = '마리나라 소스'
        self.toppings = []
        self.toppings.append('잘게 썬 레지아노 치즈')

class NYStyleClamPizza(Pizza):
    pass

class NYStylePepperoniPizza(Pizza):
    pass

class NYStyleVeggiePizza(Pizza):
    pass

class ChicagoStyleCheesePizza(Pizza):
    def __init__(self):
        self.name = '시카고 스타일 딥 디쉬 치즈 피자'
        self.dough = '아주 두꺼운 크러스트 도우'
        self.sauce = '플럼토마토 소스'
        self.toppings = []
        self.toppings.append('잘게 조각낸 모짜렐라 치즈')

    def cut(self):
        print('네모난 모양으로 피자 자르기')

class ChicagoStyleClamPizza(Pizza):
    pass

class ChicagoStylePepperoniPizza(Pizza):
    pass

class ChicagoStyleVeggiePizza(Pizza):
    pass

class CaliforniaStyleCheesePizza(Pizza):
    pass

class CaliforniaStyleClamPizza(Pizza):
    pass

class CaliforniaStylePepperoniPizza(Pizza):
    pass

class CaliforniaStyleVeggiePizza(Pizza):
    pass

# 간단한 팩토리 클래스
class SimplePizzaFactory:
    
    @classmethod
    def createPizza(cls, type):
        pizza = None
        
        if type == 'cheese':
            pizza = CheesePizza()
        elif type == 'clam':
            pizza = ClamPizza()
        elif type == 'pepperoni':
            pizza = PepperoniPizza()
        elif type == 'veggie':
            pizza = VeggiePizza()

        return pizza

class PizzaStore:

    pizza = Pizza()

    def orderPizza(self, type):
        
        self.pizza = self.createPizza(type)

        self.pizza.prepare()
        self.pizza.bake()
        self.pizza.cut()
        self.pizza.box()

        return self.pizza

    # 팩토리 메서드(추상 메서드)
    def createPizza(self, type):
        pass

class NYStylePizzaStore(PizzaStore):
    
    def createPizza(self, type):
        if type == 'cheese':
            return NYStyleCheesePizza()
        elif type == 'clam':
            return NYStyleClamPizza()
        elif type == 'pepperoni':
            return NYStylePepperoniPizza()
        elif type == 'veggie':
            return NYStyleVeggiePizza()

        return None
    
class ChicagoStylePizzaStore(PizzaStore):

    def createPizza(self, type):
        if type == 'cheese':
            return ChicagoStyleCheesePizza()
        elif type == 'clam':
            return ChicagoStyleClamPizza()
        elif type == 'pepperoni':
            return ChicagoStylePepperoniPizza()
        elif type == 'veggie':
            return ChicagoStyleVeggiePizza()

        return None
    
class CaliforniaPizzaStore(PizzaStore):
    
    def createPizza(self, type):
        if type == 'cheese':
            return CaliforniaStyleCheesePizza()
        elif type == 'clam':
            return CaliforniaStyleClamPizza()
        elif type == 'pepperoni':
            return CaliforniaStylePepperoniPizza()
        elif type == 'veggie':
            return CaliforniaStyleVeggiePizza()

        return None
    
if __name__ == "__main__":
    nyStore = NYStylePizzaStore()
    chicagoStore = ChicagoStylePizzaStore()

    pizza = nyStore.orderPizza('cheese')
    print(f'내가 주문한 {pizza.getName()}\n')

    pizza =  chicagoStore.orderPizza('cheese')
    print(f'너가 주문한 {pizza.getName()}')