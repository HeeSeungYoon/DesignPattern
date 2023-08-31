# HeadFirst 디자인패턴 (Python)

## Chapter 1

* 원칙 1. 변화하는 부분을 찾아내고, 변화하지 않는 부분과 분리한다.
* 원칙 2. 구현보다는 인터페이스에 맞춰서 프로그래밍한다.
* 원칙 3. 상속보다는 구성(composition)을 활용한다.

[전략 패턴](./Patterns/strategy.py) Duck 클래스, FlyBehavior, QuackBehavior 인터페이스 구현

1. 알고리즘군(ex. FlyBehavior, QuackBehavior)을 정의하고 캡슐화해서 각각의 알고리즘군을 수정해서 쓸 수 있게 해준다. 
2. 클라이언트(Duck 클래스)로부터 알고리즘을 분리해서 독립적으로 변경할 수 있다.

[p.61 전략 패턴 예제](./Patterns/strategy2.py) Character 클래스, WeaponBehavior 인터페이스 구현

## Chapter2 

* 원칙 4. 상호작용하는 객체 사이에는 가능하면 느슨한 결합(Loose Coupling)을 사용해야 한다.

느슨한 결합(Loose Coupling) : Subject는 Observer들이 Observer 인터페이스를 구현한다는 것을 제외하면 Observer에 관해 모른다.

[옵저버 패턴](./Patterns/observer.py) : 한 객체(Subject)의 상태가 바뀌면 그 객체에 의존하는 다른 객체(Observer)에게 연락이 가고 자동으로 내용이갱신되는 방식으로 일대다(one-to-many) 의존성을 정의한다.
* Subject 인터페이스 => WeatherData 클래스 구현
* Observer 인터페이스 => CurrentConditionDisplay, StatisticDisplay, ForcastDisplay, HeatIndexDisplay 클래스 구현

※ 출판-구독(Publish-Subscribe) 패턴 : 여러 개의 Subject와 메시지 유형이 있는 복잡한 상황에서 사용, 미들웨어 시스템에서 종종 쓰임

## Chapter 3

* 원칙 5. OCP(Open-Closed Principle) : 클래스는 확장에는 열려 있어야 하지만 변경에는 닫혀 있어야 한다.

[데코레이터 패턴](./Patterns/decorator.py) : 객체에 추가 요소를 동적으로 더할 수 있다. 서브클래스를 만들 때보다 훨씬 유연하게 기능을 확장할 수 있다.
* Component : Beverage 추상 클래스 => HouseBlend, DarkRoast, Espresso, Decaf 클래스 구현
* Decorator : CondimentDecorator(첨가물) 추상 클래스 => Milk, Mocha, Soy, Whip 클래스 구현

## Chapter 4

* 원칙 6. DIP(Dependency Inversion Principle) : 추상화된 것에 의존하게 만들고 구상 클래스에 의존하지 않게 만든다. 

[팩토리 패턴](./Patterns/factory.py) : 객체를 생성할 때 필요한 인터페이스를 만든다.(=>객체를 생성하는 코드를 캡슐화) 인스턴스 만드는 일은 서브 클래스에게 맡기게 된다.

팩토리 메서드 패턴
* [Creator 클래스](./Patterns/PizzaStore/pizzastore.py) : PizzaStore => NYStylePizzaStore, ChicagoPizzaStore 구상 클래스에서 팩토리 메서드(createPizza)구현, 팩토리 메서드에서 객체(Product) 인스턴스가 결정
* [Product 클래스](./Patterns/PizzaStore/pizza.py) : Pizza => NYStylePizza, ChicagoPizza 구상 클래스 구현

추상 팩토리 패턴 : 구상 클래스에 의존하지 않고도 서로 연관되거나 의존적인 객체로 이루어진 [제품군](./Patterns/PizzaStore/pizzaIngredient.pyPizzaIngredient.py)(피자 원재료)을 생산하는 인터페이스 제공한다. 
* PizzaIngredientFactory(피자 원재료 팩토리) =>
NYPizzaIngredientFactory, ChicagoPizzaIngredientFactory 구상 클래스 구현

## Chapter 5

[싱글턴 패턴](./Patterns/singleton.py) : 클래스 인스턴스를 하나만 만들고, 그 인스턴스로의 전역 접근을 제공한다.

## Chapter 6

[커맨드 패턴](./Patterns/command.py) : 요청 내역을 객체로 캡슐화해서 객체를 서로 다른 요청 내역에 따라 매개변수화할 수 있다. => 요청하는 객체와 요청을 수행하는 객체를 분리
* Commander : Command 인터페이스 => LightOnCommand, LightOffCommand, CeilingFanOnCommand, CeilingFanOffCommand ... 클래스 구현
* Invoker : RemoteControl => setCommand(), execute(), undo() 메소드 실행
* [Receiver](./Patterns/device.py) : Light, CeilingFan, GarageDoor, Stereo ... 클래스 구현

※ 로그 및 트랜잭션 시스템 구현 가능

## Chapter 7

* 원칙 7. 최소 지식 원칙(Principle of Least Knowledge) : 최소 결합을 해야 한다. => 어떤 객체든 그 객체와 상호작용을 하는 클래스의 개수와 상호작용 방식에 주의를 기울여야 한다.

[어댑터 패턴](./Patterns/adapter.py) : 특정 클래스 인터페이스를 클라이언트에서 요구하는 다른 인터페이스로 변환한다. 인터페이스가 호환되지 않아 같이 쓸 수 없었던 클래스를 사용할 수 있게 도와준다.

TurkeyAdapter => Turkey 객체를 Duck 인터페이스에서 사용 가능

[퍼사드 패턴](./Patterns/facade.py) : 서브시스템에 있는 일련의 인터페이스를 통합 인터페이스로 묶어 준다. 고수준 인터페이스를 정의하므로 서브시스템을 더 편리하게 사용할 수 있다.

HomeTheaterFacade 인터페이스 구현

## Chapter 8.

* 원칙 8. 할리우드 원칙 : 저수준 모듈을 언제 어떻게 호출할지는 고수준 모듈에서 결정한다. => 의존성 부패(Dependency rot) 방지 가능

[템플릿 메서드 패턴](./Patterns/template.py) : 알고리즘의 골격을 정의한다. 알고리즘의 일부 단계를 서브클래스에서 구현할 수 있으며, 알고리즘의 구조는 그대로 유지하면서 알고리즘의 특정 단계를 서브클래스에서 재정의할 수 있다.

CaffeineBeverage 템플릿 구현
* prepairRecipe() : 템플릿 메서드 => 추상 메서드 brew(), addCondiments() 단계를 서브클래스에서 구현

## Chapter 9.

* 원칙 9. 단일 역할 원칙 : 하나의 클래스는 하나의 역할만 맡아야 한다.

※ 응집도(Cohesion) : 한 클래스 또는 모듈이 특정 목적이나 역할을 얼마나 일관되게 지원하는지를 나타내는 척도

[반복자 패턴](./Patterns/iterator.py) : 컬렉션의 구현 방법을 노출하지 않으면서 집합체 내의 모든 항목에 접근하는 방법을 제공한다.

pancakeMenu(set), dinerMenu(list), cafeMenu(dict) 클래스의 createIterator() 메소드 호출 => iter() 메소드를 호출하여 자료형 내의 모든 항목에 접근

[컴포지트 패턴](./Patterns/composite.py) : 객체를 트리구조로 구성해서 부분-전체 계층구조를 구현한다. 개별 객체와 복합 객체를 똑같은 방법으로 다룰 수 있다.

MenuComponent 추상 클래스 => Menu(복합 객체), MenuItem(개별 객체) 구상 클래스 구현