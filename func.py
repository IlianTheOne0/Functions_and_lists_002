def main():
    while True:
        try:
            a = int(input('Enter the first number: '))
            b = int(input('Enter the second number: '))
            break
        except Exception as e:
            print(f'Error: {e}')
            continue

    a, b = is_the_biggest_check(a, b)
    print(f'Product of numbers in the range {a} and {b}: {multiplication(a, b)}')

def is_the_biggest_check(a, b):
    a, b = (b, a) if a > b else (a, b)
    return a, b

def multiplication(a, b):
    result = 1

    for i in range(a, b + 1):
        result *= i

    return result