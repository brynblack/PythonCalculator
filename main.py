operators = {
    '!=': (lambda x, y: float(eval(x)) != float(eval(y))),
    '>=': (lambda x, y: float(eval(x)) >= float(eval(y))),
    '<=': (lambda x, y: float(eval(x)) <= float(eval(y))),
    '=': (lambda x, y: float(eval(x)) == float(eval(y))),
    '>': (lambda x, y: float(eval(x)) > float(eval(y))),
    '<': (lambda x, y: float(eval(x)) < float(eval(y)))
}
arithmetic_operators = ['/', '*', '+', '-', '**', '%', '//']

while True:
    inputString = input('Please input your equation (Type help for help): ').replace(' ', '')
    if inputString == 'exit':
        break
    if inputString == 'help':
        print('PyCalc v1.0.0 - Help\nList of available boolean operators:')
        for op in operators:
            print(f'{op}')
        print('\nList of available arithmetic operators:')
        for op in arithmetic_operators:
            print(f'{op}')
    for operator in operators:
        if operator in inputString:
            partA, partB = inputString.split(operator, 1)
            try:
                print(f'{inputString}: {operators[operator](partA, partB)}\n')
            except (SyntaxError, ValueError, NameError, TypeError, ZeroDivisionError, OverflowError):
                print('Syntax Error!\n')
            break
    else:
        try:
            print(f'{inputString}: {eval(inputString)}\n')
        except (SyntaxError, ValueError, NameError, TypeError, ZeroDivisionError, OverflowError):
            print('Syntax Error!\n')
