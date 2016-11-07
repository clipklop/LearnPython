#
def calc(string):
    string = string.lower().replace(" ", "")
    parts = string.split("+")

    for plus in range(len(parts)):
        if "-" in parts[plus]:
            parts[plus] = parts[plus].split("-")

    print(parts)

def precalc(part):
    if type(part) is str:
        if "*" in part:
            result = 1
            for subpart in part.split("*"):
                result *= float(subpart)
            return result

        if "/" in part:
            parts = part.split("/")

    return part


if __name__ == "__main__":
    calc("10 + 2 * 3 - 4 + 1 / 2")
    print(precalc("6*3"))