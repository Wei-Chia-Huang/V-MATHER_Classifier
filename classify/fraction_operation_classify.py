# 此程式會將分數運算的分類結果回傳
def fraction_operation_classify(operator, value1, value2):
    classify_result = {"tag": [], "strategy": None}

    # 建立分類規則的字典，用來迭代尋找符合的分類標籤
    # 分類標籤須按學習階段由低到高排列（低年級 -> 高年級）
    classify_rule = {
        "單位分數": __unit_fraction,
        "同分母分數的加法": __addition_of_same_denominator,
        "同分母分數的減法": __subtraction_of_same_denominator,
        "分數與整數的加法": __addition_of_fraction_and_integer,
        "分數與整數的減法": __subtraction_of_fraction_and_integer,
        "異分母分數的加法": __addition_of_different_denominator,
        "異分母分數的減法": __subtraction_of_different_denominator,
        "分數乘以整數": __fraction_times_integer,
        "分數乘以分數": __fraction_times_fraction,
        "分數除以整數": __fraction_divided_integer,
        "整數除以分數": __integer_divided_fraction,
        "同分母分數的除法": __divison_of_same_denominator,
        "異分母分數的除法": __divison_of_different_denominator,
    }

    # 建立分類標籤所對應的詳解工具之字典
    # 若有新增的分類標籤或詳解工具，請記得修改此字典
    strategy_table = {
        "暫無詳解工具": [
            "單位分數", "同分母分數的加法", "同分母分數的減法", "分數與整數的加法", 
            "分數與整數的減法", "異分母分數的加法", "異分母分數的減法", "分數乘以整數", 
            "分數乘以分數", "分數除以整數", "整數除以分數", "同分母分數的除法", "異分母分數的除法"
        ]
    }

    # 提取兩分數分子跟分母，資料型態為 [分子, 分母]，整數計為 [0, 0]
    value1_parts = [0, 0] if "Divide" not in value1 else __numerator_and_denominator(value1)
    value2_parts = [0, 0] if "Divide" not in value2 else __numerator_and_denominator(value2)

    try:
        # 迭代尋找符合的所有分類標籤
        for key in classify_rule:
            if classify_rule[key](operator, value1_parts, value2_parts):
                classify_result["tag"].append(key)

        # 詳解工具由學習階段最早的分類標籤決定
        for key in strategy_table:
            if classify_result["tag"][0] in strategy_table[key]:
                classify_result["strategy"] = key

        return classify_result
    except Exception as err:
        print(err)
        classify_result["tag"].append("fraction_operation_classify.py 有 Bug, 須排除")
        classify_result["strategy"] = "因程式有錯誤，故無對應詳解工具"
        return classify_result
    
# 提取分子跟分母
def __numerator_and_denominator(fraction):
    # 使用 split 函式切割字串，取得 [] 中的字串
    parts = fraction.split("[")[1].split("]")[0].split(",")

    # 取得分子與分母，並轉換成整數
    numerator = int(parts[0].strip())
    denominator = int(parts[1].strip())

    # 回傳結果
    return [numerator, denominator]

# 分類規則：單位分數，目前都先回傳 False
def __unit_fraction(operator, value1, value2):
    return False

# 分類規則：同分母分數的加法
def __addition_of_same_denominator(operator, value1_parts, value2_parts):
    # 判斷運算符是不是加法
    if operator == "+":
       # 判斷是否為兩個同分母分數
        if value1_parts != [0, 0] and value2_parts != [0, 0]:
            if value1_parts[1] == value2_parts[1]:
                return True
    return False

# 分類規則：同分母分數的減法
def __subtraction_of_same_denominator(operator, value1_parts, value2_parts):
    # 判斷運算符是不是減法
    if operator == "-":
        # 判斷是否為兩個同分母分數
        if value1_parts != [0, 0] and value2_parts != [0, 0]:
            if value1_parts[1] == value2_parts[1]:
                return True
    return False

# 分類規則：分數與整數的加法
def __addition_of_fraction_and_integer(operator, value1_parts, value2_parts):
    # 判斷運算符是不是加法
    if operator == "+":
        # 判斷是否為一個分數跟一個整數
        if value1_parts == [0, 0] or value2_parts == [0, 0]:
            return True
    return False

# 分類規則：分數與整數的減法
def __subtraction_of_fraction_and_integer(operator, value1_parts, value2_parts):
    # 判斷運算符是不是減法
    if operator == "-":
        # 判斷是否為一個分數跟一個整數
        if value1_parts == [0, 0] or value2_parts == [0, 0]:
            return True
    return False

# 分類規則：異分母分數的加法
def __addition_of_different_denominator(operator, value1_parts, value2_parts):
    # 判斷運算符是不是加法
    if operator == "+":
        # 判斷是否為兩個異分母分數
        if value1_parts != [0, 0] and value2_parts != [0, 0]:
            if value1_parts[1] != value2_parts[1]:
                return True
    return False

# 分類規則：異分母分數的減法
def __subtraction_of_different_denominator(operator, value1_parts, value2_parts):
    # 判斷運算符是不是減法
    if operator == "-":
        # 判斷是否為兩個異分母分數
        if value1_parts != [0, 0] and value2_parts != [0, 0]:
            if value1_parts[1] != value2_parts[1]:
                return True
    return False

# 分類規則：分數乘以整數
def __fraction_times_integer(operator, value1_parts, value2_parts):
    # 判斷運算符是不是乘法
    if operator == "*":
        # 判斷是否為一個分數跟一個整數
        if value1_parts == [0, 0] or value2_parts == [0, 0]:
            return True
    return False

# 分類規則：分數乘以分數
def __fraction_times_fraction(operator, value1_parts, value2_parts):
    # 判斷運算符是不是乘法
    if operator == "*":
        # 判斷是否為兩個分數
        if value1_parts != [0, 0] and value2_parts != [0, 0]:
            return True
    return False

# 分類規則：分數除以整數
def __fraction_divided_integer(operator, value1_parts, value2_parts):
    # 判斷運算符是不是除法
    if operator == "/":
        # 判斷是否為分數除以整數
        if value1_parts != [0, 0] and value2_parts == [0, 0]:
            return True
    return False

# 分類規則：分數除以整數
def __integer_divided_fraction(operator, value1_parts, value2_parts):
    # 判斷運算符是不是除法
    if operator == "/":
        # 判斷是否為整數除以分數
        if value1_parts == [0, 0] and value2_parts != [0, 0]:
            return True
    return False

# 分類規則：同分母分數的除法
def __divison_of_same_denominator(operator, value1_parts, value2_parts):
    # 判斷運算符是不是加法
    if operator == "/":
       # 判斷是否為兩個同分母分數
        if value1_parts != [0, 0] and value2_parts != [0, 0]:
            if value1_parts[1] == value2_parts[1]:
                return True
    return False

# 分類規則：異分母分數的除法
def __divison_of_different_denominator(operator, value1_parts, value2_parts):
    # 判斷運算符是不是除法
    if operator == "/":
        # 判斷是否為兩個異分母分數
        if value1_parts != [0, 0] and value2_parts != [0, 0]:
            if value1_parts[1] != value2_parts[1]:
                return True
    return False