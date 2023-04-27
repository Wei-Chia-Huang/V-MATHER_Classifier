from operate_object import * 
import random

# 生成兩正整數運算的題目
def generate_int_equation():
    # 隨機生成兩個 0 到 9999 的正整數 (範圍可自行調整)
    value1 = random.randint(0, 9999)  
    value2 = random.randint(0, 9999)

    # 隨機選擇加減乘除運算符號  
    operator = random.choice(["+", "-", "*", "/"]) 

    return f"{value1} {operator} {value2}"

# 生成兩正小數或整數運算的題目
def generate_decimal_equation():
    # 隨機產生兩個數值，可能是整數或小數，小數最多到小數點下第四位
    value1 = round(random.uniform(0, 100), random.randint(0, 4))
    value2 = round(random.uniform(0, 100), random.randint(0, 4))

    # 隨機產生一個運算符
    operator = random.choice(["+", "-", "*", "/"])

    # 如果數值是整數，去除小數點後的部分
    if value1.is_integer():
        value1 = int(value1)
    if value2.is_integer():
        value2 = int(value2)
    
    return f"{value1} {operator} {value2}"

# 生成兩正分數或整數運算的題目
def generate_fraction_equation():
    # 隨機產生兩個數值，可能是整數或分數
    value1 = f"Divide[{random.randint(1, 100)}, {random.randint(1, 100)}]" 
    value2 = f"Divide[{random.randint(1, 100)}, {random.randint(1, 100)}]"

    # 隨機選擇加減乘除運算符號  
    operator = random.choice(["+", "-", "*", "/"])

    # 提取兩分數的分子跟分母
    value1_numerator, value1_denominator = numerator_and_denominator(value1)
    value2_numerator, value2_denominator = numerator_and_denominator(value2)

    # 若分數可整除，視為整數
    if value1_numerator % value1_denominator == 0:
        value1 = value1_numerator // value1_denominator 
    if value2_numerator % value2_denominator == 0:
        value2 = value2_numerator // value2_denominator

    return f"{value1} {operator} {value2}"

# 提取分子跟分母
def numerator_and_denominator(fraction):
    # 使用 split 函式切割字串，取得 [] 中的字串
    parts = fraction.split("[")[1].split("]")[0].split(",")

    # 取得分子與分母，並轉換成整數
    numerator = int(parts[0].strip())
    denominator = int(parts[1].strip())

    # 回傳結果
    return numerator, denominator

print("兩正整數運算分類測試:")
i = 0
while i < 20:
    # 生成兩正整數運算的題目
    question = generate_int_equation()
    
    # 建立 Node 物件
    output = Node(question)  

    # 輸出題目與分類結果
    print(f"{output.LeftValue} {output.operator} {output.RightValue}, {output.classify()}")
    i += 1  

print("\n兩正小數或整數運算分類測試:")
i = 0
while i < 20:
    # 生成兩正小數或整數運算的題目
    question = generate_decimal_equation()
    
    # 建立 Node 物件
    output = Node(question)  

    # 輸出題目與分類結果
    print(f"{output.LeftValue} {output.operator} {output.RightValue}, {output.classify()}")
    i += 1  

print("\n兩正分數或整數運算分類測試:")
i = 0
while i < 20:
    # 生成兩分數或整數運算的題目
    question = generate_fraction_equation()
    
    # 建立 Node 物件
    output = Node(question)  

    # 輸出題目與分類結果
    print(f"{output.LeftValue} {output.operator} {output.RightValue}, {output.classify()}")
    i += 1

# 手動輸入題目
while True:
    question = input("\n請輸入題目：")
    
    # 建立 Node 物件
    output = Node(question)

    # 輸出題目與分類結果
    print(f"{output.LeftValue} {output.operator} {output.RightValue}, {output.classify()}")