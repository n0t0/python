def print_side(side_end, side_filling, size, line_start=False, line_end=''):
    if line_start:
        print(side_end, end='')
    print(' ', end='')
    print(side_filling * size, end='')
    print(side_end, end=line_end)
 

def print_horizontal(x, side_lenght, params):
    for i in range(x - 1):
        if i == 0:
            print_side(*params, side_lenght, line_start=True)
        else:
            print_side(*params, side_lenght)
    print_side(*params, side_lenght, line_end='\n')


def print_vertical(x, side_lenght, params):
    for n in range(side_lenght):
        for i in range(x - 1):
            if i == 0:
                print_side(*params, side_lenght, line_start=True)
            else:
                print_side(*params, side_lenght)
        print_side(*params, size=side_lenght, line_end='\n')


def matrix(x=2, y=1, side_lenght=2, h_params=['+', '- '], v_params=['|', '  ']):
    for i in range(y):
        if i == 0:
            print_horizontal(x, side_lenght, h_params)
        print_vertical(x, side_lenght, v_params)
        print_horizontal(x, side_lenght, h_params)


matrix(4, 2, 4, ['*', '--'])
