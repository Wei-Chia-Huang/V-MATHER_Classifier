from addition_classify import addition_classify
from subtraction_classify import subtraction_classify
from multiplication_classify import multiplication_classify
from division_classify import division_classify
from decimal_operation_classify import decimal_operation_classify

class Node():
    def __init__(self, question):
        self.operator = None
        self.LeftValue = None
        self.RightValue = None
        self.__preprocessing(question)  # 將輸入預處理
    
    # 根據物件的 self.operator 來決定分類方式，並回傳分類結果
    def classify(self):
        if "." in self.LeftValue or "." in self.RightValue:
            return decimal_operation_classify(self.operator, self.LeftValue, self.RightValue)
        elif self.operator == "+":
            return addition_classify(self.LeftValue, self.RightValue)
        elif self.operator == "-":
            return subtraction_classify(self.LeftValue, self.RightValue)
        elif self.operator == "*":
            return multiplication_classify(self.LeftValue, self.RightValue)
        elif self.operator == "/":
            return division_classify(self.LeftValue, self.RightValue)

    # 將輸入預處理，建立此物件的屬性
    def __preprocessing(self, question):
        operator_list = ["+", "-", "*", "/"]

        for w in question:
            if w == "=" or w == "?":
                question = question.replace(w, "")
        
        for char in operator_list:
            if char in question:
                self.operator = char
        
        self.LeftValue = question.split(self.operator)[0].strip()
        self.RightValue = question.split(self.operator)[1].strip()


# class Addition(Node):
#     def __init__(self, operator, left_value, right_value):
#         super().__init__()
#         self.operator = operator
#         self.LeftValue = left_value
#         self.RightValue = right_value
    
#     def result(self): 
#         return addition_classify(self.LeftValue, self.RightValue)

# class Subtraction(Node):
#     def __init__(self, operator, left_value, right_value):
#         super().__init__()
#         self.operator = operator
#         self.LeftValue = left_value
#         self.RightValue = right_value
    
#     def result(self):
#         print("substraction") 

# class Mutiplication(Node):
#     def __init__(self, operator, left_value, right_value):
#         super().__init__()
#         self.operator = operator
#         self.LeftValue = left_value
#         self.RightValue = right_value
    
#     def result(self):
#         print("mutiplication") 

# class Division(Node):
    # def __init__(self, operator, left_value, right_value):
    #     super().__init__()
    #     self.operator = operator
    #     self.LeftValue = left_value
    #     self.RightValue = right_value
    
    # def result(self):
    #     print("division") 