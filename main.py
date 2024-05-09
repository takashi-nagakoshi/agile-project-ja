import math
DO_UNIT_TEST = True

INPUT_ERROR             = "<Input Error> "
DESCRIPTION_ADD         = "Add         : x1 + x2"
DESCRIPTION_SUBTRACT    = "Subtract    : x1 - x2"
DESCRIPTION_MULTIPLY    = "Multiply    : x1 * x2"
DESCRIPTION_DIVIDE      = "Divide      : x1 / x2"
DESCRIPTION_EXPONENT    = "Exponent    : x1^x2"
DESCRIPTION_SQUARE_ROOT = "Square Root : sqrt(x1)"
DESCRIPTION_LAST_RESULT = "Show the last result value"

# [add]__________________________________________________________________________________________________________
def add(num1, num2):
    return num1 + num2

def test_add():
    assert add(5, 3) == 8
    assert add(-5, 3) == -2
    assert add(0, 0) == 0

# [subtract]_____________________________________________________________________________________________________
def subtract(num1, num2):
    return num1 - num2

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(-5, 3) == -8
    assert subtract(0, 0) == 0

# [multiply]_____________________________________________________________________________________________________
def multiply(num1, num2):
    return num1 * num2

def test_multiply():
    assert multiply(5, 3) == 15
    assert multiply(-5, 3) == -15
    assert multiply(0, 0) == 0

# [divide]_______________________________________________________________________________________________________
def divide(num1, num2):
    return

def test_divide():
    return

# [exponent]_____________________________________________________________________________________________________
def exponent(num1, num2):
    return

def test_exponent():
    return

# [square root]__________________________________________________________________________________________________

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

# [main関数と付属関数]______________________________________________________________________________________________

def main(last_result):
    # 「Operation」の一覧を表示し，また「Operation」のdictionaryを作成する．
    print("\n########### Operation list ###########")
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
    
    # ユーザーに「Operation」を選択してもらう．
    choice = input("Choose Operation (" + "/".join(ids) + ")  : ")

    # 選択された「Operation」に応じた処理を行う．
    if choice in ids:
        # 前処理
        cindex = ids.index(choice)
        descriptions = [operation['Description'] for operation in operations]    
        num_inputs = [operation['NumOfInputs'] for operation in operations]
        cdescription = descriptions[cindex]
        cnum_index = num_inputs[cindex]

        # Mode表示と同時にユーザに数値を入力してもらう．
        print("<" + str(cdescription) + ">")
        num1, num2 = get_input_num(cnum_index, last_result)

        # 選択された「Operation」に応じた関数をcallする．
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
    else:
        print("Invalid input")
        result = last_result
    return result

def get_input_num(num_of_required_input, last_result):
    num1 = "None" # 0で初期化してもいいが，うっかり初期値のまま計算が継続しないようstrで初期化しておく．
    num2 = "None"

    if num_of_required_input >= 1:
        num1 = request_user_to_specify_num("x1", last_result)
    if num_of_required_input >= 2:
        num2 = request_user_to_specify_num("x2", last_result)
    return num1, num2

def request_user_to_specify_num(name_of_value, last_result):
    msg_of_last = "last"
    while True:
        num = input("Enter " + name_of_value + " value (type '" + msg_of_last + "' to use the last result) \n: ")
        if num == msg_of_last: 
            convert_success, result = convert_to_float(last_result)
            if convert_success:
                return result
            else:
                print("Cannot use tha last result. Please input different value.")
        else:
            convert_success, result = convert_to_float(num)
            if convert_success:
                return result
            else:
                print("Invalid input. Please input again")

def convert_to_float(num):
    try:
        result = float(num)
        return True, result
    except ValueError:
        return False, "None"

# [Unit test関数を集約してcallする]________________________________________________________________________________

def unit_test_aggregation():
    test_add()
    test_subtract()
    test_multiply()
    test_divide()
    test_exponent()
    test_square_root()
    return

# [関数実行]______________________________________________________________________________________________________
if __name__ == "__main__":
    if DO_UNIT_TEST:
        unit_test_aggregation()

    last_result = "None"
    while True:
        # unit_testが書きやすいよう，while文の中の処理は独立関数とする．
        result = main(last_result) 
        last_result = result

