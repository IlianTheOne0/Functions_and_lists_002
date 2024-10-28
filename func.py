def main():
    while True:
        try:
            number = int(input('Enter the number: '))
            break
        except Exception as e:
            print(f'Error: {e}')
            continue

    number = is_negative(number)

    print('Is this number a palindrome?:', is_palindrome(number))

def is_negative(number):
    return (number - (number * 2)) if number < 0 else number

def is_palindrome(number):
    result = ''
    original_value = number

    if len(str(original_value)) != 1:
        while number:
            digit = number % 10
            number //= 10

            result += str(digit)

        return int(result) == original_value
    else:
        return True