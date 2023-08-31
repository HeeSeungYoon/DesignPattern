class MenuComponent:
    def __init__(self):
        pass

    def getName(self):
        pass

    def getDescription(self):
        pass

    def getPrice(self):
        pass

    def isVegetarian(self):
        pass

    def printM(self):
        pass

    def add(self, menuComponent):
        pass

    def remove(self, menuComponent):
        pass
    
    def getChild(self, child):
        pass

class Menu(MenuComponent):
    name = ''
    description = ''

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.menuComponents = []

    def getName(self):
        return self.name

    def getDescription(self):
        return self.description

    def printM(self):
        print(f'\n {self.getName()}, {self.getDescription()}')
        print('-----------------------------')

        for menuComponent in self.menuComponents:
            menuComponent.printM()

    
    def add(self, menuComponent):
        self.menuComponents.append(menuComponent)

    def remove(self, menuComponent):
        self.menuComponents.remove(menuComponent)

    def getChild(self, child):
        return self.menuComponents[child]

class MenuItem(MenuComponent):
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
    
    def printM(self):
        print(' %s%s, %.2f\n     -- %s'%(self.getName(), '(v)' if self.isVegetarian() else '', self.getPrice(), self.getDescription()))

class Waitress:
    allMenus = None

    def __init__(self, allMenus):
        self.allMenus = allMenus

    def printMenu(self):
        self.allMenus.printM()

if __name__ == '__main__':
    pancakeHouseMenu = Menu('팬케이크 하우스 메뉴', '아침 메뉴')
    dinerMenu = Menu('객체마을 식당 메뉴', '점심 메뉴')
    cafeMenu = Menu('카페 메뉴','저녁 메뉴')
    dessertMenu = Menu('디저트 메뉴', '디저트를 즐겨 보세요!')

    allMenus = Menu('전체 메뉴', '전체 메뉴')

    allMenus.add(pancakeHouseMenu)
    allMenus.add(dinerMenu)
    allMenus.add(cafeMenu)

    pancakeHouseMenu.add(MenuItem('K&B 팬케이크 세트','스크램블 에그와 토스트가 곁들여진 팬케이크',True, 2.99))
    pancakeHouseMenu.add(MenuItem('레귤러 팬케이크 세트','달걀 프라이와 소시지가 곁들여진 팬케이크',False,2.99))
    pancakeHouseMenu.add(MenuItem('블루베리 팬케이크','신선한 블루베리와 블루베리 시럽으로 만든 팬케이크',True,3.49))
    pancakeHouseMenu.add(MenuItem('와플','취향에 따라 블루베리나 딸기를 얹을 수 있는 와플',True,3.59))

    dinerMenu.add(MenuItem('채식주의자용 BLT','통밀 위에 콩고기 베이컨, 상추, 토마토를 얹은 메뉴',True, 2.99))
    dinerMenu.add(MenuItem('BLT', '통밀 위에 베이컨, 상추, 토마토를 얹은 메뉴',False, 2.99))
    dinerMenu.add(MenuItem('오늘의 스프','감자 샐러드를 곁들인 오늘의 스프',False,3.29))
    dinerMenu.add(MenuItem('핫도그','사워크라우트, 갖은 양념, 양파, 치즈가 곁들여진 핫도그',False, 3.05))
    dinerMenu.add(MenuItem('찐 채소와 브라운 라이스','찐 채소와 브라운 라이스의 절묘한 조화',True,3.99))
    dinerMenu.add(MenuItem('파스타','마리나라 소스 스파게티. 효모빵도 드립니다.',True,3.89))

    cafeMenu.add(MenuItem('베지 버거와 에어 프라이','통밀빵, 상추, 토마토, 감자 튀김이 첨가된 베지 버거',True,3.99))
    cafeMenu.add(MenuItem('오늘의 스프','샐러드가 곁들여진 오늘의 스프',False,3.69))
    cafeMenu.add(MenuItem('부리토','통 핀토콩과 살사, 구아카몰이 곁들여진 푸짐한 부리토', True,4.29))

    dinerMenu.add(dessertMenu)

    dessertMenu.add(MenuItem('애플 파이','바삭바삭한 크러스트에 바닐라 아이스크림이 얹혀 있는 애플 파이',True, 1.59))
    dessertMenu.add(MenuItem('치즈 케이크','초콜릿 그레이엄 크러스트 위에 부드러운 뉴욕 치즈케이크',True,1.99))
    dessertMenu.add(MenuItem('소르베','라즈베리와 라임의 절묘한 조화',True,1.89))

    waitress = Waitress(allMenus)

    waitress.printMenu()