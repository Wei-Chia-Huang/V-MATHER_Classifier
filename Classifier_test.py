from OperateObject import *

input = "53 + 626".split()

operator_list = [" + ", " - ", " * ", " / "]

if input[1] == "+":
    output = Addition(input[1], input[0], input[2])
elif input[1] == "-":
    output = Substraction(input[1], input[0], input[2])
elif input[1] == "*":
    output = Mutiplication(input[1], input[0], input[2])
elif input[1] == "/":
    output = Division(input[1], input[0], input[2])

print(" ".join(input) + ", " + output.result())