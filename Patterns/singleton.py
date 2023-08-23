from threading import Lock

# 파이썬에서는 객체 인스턴스를 하나만 만들지 않고 
# 여러 개의 객체가 하나의 인스턴스를 공유하도록 함

class Singleton:
    __uniqueInstance = None
    __lock = Lock()

    def __init__(self):
        raise RuntimeError('Call getInstance() instead')

    # DCL(Double-Checked Locking)
    @classmethod
    def getInstance(cls):
        if cls.__uniqueInstance is None:
            with cls.__lock:
                if not cls.__uniqueInstance :
                    cls.__uniqueInstance = cls.__new__(cls)
        return cls.__uniqueInstance


class ChocolatBoiler:
    __uniqueInstance = None
    __lock = Lock()
    
    __empty = True
    __boiled = False

    def __init__(self):
        raise RuntimeError('Call getInstance() instead')
    
    @classmethod
    def getInstance(cls):
        if cls.__uniqueInstance is None:
            with cls.__lock:
                if not cls.__uniqueInstance :
                    cls.__uniqueInstance = cls.__new__(cls)
        return cls.__uniqueInstance


    def fill(self):
        if self.isEmpty():
            self.__empty = False
            self.__boiled = False

    def drain(self):
        if (not self.isEmpty()) and self.isBoiled():
            # 끓인 재료를 다음 단계로 넘김
            self.__empty = True

    def boil(self):
        if (not self.isEmpty()) and (not self.isBoiled()):
            self.__boiled = True

    def isEmpty(self):
        return self.__empty
    
    def isBoiled(self):
        return self.__boiled


if __name__ == '__main__':
    chocolateBoiler = ChocolatBoiler.getInstance()
    print(chocolateBoiler.isEmpty())
    