def vol(x):
    if (type(x) is str):
        return "Numbers only"

    if (x <= 0):
        return "Positive numbers only"

    return x * x * x
