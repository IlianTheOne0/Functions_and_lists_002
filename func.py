def main():
    while True:
        try:
            a = int(input('Enter the first number: '))
            b = int(input('Enter the second number: '))
            break
        except Exception as e:
            print(f'Error: {e}')
            continue

    print(f'All even numbers in the range {a} and {b}: {is_even(a, b)}')

def is_even(a, b):
    result = str()

    for i in range(a, b + 1):
        if i % 2 == 0:
            result += str(i) + ' '

    return result