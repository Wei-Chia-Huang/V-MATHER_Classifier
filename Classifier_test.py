from operate_object import *
import unicodedata  

while True:
    question = input("請輸入算式：")
    question = unicodedata.normalize("NFKC", question)  # 將題目字元轉為半形大小
    output = Node(question)  # 建立 Node 物件
    print(f"{output.LeftValue} {output.operator} {output.RightValue}, {output.classify()}\n")  # 輸出題目與分類結果