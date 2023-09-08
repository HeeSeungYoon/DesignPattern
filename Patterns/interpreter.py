class Expression:
    def interpret(self, context):
        pass

class Sequence(Expression):
    def __init__(self) -> None:
        self.expression1=None
        self.expression2=None

    def interpret(self, context):
        return super().interpret(context)
    
class Repetition(Expression):
    def __init__(self) -> None:
        self.variable=None
        self.expression=None

    def interpret(self, context):
        return super().interpret(context)
    
class Variable(Expression):
    def interpret(self, context):
        return super().interpret(context)
    
class QuackCommand(Expression):
    def interpret(self, context):
        return super().interpret(context)
    
class RightCommand(Expression):
    def interpret(self, context):
        return super().interpret(context)
    
class FlyCommand(Expression):
    def interpret(self, context):
        return super().interpret(context)
    
