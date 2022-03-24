import re
def seven_ate9(s):
    pattern = re.sub(r"(7{1})(9){1}(7{1})",'77', s)
    if '797' in pattern:
        return pattern.replace('797', '77')
    return pattern

a = '7979797'
print(seven_ate9(a))