# 此程式會將小數運算的分類結果回傳
def decimal_operation_classify(operator, value1, value2):
    classify_result = {"tag": [], "strategy": None}

    # 建立分類規則的字典，用來迭代尋找符合的分類標籤
    # 分類標籤須按學習階段由低到高排列（低年級 -> 高年級）
    classify_rule = {
        "一位小數的加法": __addition_of_one_decimal_places,
        "一位小數的減法": __subtraction_of_one_decimal_places,
        "二位小數的加法": __addition_of_two_decimal_places,
        "二位小數的減法": __subtraction_of_two_decimal_places,
        "一位小數乘以一位整數": __one_decimal_times_one_digit,
        "二位小數乘以一位整數": __two_decimal_times_one_digit,
        "二位小數乘以二位整數": __two_decimal_times_two_digit,
        "多位小數的加法": __addition_of_multiple_decimal_places,
        "多位小數的減法": __subtraction_of_multiple_decimal_places,
        "小數乘以整數": __decimal_times_integer,
        "小數乘以小數": __decimal_times_decimal,
        "小數除以整數": __decimal_divided_integer,
        "整數除以小數": __integer_divided_decimal,
        "小數除以小數": __decimal_divided_decimal,
        "運算結果小於零": __answer_less_then_0
    }

    # 建立分類標籤所對應的詳解工具之字典
    # 若有新增的分類標籤或詳解工具，請記得修改此字典
    strategy_table = {
        "暫無詳解工具": [
            "一位小數的加法", "一位小數的減法", "二位小數的加法", "二位小數的減法", 
            "一位小數乘以一位整數", "二位小數乘以一位整數", "二位小數乘以二位整數",
            "多位小數的加法", "多位小數的減法", "小數乘以整數", "小數乘以小數", 
            "小數除以整數", "整數除以小數", "小數除以小數", "運算結果小於零"
        ]
    }
    
    try:
        # 迭代尋找符合的所有分類標籤
        for key in classify_rule:
            if classify_rule[key](operator, value1, value2):
                classify_result["tag"].append(key)

        # 詳解工具由學習階段最早的分類標籤決定
        for key in strategy_table:
            if classify_result["tag"][0] in strategy_table[key]:
                classify_result["strategy"] = key

        return classify_result
    except Exception as err:
        print(err)
        classify_result["tag"].append("decimal_operation_classify.py 有 Bug, 須排除")
        classify_result["strategy"] = "因程式有錯誤，故無對應詳解工具"
        return classify_result

# 分類規則：一位小數的加法
def __addition_of_one_decimal_places(operator, value1, value2):
    # 判斷運算符是不是加法
    if operator == "+":
        # 處理value1, value2的小數點
        value1_decimal = 0 if "." not in value1 else len(value1.split(".")[1])
        value2_decimal = 0 if "." not in value2 else len(value2.split(".")[1])
        
        # 判斷value1, value2是不是一位小數
        if max(value1_decimal, value2_decimal) == 1:
            return True
    return False

# 分類規則：一位小數的減法
def __subtraction_of_one_decimal_places(operator, value1, value2):
    # 判斷運算符是不是減法，且 value1 大於 value2
    if operator == "-" and float(value1) > float(value2):
        # 處理value1, value2的小數點
        value1_decimal = 0 if "." not in value1 else len(value1.split(".")[1])
        value2_decimal = 0 if "." not in value2 else len(value2.split(".")[1])
        
        # 判斷value1, value2是不是一位小數
        if max(value1_decimal, value2_decimal) == 1:
            return True
    return False

# 分類規則：二位小數的加法
def __addition_of_two_decimal_places(operator, value1, value2):
    if operator == "+":
        # 處理value1, value2的小數點
        value1_decimal = 0 if "." not in value1 else len(value1.split(".")[1])
        value2_decimal = 0 if "." not in value2 else len(value2.split(".")[1])
        
        # 判斷value1, value2是不是二位小數
        if max(value1_decimal, value2_decimal) == 2:
            return True
    return False

# 分類規則：二位小數的減法
def __subtraction_of_two_decimal_places(operator, value1, value2):
    if operator == "-" and float(value1) > float(value2):
        # 處理value1, value2的小數點
        value1_decimal = 0 if "." not in value1 else len(value1.split(".")[1])
        value2_decimal = 0 if "." not in value2 else len(value2.split(".")[1])
        
        # 判斷value1, value2是不是二位小數
        if max(value1_decimal, value2_decimal) == 2:
            return True
    return False

# 分類規則：一位小數乘以一位整數
def __one_decimal_times_one_digit(operator, value1, value2):
    if operator == "*":
        # 處理value1, value2的小數點
        value1_decimal = 0 if "." not in value1 else len(value1.split(".")[1])
        value2_decimal = 0 if "." not in value2 else len(value2.split(".")[1])
        
        # 判斷value1, value2是否有一位小數
        if max(value1_decimal, value2_decimal) == 1:
            # 判斷value1, value2是否有一位整數
            if len(value1) == 1 or len(value2) == 1:
                return True
    return False

# 分類規則：二位小數乘以一位整數
def __two_decimal_times_one_digit(operator, value1, value2):
    if operator == "*":
        # 處理value1, value2的小數點
        value1_decimal = 0 if "." not in value1 else len(value1.split(".")[1])
        value2_decimal = 0 if "." not in value2 else len(value2.split(".")[1])
        
        # 判斷value1, value2是否有二位小數
        if max(value1_decimal, value2_decimal) == 2:
            # 判斷value1, value2是否有一位整數
            if len(value1) == 1 or len(value2) == 1:
                return True
    return False

# 分類規則：二位小數乘以二位整數
def __two_decimal_times_two_digit(operator, value1, value2):
    if operator == "*":
        # 處理value1, value2的小數點
        value1_decimal = 0 if "." not in value1 else len(value1.split(".")[1])
        value2_decimal = 0 if "." not in value2 else len(value2.split(".")[1])
        
        # 判斷value1, value2是否有二位小數
        if max(value1_decimal, value2_decimal) == 2:
            # 判斷value1, value2是否有二位整數
            if len(value1) == 2 or len(value2) == 2:
                return True
    return False

# 分類規則：多位小數的加法
def __addition_of_multiple_decimal_places(operator, value1, value2):
    if operator == "+":
        # 處理value1, value2的小數點
        value1_decimal = 0 if "." not in value1 else len(value1.split(".")[1])
        value2_decimal = 0 if "." not in value2 else len(value2.split(".")[1])
        
        # 判斷value1, value2是否為多位小數
        if max(value1_decimal, value2_decimal) > 2:
            return True
    return False

# 分類規則：多位小數的減法
def __subtraction_of_multiple_decimal_places(operator, value1, value2):
    if operator == "-" and float(value1) > float(value2):
        # 處理value1, value2的小數點
        value1_decimal = 0 if "." not in value1 else len(value1.split(".")[1])
        value2_decimal = 0 if "." not in value2 else len(value2.split(".")[1])
        
        # 判斷value1, value2是否為多位小數
        if max(value1_decimal, value2_decimal) > 2:
            return True
    return False

# 分類規則：小數乘以整數
def __decimal_times_integer(operator, value1, value2):
    if operator == "*":
        # 處理value1, value2的小數點
        value1_decimal = 0 if "." not in value1 else len(value1.split(".")[1])
        value2_decimal = 0 if "." not in value2 else len(value2.split(".")[1])
        
        # 判斷value1, value2是有多位小數
        if max(value1_decimal, value2_decimal) > 0:
            # 判斷value1, value2是否有整數
            if value1_decimal == 0 or value2_decimal == 0:
                return True
    return False

# 分類規則：小數乘以小數
def __decimal_times_decimal(operator, value1, value2):
    if operator == "*":
        if "." in value1 and "." in value2:
            return True
    return False

# 分類規則：小數除以整數
def __decimal_divided_integer(operator, value1, value2):
    if operator == "/":
        if "." in value1 and "." not in value2:
            return True
    return False

# 分類規則：整數除以小數
def __integer_divided_decimal(operator, value1, value2):
    if operator == "/":
        if "." not in value1 and "." in value2:
            return True
    return False

# 分類規則：小數除以小數
def __decimal_divided_decimal(operator, value1, value2):
    if operator == "/":
        if "." in value1 and "." in value2:
            return True
    return False

# 分類規則：運算結果小於零
def __answer_less_then_0(operator, value1, value2):
    if operator == "-" and float(value1) < float(value2):
        return True
    return False
