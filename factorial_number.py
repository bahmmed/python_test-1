v_given_number=int(input("Enter Positive integer for factorial: "))
def cal_factorial(v_given_number):
    if v_given_number < 0:
        return "Factorial is not defined for negative numbers."
    elif v_given_number == 0 or v_given_number == 1:
        return 1
    else:
        result = 1
        while v_given_number > 1:
            result *= v_given_number
            v_given_number -= 1
        return result

cal_factorial(0)
factorial_result = cal_factorial(v_given_number)
print(f"The factorial of {v_given_number} is {factorial_result}")
