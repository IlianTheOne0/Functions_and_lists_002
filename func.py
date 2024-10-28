def main():
    while True:
        try:
            number = int(input('Enter the number: '))
            break
        except Exception as e:
            print(f'Error: {e}')
            continue

    result = len(spliter(is_negative(number)))

    print('The number of digits in a number:', 1 if result == 0 else result)

def is_negative(number):
    return (number - (number * 2)) if number < 0 else number

def spliter(number):
    result = []

    while number:
        digit = number % 10
        number //= 10

        result.append(digit)

    return result