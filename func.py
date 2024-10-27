def main():
    while True:
        try:
            size = int(input('Size: '))
            symbol = input('Symbol: ')
            state = input('Filled or empty (True, False): ')

            if state not in ['True', 'False']:
                raise ValueError(f"invalid literal for bool(): '{state}'")
            break
        except Exception as e:
            print(f'Error: {e}')
            continue

    painter(size, symbol, state)

def painter(size, symbol, state):
    if state == 'True':
        for y in range(0, size):
            for x in range(0, size):
                print(symbol, end='  ')
            print()
    else:
        print((symbol + '  ') * size)

        for y in range(0, size - 2):
            print('*', end='  ')
            print('.  ' * (size - 2), end='')
            print('*', end='  ')
            print()

        print((symbol + '  ') * size)