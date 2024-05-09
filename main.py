import math
import inspect

INPUT_ERROR = "<Input Error> "
DO_UNIT_TEST = True

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

print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Exponent")
print("6. Square Root")

while True:
    choice = input("Enter choice (1/2/3/4/5/6): ")

    if choice in ('1', '2', '3', '4', '5', '6'):
        num1 = float(input("Enter first number: "))

        if choice != '6':
            num2 = float(input("Enter second number: "))

        if choice == '1':
            print("Result:", add(num1, num2))
        elif choice == '2':
            print("Result:", subtract(num1, num2))
        elif choice == '3':
            print("Result:", multiply(num1, num2))
        elif choice == '4':
            print("Result:", divide(num1, num2))
        elif choice == '5':
            print("Result:", exponent(num1, num2))
        elif choice == '6':
            print("Result:", square_root(num1))
    else:
        print("Invalid input")


