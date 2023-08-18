from PizzaStore.pizzaIngredient import *
from PizzaStore.pizzastore import *

# 원재료 팩토리 (추상 팩토리)
class PizzaIngredientFactory:
    
    def createDough(self):
        pass

    def createSauce(self):
        pass

    def createCheese(self):
        pass

    def createVeggies(self):
        pass

    def createPepperoni(self):
        pass

    def createClam(self):
        pass

class NYPizzaIngredienetFactory(PizzaIngredientFactory):
    
    def createDough(self):
        return ThinCrushDough()
    
    def createSauce(self):
        return MarinaraSauce()
    
    def createCheese(self):
        return ReggianoCheese()
    
    def createVeggies(self):
        veggies = [Galic(), Onion(), Mushroom(), ReadPepper()]
        return veggies
    
    def createPepperoni(self):
        return SlicedPepperoni()
    
    def createClam(self):
        return FreshClams()
    
class ChicagoPizzaIngredientFactory(PizzaIngredientFactory):
    
    def createDough(self):
        return ThickCrustDough()
    
    def createSauce(self):
        return PlumTomatoSauce()
    
    def createCheese(self):
        return MozzarellaCheese()
    
    def createVeggies(self):
        veggies = [BlackOlives(), EggPlant(), Spinach()]
        return veggies
    
    def createPepperoni(self):
        return SlicedPepperoni()
    
    def createClam(self):
        return FrozenClams()

if __name__ == "__main__":
    nyStore = NYStylePizzaStore()
    chicagoStore = ChicagoStylePizzaStore()

    pizza = nyStore.orderPizza('cheese')
    print(f'너가 주문한 {pizza.getName()}\n')

    pizza =  chicagoStore.orderPizza('cheese')
    print(f'내가 주문한 {pizza.getName()}\n')

    pizza = nyStore.orderPizza('clam')
    print(f'너가 주문한 {pizza.getName()}\n')

    pizza =  chicagoStore.orderPizza('clam')
    print(f'내가 주문한 {pizza.getName()}\n')

    pizza = nyStore.orderPizza('pepperoni')
    print(f'너가 주문한 {pizza.getName()}\n')

    pizza =  chicagoStore.orderPizza('pepperoni')
    print(f'내가 주문한 {pizza.getName()}\n')

    pizza = nyStore.orderPizza('veggie')
    print(f'너가 주문한 {pizza.getName()}\n')

    pizza =  chicagoStore.orderPizza('veggie')
    print(f'내가 주문한 {pizza.getName()}\n')