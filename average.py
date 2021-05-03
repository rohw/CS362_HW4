def avg(arr):
    if type(arr) != list:
        return "It's not a list"
    elif (len(arr) == 0):
        return "It's an empty list"
    else:
        sum = 0
        for x in arr:
            sum += x
        return sum / len(arr)
