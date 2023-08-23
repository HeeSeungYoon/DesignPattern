from PizzaStore.pizzaIngredient import *
from factory import PizzaIngredientFactory

# 제품(Product) 클래스
class Pizza:

    def __init__(self):
        self.name = '피자'

        self.dough = Dough()
        self.sauce = Sauce()
        self.cheese = Cheese()
        self.veggies = []
        self.pepperoni = Pepperoni()
        self.clam = Clams()

    def prepare(self):
        pass
        
    def bake(self):
        print("175도에서 25분간 굽기")

    def cut(self):
        print('피자를 8등분으로 자르기')

    def box(self):
        print('상자에 피자 담기')

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

# CheesePizza, ClamPizza, PepperoniPizza, VeggiePizza : 구상 클래스 
class CheesePizza(Pizza):
    ingredientFactory = PizzaIngredientFactory()

    def __init__(self, ingredientFactory):
        self.ingredientFactory = ingredientFactory
    
    def prepare(self):
        print(f'준비 중: {self.name}')
        self.dough = self.ingredientFactory.createDough()
        self.sauce = self.ingredientFactory.createSauce()
        self.cheese = self.ingredientFactory.createCheese()

class ClamPizza(Pizza):
    ingredientFactory = PizzaIngredientFactory()

    def __init__(self, ingredienetFactory):
        self.ingredientFactory = ingredienetFactory

    def prepare(self):
        print(f'준비 중: {self.name}')
        self.dough = self.ingredientFactory.createDough()
        self.sauce = self.ingredientFactory.createSauce()
        self.cheese = self.ingredientFactory.createCheese()
        self.clam = self.ingredientFactory.createClam()

class PepperoniPizza(Pizza):
    ingredientFactory = PizzaIngredientFactory()
     
    def __init__(self, ingredientFactory):
        self.ingredientFactory = ingredientFactory
    
    def prepare(self):
        print(f'준비 중: {self.name}')
        self.dough = self.ingredientFactory.createDough()
        self.sauce = self.ingredientFactory.createSauce()
        self.cheese = self.ingredientFactory.createCheese()
        self.pepperoni = self.ingredientFactory.createPepperoni()

class VeggiePizza(Pizza):
    ingredientFactory = PizzaIngredientFactory()

    def __init__(self, ingredientFactory):
        self.ingredientFactory = ingredientFactory
    
    def prepare(self):
        print(f'준비 중: {self.name}')
        self.dough = self.ingredientFactory.createDough()
        self.sauce = self.ingredientFactory.createSauce()
        self.cheese = self.ingredientFactory.createCheese()
        self.veggies = self.ingredientFactory.createVeggies()
