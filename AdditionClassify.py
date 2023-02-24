def addition_classify(value1, value2):
    classify_tag = {
        "10 以內的加法": 0,
        "20 以內的加法": 0,
        "二位數的加法（不進位）": 0,
        "二位數的加法（有進位）": 0,
        "三位數的加法（不進位）": 0,
        "三位數的加法（有進位）": 0,
        "四位數的加法": 0,
        "十萬以內的加法 ": 0,
        "大數加法": 0
    }
    
    classify_rule = {
        "10 以內的加法": __less_than_10,
        "20 以內的加法": __less_than_20,
        "二位數的加法（不進位）": __twoDigit_numbers_without_carry,
        "二位數的加法（有進位）": __twoDigit_numbers_with_carry,
        "三位數的加法（不進位）": __threeDigit_numbers_without_carry,
        "三位數的加法（有進位）": __threeDigit_numbers_with_carry,
        "四位數的加法": __fourDigit_numbers,
        "十萬以內的加法 ": __less_than_one_hundred_thousand,
        "大數加法": __addition_of_large_numbers
    }

    for key in classify_rule:
        if classify_rule[key](value1, value2):
            classify_tag[key] = 1

    return ", ".join(key for key in classify_tag if classify_tag[key] != 0)

def __less_than_10(value1, value2):
    if int(value1) + int(value2) <= 10:
        return True
    return False

def __less_than_20(value1, value2):
    if int(value1) + int(value2) <= 20:
        return True
    return False

def __twoDigit_numbers_without_carry(value1, value2):
    if max(len(value1), len(value2)) == 2:
        value1 = list(value1)[::-1]
        value2 = list(value2)[::-1]
        for i in range(min(len(value1), len(value2))):
            if int(value1[i]) + int(value2[i]) >= 10:
                return False
        return True
    return False

def __twoDigit_numbers_with_carry(value1, value2):
    if max(len(value1), len(value2)) == 2:
        value1 = list(value1)[::-1]
        value2 = list(value2)[::-1]
        for i in range(min(len(value1), len(value2))):
            if int(value1[i]) + int(value2[i]) >= 10:
                return True
        return False
    return False

def __threeDigit_numbers_without_carry(value1, value2):
    if max(len(value1), len(value2)) == 3:
        value1 = list(value1)[::-1]
        value2 = list(value2)[::-1]
        for i in range(min(len(value1), len(value2))):
            if int(value1[i]) + int(value2[i]) >= 10:
                return False
        return True
    return False

def __threeDigit_numbers_with_carry(value1, value2):
    if max(len(value1), len(value2)) == 3:
        value1 = list(value1)[::-1]
        value2 = list(value2)[::-1]
        for i in range(min(len(value1), len(value2))):
            if int(value1[i]) + int(value2[i]) >= 10:
                return True
        return False
    return False

def __fourDigit_numbers(value1, value2):
    if max(len(value1), len(value2)) == 4:
        return True
    return False

def __less_than_one_hundred_thousand(value1, value2):
    if int(value1) + int(value2) <= 100000:
        return True
    return False

def __addition_of_large_numbers(value1, value2):
    if int(value1) + int(value2) > 100000:
        return True
    return False