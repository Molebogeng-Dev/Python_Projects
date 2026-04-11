def add_numbers(num, num2):
    return num + num2

def is_even(num):
    return True if num%2==0 else False

def reverse_string(text):
    reverse = [text[len(text) -1 - i] for i in range(len(text)) ]
    return ''.join(reverse) #return text[::-1]

def factorial(num):
    if num == 1 or num == 0:
        return 1
    
    elif num < 0:
        raise(ValueError)
    
    return num * factorial(num -1)

