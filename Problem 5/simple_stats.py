
def simple_stats():
    num1 = float(input())
    num2 = float(input())
    num3 = float(input())
    num4 = float(input())

    product = num1 * num2 * num3 * num4
    average = (num1 + num2 + num3 + num4) /4

    print(f'{product:.0f}', round(average))
    print(f'{product:.3f}', f'{average:.3f}')


    ''' Type your code here. '''
if __name__ == "__main__":
    simple_stats()