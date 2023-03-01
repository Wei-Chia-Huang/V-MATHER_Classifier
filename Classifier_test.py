from operate_object import *

while True:
    question = input("請輸入算式：")
    output = Node(question)  # 建立 Node 物件
    print(question + ", " + output.classify() + "\n")  # 輸出題目與分類結果