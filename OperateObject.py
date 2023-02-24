from AdditionClassify import addition_classify

class Node():
    def __init__(self):
        self.operator = None
        self.LeftValue = None
        self.RightValue = None
    
    def result(self):
        pass

class Addition(Node):
    def __init__(self, operator, left_value, right_value):
        super().__init__()
        self.operator = operator
        self.LeftValue = left_value
        self.RightValue = right_value
    
    def result(self): 
        return addition_classify(self.LeftValue, self.RightValue)

class Substraction(Node):
    def __init__(self, operator, left_value, right_value):
        super().__init__()
        self.operator = operator
        self.LeftValue = left_value
        self.RightValue = right_value
    
    def result(self):
        print("substraction") 

class Mutiplication(Node):
    def __init__(self, operator, left_value, right_value):
        super().__init__()
        self.operator = operator
        self.LeftValue = left_value
        self.RightValue = right_value
    
    def result(self):
        print("mutiplication") 

class Division(Node):
    def __init__(self, operator, left_value, right_value):
        super().__init__()
        self.operator = operator
        self.LeftValue = left_value
        self.RightValue = right_value
    
    def result(self):
        print("division") 