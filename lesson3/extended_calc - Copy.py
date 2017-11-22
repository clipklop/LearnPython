# **
# An advanced calculator.
# **


# main calculator function
def calculator(string):
    string = string.replace(' ', '')
    parts = string.split("+")

    for plus in range(len(parts)):
        if '-' in parts[plus]:
            parts[plus] = parts[plus].split('-')
       

    print(parts)


def precalc(part):
    """"""
    if type(part) is str:
        if '*' in part:
            result = 1
            for subpart in part.split('*'):
                result *= float(subpart)
            return result
    return part

if __name__ == "__main__":
    calculator("10 + 2 * 3 * 2.5 - 4 + 1 / 2")
    print(precalc("2 * 3*0.5"))