def arithmetic(a, b, operator):
    operations = {
        'add': a+b, 
        'subtract': a-b,
        'divide': a/b,
        'multiply': a*b
    }
    return operations[operator]