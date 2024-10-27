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

    print(f'All even numbers in the range {a} and {b}: {is_even(a, b)}')

def is_the_biggest_check(a, b):
    a, b = (b, a) if a > b else (a, b)
    return a, b

def is_even(a, b):
    result = str()

    for i in range(a, b + 1):
        if i % 2 == 0:
            result += str(i) + ' '

    return result