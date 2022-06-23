def camel_case(string):
    return ''.join(string.title().split())


print(camel_case('hello world'))