def main():
    print('The lowest number is:', search_for_the_least(split(input('Enter numbers, separated by a space: '), ' ')))

def split(numbers, pattern):
    for number in pattern:
        numbers = numbers.replace(number, ' ')
    return numbers.split()

def search_for_the_least(numbers):
    lowest = numbers[0]

    for i in range(len(numbers) - 1):
        if numbers[i + 1] < lowest:
            lowest = numbers[i + 1]

    return lowest