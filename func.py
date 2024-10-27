def main():
    try:
        a = int(input('Enter the first number: '))
        b = int(input('Enter the second number: '))

        print(is_even(a, b))
    except Exception as e:
        print(f'Error: {e}')

def is_even(a, b):
    result = str()

    for i in range(a, b + 1):
        if i % 2 == 0:
            result += str(i) + ' '

    return result