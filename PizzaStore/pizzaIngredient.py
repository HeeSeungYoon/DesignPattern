# 원재료 클래스
class Dough:
    def __init__(self):
        pass

class ThinCrushDough(Dough):
    def __init__(self):
        print('얇은 크러스트 도우')

class ThickCrustDough(Dough):
    def __init__(self):
        print('두꺼운 크러스트 도우')

class Sauce:
    def __init__(self):
        pass

class MarinaraSauce(Sauce):
    def __init__(self):
        print('마리나라 소스')

class PlumTomatoSauce(Sauce):
    def __init__(self):
        print('프룸 토마토 소스')

class Cheese:
    def __init__(self):
        pass

class ReggianoCheese(Cheese):
    def __init__(self):
        print('레기아노 치즈')

class MozzarellaCheese(Cheese):
    def __init__(self):
        print('모짜렐라 치즈')

class Veggies:
    def __init__(self):
        pass

class Galic(Veggies):
    def __init__(self):
        print('마늘')

class Onion(Veggies):
    def __init__(self):
        print('양파')

class Mushroom(Veggies):
    def __init__(self):
        print('버섯')

class ReadPepper(Veggies):
    def __init__(self):
        print('레드페퍼')

class BlackOlives(Veggies):
    def __init__(self):
        print('블랙 올리브')

class EggPlant(Veggies):
    def __init__(self):
        print('달걀')

class Spinach(Veggies):
    def __init__(self):
        print('시금치')

class Pepperoni:
    def __init__(self):
        pass

class SlicedPepperoni(Pepperoni):
    def __init__(self):
        print('얇게 썬 페퍼로니')

class Clams:
    def __init__(self):
        pass

class FreshClams(Clams):
    def __init__(self):
        print('신선한 조개')

class FrozenClams(Clams):
    def __init__(self):
        print('얼린 조개')