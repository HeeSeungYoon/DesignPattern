class Iterator:
    def hasNext(self):
        pass

    def next(self):
        pass

class DinerMenuIterator(Iterator):
    items = []
    position = 0

    def __init__(self, items):
        self.items = items

    def hasNext(self):
        if self.position >= len(self.items) or self.items[self.position] is None :
            return False
        else :
            return True

    def next(self):
        menuItem = self.items[self.position]
        self.position += 1
        return menuItem

class PancakeHouseIterator(Iterator):
    items = set()
    position = 0

    def __init__(self, items):
        self.items = items

    def hasNext(self):
        items = list(self.items)
        if self.position >= len(items) or items[self.position] is None :
            return False
        else :
            return True

    def next(self):
        items = list(self.items)
        menuItem = items[self.position]
        self.position+=1
        return menuItem

class MenuItem:
    name = ''
    description = ''
    vegetarian = False
    price = 0

    def __init__(self, name, description, vegetarian, price):
        self.name = name
        self.description = description
        self.vegetarian = vegetarian
        self.price = price

    def getName(self):
        return self.name
    
    def getDescription(self):
        return self.description
    
    def getPrice(self):
        return self.price
    
    def isVegetarian(self):
        return self.vegetarian

class Menu:
    def createIterator(self):
        pass

class DinerMenu(Menu):
    MAX_ITEMS = 6
    menuItems = []

    def __init__(self):
        self.addItem('채식주의자용 BLT','통밀 위에 콩고기 베이컨, 상추, 토마토를 얹은 메뉴',True, 2.99)
        self.addItem('BLT', '통밀 위에 베이컨, 상추, 토마토를 얹은 메뉴',False, 2.99)
        self.addItem('오늘의 스프','감자 샐러드를 곁들인 오늘의 스프',False,3.29)
        self.addItem('핫도그','사워크라우트, 갖은 양념, 양파, 치즈가 곁들여진 핫도그',False, 3.05)
        self.addItem('찐 채소와 브라운 라이스','찐 채소와 브라운 라이스의 절묘한 조화',True,3.99)
        self.addItem('파스타','마리나라 소스 스파게티. 효모빵도 드립니다.',False,3.89)

    def addItem(self, name, description, vegetarian, price):
        menuItem = MenuItem(name, description, vegetarian, price)
        if len(self.menuItems) >= self.MAX_ITEMS:
            print('죄송합니다. 메뉴가 꽉 찼습니다. 더 이상 추가할 수 없습니다.')
        else:
            self.menuItems.append(menuItem)

    def createIterator(self):
        return iter(self.menuItems)
    
class PanckaeHouseMenu(Menu):
    menuItems = set()

    def __init__(self):
        self.addItem('K&B 팬케이크 세트','스크램블 에그와 토스트가 곁들여진 팬케이크',True, 2.99)
        self.addItem('레귤러 팬케이크 세트','달걀 프라이와 소시지가 곁들여진 팬케이크',False,2.99)
        self.addItem('블루베리 팬케이크','신선한 블루베리와 블루베리 시럽으로 만든 팬케이크',True,3.49)
        self.addItem('와플','취향에 따라 블루베리나 딸기를 얹을 수 있는 와플',True,3.59)

    def addItem(self, name, description, vegetarian, price):
        menuItem = MenuItem(name, description, vegetarian, price)
        self.menuItems.add(menuItem)

    def createIterator(self):
        return iter(self.menuItems)

class CafeMenu(Menu):
    menuItems = {}

    def __init__(self):
        self.addItem('베지 버거와 에어 프라이','통밀빵, 상추, 토마토, 감자 튀김이 첨가된 베지 버거',True,3.99)
        self.addItem('오늘의 스프','샐러드가 곁들여진 오늘의 스프',False,3.69)
        self.addItem('부리토','통 핀토콩과 살사, 구아카몰이 곁들여진 푸짐한 부리토', True,4.29)

    def addItem(self, name, description, vegetarian, price):
        menuItem = MenuItem(name, description, vegetarian, price)
        self.menuItems[name] = menuItem

    def createIterator(self):
        return iter(self.menuItems.values())

class Waitress:
    menus = []

    def __init__(self, menus):
        self.menus = menus
    
    def printMenu(self):
        menuIterator = iter(self.menus)
        for menu in menuIterator:
            self.printMenuIterator(menu.createIterator())

        # print('메뉴\n-----\n아침 메뉴')
        # print('\n점심 메뉴')
        # print('\n저녁 메뉴')
        

    def printMenuIterator(self, iterator):
        for menuItem in iterator:
            print(f'{menuItem.getName()}, {menuItem.getPrice()} -- {menuItem.getDescription()}')

if __name__ == '__main__':
    menus = [PanckaeHouseMenu(), DinerMenu(), CafeMenu()]
    waitress = Waitress(menus)
    waitress.printMenu()