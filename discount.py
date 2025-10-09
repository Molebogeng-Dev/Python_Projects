def calculate_discount(num1,num2):
    if num1 > 0 and num2 > 90:
        return float(num1 - (num1 * 90/100))
    elif num1 > 0 and num2 > 0:
        return float(num1 - (num1 * num2/100))
    raise(ValueError)

