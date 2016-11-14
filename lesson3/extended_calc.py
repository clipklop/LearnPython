#
def calc(string):
    string = string.lower().replace(" ", "")
    parts = string.split("+")

    for plus in range(len(parts)):
        if "-" in parts[plus]:
            parts[plus] = parts[plus].split("-")

    print(parts)

    for plus in range(len(parts)):
        parts[plus] = precalc(parts[plus])

    print(parts)

def precalc(part):
    if type(part) is str:
        if "*" in part:
            result = 1
            for subpart in part.split("*"):
                result *= float(subpart)
            return result
        elif "/" in part:
            parts = list(map(float, part.split("/")))
            result = parts[0]
            for subpart in parts[1:]:
                result /= subpart
            return result
        else:
            return float(part)
    elif type(part) is list:
        for i in range(len(part)):
            part[i] = precalc(part[i])
    return part


if __name__ == "__main__":
    calc("3 / 2 + 10 + 2 * 3 * 2.5 - 4 + 1 / 2")
    print(precalc("6*3"))
    print(precalc("1/2"))