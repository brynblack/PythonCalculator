operators = {
    '!=': ((lambda x, y: float(eval(x)) != float(eval(y))), 'Not equal'),
    '>=': ((lambda x, y: float(eval(x)) >= float(eval(y))), 'Greater than or equal to'),
    '<=': ((lambda x, y: float(eval(x)) <= float(eval(y))), 'Less than or equal to'),
    '=': ((lambda x, y: float(eval(x)) == float(eval(y))), 'Equal to'),
    '>': ((lambda x, y: float(eval(x)) > float(eval(y))), 'Greater than'),
    '<': ((lambda x, y: float(eval(x)) < float(eval(y)), 'Less than'))
}
arithmetic_operators = {
    '/': 'Division',
    '*': 'Multiplication',
    '+': 'Addition',
    '-': 'Subtraction',
    '**': 'Exponentiation',
    '%': 'Modulus',
    '//': 'Floor division'
}

print('PyCalc v2.0.0')
while True:
    inputString = input('Please input your equation (Type help for help): ').replace(' ', '').lower()
    if inputString == 'exit':
        break
    if inputString == 'help':
        print('List of available boolean operators:')
        for operator in operators:
            print(f'{operator}  {operators.get(operator)[1]}')
        print('\nList of available arithmetic operators:')
        for operator in arithmetic_operators:
            print(f'{operator}  {arithmetic_operators.get(operator)}')
        print()
        continue
    for operator in operators:
        if operator in inputString:
            partA, partB = inputString.split(operator, 1)
            try:
                print(f'{inputString}: {operators[operator][0](partA, partB)}\n')
            except (SyntaxError, ValueError, NameError, TypeError, ZeroDivisionError, OverflowError):
                print('Syntax Error!\n')
            break
    else:
        try:
            print(f'{inputString}: {eval(inputString)}\n')
        except (SyntaxError, ValueError, NameError, TypeError, ZeroDivisionError, OverflowError):
            print('Syntax Error!\n')
