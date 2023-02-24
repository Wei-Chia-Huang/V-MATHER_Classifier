# [ 0224 ] V-MATHER 分類器程式碼初上傳

## 執行方式

### ⚠️ 下方文件都要在同一個資料夾下

### 運行流程

1. 更改 Classifier_test.py 當中的 input
    
    **⚠️ 輸入時，運算子前後都要加空格**
    
2. 執行 Classifier_test.py
3. 於終端機顯示 `input, 包含的分類目標 1, 包含的分類目標 2, ...`

### 範例

1. input = 53 + 626
2. 執行 Classifier_test.py
3. 於終端機顯示 `53 + 626, 三位數的加法（不進位）, 十萬以內的加法`

## 文件說明

### Classifier_test.py

此程式碼為數學問題分類器，可取得題目數值，並判斷題目為 （以均一為分類標準）

[初步解題系統實作](https://www.notion.so/06694af4299445b892e3a9e6f2c2599e)

### OperateObject.py

- 此程式為各種運算方式的類別（class）
- 目前以撰寫加法、減法、乘法、除法的類別
- 未來可在此程式新增運算方式的類別

### AdditionClassify.py（初步撰寫完成）

- 此程式用來判斷加法物件包含哪些分類目標，並回傳給 Classifier_test.py
- 利用 python 的字典來做迭代判斷
- 未來可在此程式新增加法分類目標與規則

### SubstractionClassify.py（尚未撰寫）

- 此程式用來判斷減法物件包含哪些分類目標，並回傳給 Classifier_test.py
- 利用 python 的字典來做迭代判斷
- 未來可在此程式新增減法分類目標與規則

### MutiplicationClassify.py（尚未撰寫）

- 此程式用來判斷乘法物件包含哪些分類目標，並回傳給 Classifier_test.py
- 利用 python 的字典來做迭代判斷
- 未來可在此程式新增乘法分類目標與規則

### DivisionClassify.py（尚未撰寫）

- 此程式用來判斷除法物件包含哪些分類目標，並回傳給 Classifier_test.py
- 利用 python 的字典來做迭代判斷
- 未來可在此程式新增除法分類目標與規則

### Infix _To_Postfix.py、ExpressTree.py（暫時用不到）

- 嘗試中的東西，先不用理他

### test_data.xlsx

- 測試資料集