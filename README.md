# [ 0307 ] V-MATHER 分類器程式碼修改

## 執行方式

### ⚠️ 下方文件都要在同一個資料夾下

### 運行流程

1. 執行 classifier_test.py
2. classifier_test.py 會自動生成兩正整數運算的題目，並分類題目
3. classifier_test.py 會自動生成兩正小數或整數運算的題目，並分類題目
4. 將分類結果顯示於終端機

> 自動生成的題目分類完畢後，會進入手動輸入題目的分類。
若不須手動輸入，可用 `ctrl + c` 終止程式，或是將 classifier_test.py 當中得手動輸入部分註解掉。
> 

### 題目的輸入規範

- 標準輸入
    
    運算子前後加空格。例如：`123 + 456`
    
- 容錯輸入
    1. 輸入可以自動忽略空格。例如：`123+421` 或 `223 + 321`
    2. 接受半全形的混和輸入。例如：`１２３＋４５６` 或 `１2４＊３２1`
    3. 接受輸入等號與問號。例如：`123+345 =` 或 `123+345 ?` 或 `123+345 = ?`
- 未完成的容錯輸入
    1. `23.-21.2` -> 要能接受 " 23. " 這種小數點後面沒有的輸入。
    2. `12.21*21...` -> 要能接受 " 21... " 這種多打了很多小數點的情況。

## 文件說明

### classifier_test.py

此程式碼為數學問題分類器，可取得題目數值，並判斷題目為 （以均一為分類標準）

目前已完成容錯輸入第一點

[初步解題系統實作](https://www.notion.so/06694af4299445b892e3a9e6f2c2599e)

[**設計規格說明**](https://www.notion.so/f201c65fe79f43bb8f9e1eb4d8ca9948)

### operate_object.py

- 此程式為各種運算方式的類別（class）
- ~~目前已撰寫加法、減法、乘法、除法的類別~~
- 目前只有 Node 類別
- 未來可在此程式新增運算方式的類別

### xxx_classify.py 都有利用 `try...except...` 來幫助排除錯誤

### addition_classify.py（初步撰寫完成）

- 此程式用來判斷加法物件包含哪些分類目標，並回傳給 classifier_test.py
- 利用 python 的字典來做迭代判斷
- 未來可在此程式新增加法分類目標與規則

### subtraction_classify.py（初步撰寫完成）

- 此程式用來判斷減法物件包含哪些分類目標，並回傳給 classifier_test.py
- 利用 python 的字典來做迭代判斷
- 未來可在此程式新增減法分類目標與規則

### multiplication_classify.py（初步撰寫完成）

- 此程式用來判斷乘法物件包含哪些分類目標，並回傳給 classifier_test.py
- 利用 python 的字典來做迭代判斷
- 未來可在此程式新增乘法分類目標與規則

### division_classify.py（初步撰寫完成）

- 此程式用來判斷除法物件包含哪些分類目標，並回傳給 classifier_test.py
- 利用 python 的字典來做迭代判斷
- 未來可在此程式新增除法分類目標與規則

### decimal_operation_classify.py（初步撰寫完成）

- 此程式用來判斷小數運算物件包含哪些分類目標，並回傳給 classifier_test.py
- 利用 python 的字典來做迭代判斷
- 未來可在此程式新增小數運算分類目標與規則

### Infix _To_Postfix.py、ExpressTree.py（暫時用不到）

- 嘗試中的東西，先不用理他

### test_data.xlsx

- 測試資料集