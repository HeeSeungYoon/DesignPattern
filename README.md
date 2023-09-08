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

## Chapter 10.

[상태 패턴](./Patterns/state_proxy.py) : 객체의 내부 상태가 바뀜에 따라서 객체의 행동을 바꿀 수 있다. 객체의 클래스가 바뀌는 것과 같은 결과를 얻을 수 있다.

* State 추상 클래스 => NoQuarterState, HasQuarterState, SoldState, SoldOutState 구상 클래스 구현
* GumballMachine 클래스 => 현재 상태를 나타내는 객체(state)에게 행동(insertQuarter(), ejectQuarter(), turnCrank(), dispense() 메소드) 위임

## Chapter 11.

[프록시 패턴](./Patterns/state_proxy.py) : 특정 객체(원격 객체, 생성하기 힘든 객체, 보안이 중요한 객체)로의 접근을 제어하는 대리인(특정 객체를 대변하는 객체)을 제공한다.

* Client : GumballMonitor 
* 원격 객체 : GumballMachine

※ 프록시 종류 : 원격 프록시, 가상 프록시, 보호 프록시, 캐싱 프록시, 동기화 프록시, 방화벽 프록시, 지연 복사 프록시, 스마트 레퍼런스 프록시, 복잡도 숨김 프록시 등 ...

## Chapter 12.

[복합 패턴](./Patterns/simuduck.py)

* Quackable 추상 클래스 => MallardDuck, DuckCall, RedHeadDuck, RubberDuck 구상 클래스

+어댑터 패턴 
* GooseAdapter : 거위용 어댑터

+데코레이터 패턴
* Decorator : QuackCounter => 오리가 소리 낸 횟수

+팩토리 패턴
* AbstartDuckFactory : 모든 오리를 감싼다.

+컴포지트 패턴
* Flock : 복합 객체 => 오리 무리를 관리

+옵저버 패턴 
* QuackObservable 추상 클래스 => Observable 구상클래스
* Observer : Quackologist

+반복자 패턴 

## Chapter 13.

## Chapter 14.

[브리지 패턴](./Patterns/bridge.py) : 추상화된 부분과 구현 부분을 서로 다른 클래스 계층 구조로 분리해서 그 둘을 모두 변경할 수 있다.

* RemoteControl <-> TV : 브릿지(bridge)

---

[빌더 패턴](./Patterns/builder.py) : 복합 객체 생성 과정을 캡슐화한다. 제품의 내부 구조를 클라이언트로부터 보호할 수 있다. 

builder : AbstractBuilder 추상 클래스 => VacationBuilder 구상 빌더

---

[책임 연쇄 패턴](./Patterns/chain_of_responsibility.py) : 요청을 보낸 쪽과 받는 쪽을 분리할 수 있다. 객체는 사슬의 구조를 몰라도 되고 그 사슬에 들어 있는 다른 객체의 직접적인 레퍼런스를 가질 필요도 없으므로 객체를 단순하게 만들 수 있다.

SpamHandler -> FanHandler -> ComplaintHandler -> NewLocHandler 사슬을 따라 요청이 전달

---

[플라이웨이트 패턴](./Patterns/flyweight.py) : 실행 시에 객체 인스턴스의 개수를 줄여서 메모리를 절약할 수 있다. 여러 가상 객체의 상태를 한 곳에 모아 둘 수 있다.

TreeManager => treeArray 리스트에 Tree 인스턴스들을 저장

---

[인터프리터 패턴](./Patterns/interpreter.py) : 간단한 언어를 구현할 때 유용하게 쓰인다.

expression ::= command | sequence | repetiton

sequence ::= expression ';' expression

command ::= right | quack | fly

repetition ::= while '(' variable ')' expression

variable ::= [A-Z,a-z]+

---

중재자 패턴 : 서로 관련된 객체 사이의 복잡한 통신과 제어를 한 곳으로 집중시킬 때 사용한다. 
* 시스템과 객체를 분리함으로써 재사용성을 획기적으로 향상시킬 수 있다. 
* 제어 로직을 한 군데 모아놨으므로 관리하기가 수월하다.
* 시스템에 들어있는 객체 사이에서 오가는 메시지를 확 줄이고 단순화할 수 있다.

---

[메멘토 패턴](./Patterns/memento.py) : 객체를 이전의 상태로 복구할 때 사용한다.
* 저장된 상태를 핵심 객체와는 다른 별도의 객체에 보관할 수 있어 안전하다.
* 핵심 객체의 데이터를 계속해서 캡슐화된 상태로 유지할 수 있다.

프로토타입 패턴 : 어떤 클래스의 인스턴스를 만들 때 자원과 시간이 많이 들거나 복잡할 때 사용한다. 기존 인스턴스를 복사하기만 해도 새로운 인스턴스를 만들 수 있다.
* 클라이언트는 새로운 인스턴스를 만드는 과정을 몰라도 된다.
* 클라이언트는 구체적인 형식을 몰라도 객체를 생성할 수 있다.

---

비지터 패턴 : 다양한 객체에 새로운 기능을 추가해야한는데 캡슐화가 별로 중요하지 않을 때 사용한다.
* 복합 객체 내에 속해 있는 모든 객체에 접근하는 일을 도와주는 역할을 한다. 
* 구조를 변경하지 않으면서도 복합 객체 구조에 새로운 기능을 추가할 수 있다. 

Client(Traverser) => Visitor 객체 호출 : 모든 클래스의 getState() 메소드 호출