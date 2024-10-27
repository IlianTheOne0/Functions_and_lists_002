def main():
    try:
        size = int(input('Size: '))
        symbol = str(input('Symbol: '))
        state = bool(input('Filled or empty (True, False): '))
    except Exception as e:
        print(f'Error: {e}')

def painter(size, symbol, state):
    for i in range(0, 11):
        for j in range(0, 11):
            print('*', end='  ')
        print()