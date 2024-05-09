import math
import inspect

DO_UNIT_TEST = True

INPUT_ERROR             = "<Input Error> "
DESCRIPTION_ADD         = "Add"
DESCRIPTION_SUBTRACT    = "Subtract"
DESCRIPTION_MULTIPLY    = "Multiply"
DESCRIPTION_DIVIDE      = "Divide"
DESCRIPTION_EXPONENT    = "Exponent"
DESCRIPTION_SQUARE_ROOT = "Square Root"
DESCRIPTION_LAST_RESULT = "Show the last result value"


def square_root(num):
    if num >= 0:
        return math.sqrt(num)
    elif num < 0:
        return INPUT_ERROR + "enter non-negative real number!!"

def test_square_root():
    # いくつかの非負実数に対して，出力値を指定しながら期待通りの出力かを確認する．
    error_msg = "Unit test failed"
    assert square_root(4) == 2, error_msg
    assert square_root(1) == 1, error_msg
    assert square_root(0) == 0, error_msg

    # 非負実数の入力に対して，「出力の二乗が入力と一致すること」「出力が非負であること」を確認する．
    num_array = (0, 100, 9999, 999999, 1767.76432)
    for num in num_array:
        assert num >= 0, "Input of the unit test is not reasonable."
        error_msg = "Unit test failed (in = " + str(num) + ")"
        # 計算の丸め誤差により正確には値が一致しない可能性があるため，両辺ともroundで四捨五入し整数にしてから比較する．
        assert (round(square_root(num) ** 2) == round(num)) == True, error_msg
        assert square_root(num) >= 0, error_msg

    # 負実数の入力に対し，INPUT_ERRORの文言が出力されていることを確認する．
    num_array = (-100, -9999, -999999)
    for num in num_array:
        assert num < 0, "Input of the unit test is not reasonable."
        error_msg = "Unit test failed (in = " + str(num) + ")"
        assert INPUT_ERROR in square_root(num), error_msg
    
    return

def unit_test_aggregation():
    test_square_root()
    return

if DO_UNIT_TEST:
    unit_test_aggregation()

def get_input_num(num_of_required_input):
    num1 = 0 
    num2 = 0
    if num_of_required_input >= 1:
        num1 = float(input("Enter first number : "))
        if num_of_required_input >= 2:
            num2 = float(input("Enter second number  : "))
    return num1, num2

def main():
    last_result = "None"
    while True:
        print("\n")
        print("########### Operation list ###########")
        operations = []
        operations.append({"ID":"1", "Description":DESCRIPTION_ADD, "NumOfInputs":2})
        operations.append({"ID":"2", "Description":DESCRIPTION_SUBTRACT, "NumOfInputs":2})
        operations.append({"ID":"3", "Description":DESCRIPTION_MULTIPLY, "NumOfInputs":2})
        operations.append({"ID":"4", "Description":DESCRIPTION_DIVIDE, "NumOfInputs":2})
        operations.append({"ID":"5", "Description":DESCRIPTION_EXPONENT, "NumOfInputs":2})
        operations.append({"ID":"6", "Description":DESCRIPTION_SQUARE_ROOT, "NumOfInputs":1})
        operations.append({"ID":"7", "Description":DESCRIPTION_LAST_RESULT, "NumOfInputs":0})
        for elem in operations:
            print(elem["ID"] + ". " + elem["Description"])
        print("######################################")
        ids = [operation['ID'] for operation in operations]
        
        
        choice = input("Choose Operation (" + "/".join(ids) + ")  : ")

        if choice in ids:
            cindex = ids.index(choice)
            descriptions = [operation['Description'] for operation in operations]    
            num_inputs = [operation['NumOfInputs'] for operation in operations]
            cdescription = descriptions[cindex]
            cnum_input = num_inputs[cindex]

            print("<" + str(cdescription) + ">")
            num1, num2 = get_input_num(cnum_input)

            if cdescription == DESCRIPTION_ADD:
                result = add(num1, num2)
            elif cdescription == DESCRIPTION_SUBTRACT:
                result = subtract(num1, num2)
            elif cdescription == DESCRIPTION_MULTIPLY:
                result = multiply(num1, num2)
            elif cdescription == DESCRIPTION_DIVIDE:
                result = divide(num1, num2)
            elif cdescription == DESCRIPTION_EXPONENT:
                result = exponent(num1, num2)
            elif cdescription == DESCRIPTION_SQUARE_ROOT:
                result = square_root(num1)
            elif cdescription == DESCRIPTION_LAST_RESULT:
                result = last_result
            else:
                result = "None"
            print("Result : ", str(result))
            last_result = result
        else:
            print("Invalid input")

main()
