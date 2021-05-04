def full_n(first_name, last_name):
    if type(first_name) == str and type(last_name) == str:
        if len(first_name) == 0 or len(last_name) == 0:
            return "Input is empty string"
        name = first_name + " " + last_name
        return name
    else:
        return "Input must be string"
