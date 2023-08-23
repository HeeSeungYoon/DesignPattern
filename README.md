# HeadFirst 디자인패턴 (Python)

## Chapter 1. 

* 원칙 1. 변화하는 부분을 찾아내고, 변화하지 않는 부분과 분리한다.
* 원칙 2. 구현보다는 인터페이스에 맞춰서 프로그래밍한다.
* 원칙 3. 상속보다는 구성(composition)을 활용한다.

[전략 패턴](./strategy.py) Duck 클래스, FlyBehavior, QuackBehavior 인터페이스 구현

1. 알고리즘군(ex. FlyBehavior, QuackBehavior)을 정의하고 캡슐화해서 각각의 알고리즘군을 수정해서 쓸 수 있게 해준다. 
2. 클라이언트(Duck 클래스)로부터 알고리즘을 분리해서 독립적으로 변경할 수 있다.

[p.61 전략 패턴 예제](./strategy2.py) Character 클래스, WeaponBehavior 인터페이스 구현

## Chapter2 

* 원칙 4. 상호작용하는 객체 사이에는 가능하면 느슨한 결합(Loose Coupling)을 사용해야 한다.

느슨한 결합(Loose Coupling) : Subject는 Observer들이 Observer 인터페이스를 구현한다는 것을 제외하면 Observer에 관해 모른다.

[옵저버 패턴](./observer.py) : 한 객체(Subject)의 상태가 바뀌면 그 객체에 의존하는 다른 객체(Observer)에게 연락이 가고 자동으로 내용이갱신되는 방식으로 일대다(one-to-many) 의존성을 정의한다.
* Subject 인터페이스 => WeatherData 클래스 구현
* Observer 인터페이스 => CurrentConditionDisplay, StatisticDisplay, ForcastDisplay, HeatIndexDisplay 클래스 구현

※ 출판-구독(Publish-Subscribe) 패턴 : 여러 개의 Subject와 메시지 유형이 있는 복잡한 상황에서 사용, 미들웨어 시스템에서 종종 쓰임

## Chapter 3.

* 원칙 5. OCP(Open-Closed Principle) : 클래스는 확장에는 열려 있어야 하지만 변경에는 닫혀 있어야 한다.

[데코레이터 패턴](./decorator.py) : 객체에 추가 요소를 동적으로 더할 수 있다. 서브클래스를 만들 때보다 훨씬 유연하게 기능을 확장할 수 있다.
* Component : Beverage 추상 클래스 => HouseBlend, DarkRoast, Espresso, Decaf 클래스 구현
* Decorator : CondimentDecorator(첨가물) 추상 클래스 => Milk, Mocha, Soy, Whip 클래스 구현

## Chapter 4.

* 원칙 6. DIP(Dependency Inversion Principle) : 추상화된 것에 의존하게 만들고 구상 클래스에 의존하지 않게 만든다. 

[팩토리 패턴](./factory.py) : 객체를 생성할 때 필요한 인터페이스를 만든다.(=>객체를 생성하는 코드를 캡슐화) 인스턴스 만드는 일은 서브 클래스에게 맡기게 된다.

팩토리 메서드 패턴
* [Creator 클래스](./PizzaStore/pizzastore.py) : PizzaStore => NYStylePizzaStore, ChicagoPizzaStore 구상 클래스에서 팩토리 메서드(createPizza)구현, 팩토리 메서드에서 객체(Product) 인스턴스가 결정
* [Product 클래스](./PizzaStore/pizza.py) : Pizza => NYStylePizza, ChicagoPizza 구상 클래스 구현

추상 팩토리 패턴 : 구상 클래스에 의존하지 않고도 서로 연관되거나 의존적인 객체로 이루어진 [제품군](./PizzaStore/pizzaIngredient.pyPizzaIngredient.py)(피자 원재료)을 생산하는 인터페이스 제공한다. 
* PizzaIngredientFactory(피자 원재료 팩토리) =>
NYPizzaIngredientFactory, ChicagoPizzaIngredientFactory 구상 클래스 구현

## Chapter 5.

[싱글턴 패턴](./singleton.py) : 클래스 인스턴스를 하나만 만들고, 그 인스턴스로의 전역 접근을 제공한다.

## Chapter 6.

[커맨드 패턴](./command.py) : 요청 내역을 객체로 캡슐화해서 객체를 서로 다른 요청 내역에 따라 매개변수화할 수 있다. => 요청하는 객체와 요청을 수행하는 객체를 분리
* Commander : Command 인터페이스 => LightOnCommand, LightOffCommand, CeilingFanOnCommand, CeilingFanOffCommand ... 클래스 구현
* Invoker : RemoteControl => setCommand(), execute(), undo() 메소드 실행
* [Receiver](./device.py) : Light, CeilingFan, GarageDoor, Stereo ... 클래스 구현

※ 로그 및 트랜잭션 시스템 구현 가능