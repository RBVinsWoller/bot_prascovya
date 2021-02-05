def reverse(func):
    if func == 'sin':
        func = 'cos'
    elif func == 'cos':
        func = 'sin'
    elif func == 'tg':
        func = 'ctg'
    elif func == 'ctg':
        func = 'tg'