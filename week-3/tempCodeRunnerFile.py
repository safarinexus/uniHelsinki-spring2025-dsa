import re

def evaluate(data):
    if not data:
        return data

    # Precompiled regex patterns for add and mul
    add_pattern = re.compile(r'add\((\d+),(\d+)\)')
    mul_pattern = re.compile(r'mul\((\d+),(\d+)\)')

    def replace_add(match):
        num1, num2 = map(int, match.groups())
        return str(num1 + num2)

    def replace_mul(match):
        num1, num2 = map(int, match.groups())
        return str(num1 * num2)

    # Replace add and mul expressions in one pass
    data = add_pattern.sub(replace_add, data)
    data = mul_pattern.sub(replace_mul, data)

    return data
