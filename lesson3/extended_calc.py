# **
# An advanced calculator.
# **


def calculator(string):
    """Main calculator function."""
    try:
        string = string.replace(' ', '')
        parts = string.split("+")

        for plus in range(len(parts)):
            if '-' in parts[plus]:
                parts[plus] = parts[plus].split('-')
        print(parts)

        for plus in range(len(parts)):
            parts[plus] = precalc(parts[plus])
        print(parts)

        result = sum(parts)
    except ValueError:
        result = 'Something goes wrong.'
    except ZeroDivisionError:
        result = "Don't break the university."
    return result


def precalc(part):
    """Split and calculate nested integers in a list by its operand."""
    if type(part) is str:
        if '*' in part:
            result = 1
            for subpart in part.split('*'):
                result *= precalc(subpart)
            return result
        elif '/' in part:
            parts = list(map(precalc, part.split("/")))
            result = parts[0]
            for subpart in parts[1:]:
                result /= subpart
            return result
        else:
            return float(part)
    elif type(part) is list:
        for i in range(len(part)):
            part[i] = precalc(part[i])
        return part[0] - sum(part[1:])

    return part


if __name__ == "__main__":
    print(calculator("3 / 2 + 10 + 2 * 3 * 2.5 - 4 + 1 / 2"))