from PizzaStore.pizza import *
from factory import NYPizzaIngredienetFactory, ChicagoPizzaIngredientFactory

# 생산자(Creator) 클래스
class PizzaStore:

    pizza = Pizza()

    def orderPizza(self, item):
        
        self.pizza = self.createPizza(item)

        self.pizza.prepare()
        self.pizza.bake()
        self.pizza.cut()
        self.pizza.box()

        return self.pizza

    # 팩토리 메서드(추상 메서드)
    def createPizza(self, item):
        pass

class NYStylePizzaStore(PizzaStore):

    ingredientFactory = NYPizzaIngredienetFactory()

    def createPizza(self, item):
        self.pizza = None
        if item == 'cheese':
            self.pizza = CheesePizza(self.ingredientFactory)
            self.pizza.setName('뉴욕 스타일 치즈 피자')
        elif item == 'clam':
            self.pizza = ClamPizza(self.ingredientFactory)
            self.pizza.setName('뉴욕 스타일 조개 피자')
        elif item == 'pepperoni':
            self.pizza = PepperoniPizza(self.ingredientFactory)
            self.pizza.setName('뉴욕 스타일 페퍼로니 피자')
        elif item == 'veggie':
            self.pizza = VeggiePizza(self.ingredientFactory)
            self.pizza.setName('뉴욕 스타일 야채 피자')

        return self.pizza
    
class ChicagoStylePizzaStore(PizzaStore):

    ingredientFactory = ChicagoPizzaIngredientFactory()

    def createPizza(self, item):
        self.pizza = None
        if item == 'cheese':
            self.pizza = CheesePizza(self.ingredientFactory)
            self.pizza.setName('시카고 스타일 치즈 피자')
        elif item == 'clam':
            self.pizza = ClamPizza(self.ingredientFactory)
            self.pizza.setName('시카고 스타일 조개 피자')
        elif item == 'pepperoni':
            self.pizza = PepperoniPizza(self.ingredientFactory)
            self.pizza.setName('시카고 스타일 페퍼로니 피자')
        elif item == 'veggie':
            self.pizza = VeggiePizza(self.ingredientFactory)
            self.pizza.setName('시카고 스타일 야채 피자')

        return self.pizza
    
# class CaliforniaPizzaStore(PizzaStore):
    
#     def createPizza(self, item):
#         if item == 'cheese':
#             self.pizza = CheesePizza(self.ingredientFactory)
#             self.pizza.setName('캘리포니아 스타일 치즈 피자')
#         elif item == 'clam':
#             self.pizza = ClamPizza(self.ingredientFactory)
#             self.pizza.setName('캘리포니아 스타일 조개 피자')
#         elif item == 'pepperoni':
#             self.pizza = PepperoniPizza(self.ingredientFactory)
#             self.pizza.setName('캘리포니아 스타일 페퍼로니 피자')
#         elif item == 'veggie':
#             self.pizza = VeggiePizza(self.ingredientFactory)
#             self.pizza.setName('캘리포니아 스타일 야채 피자')

#         return self.pizza
