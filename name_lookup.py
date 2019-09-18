def name_lookup(first_name):
    """Receives first name and returns corresponding second name"""
    if first_name == "Joe":
       return "Warren"
    elif first_name == "Scott":
        return "Rixner"
    elif first_name == "John":
        return "Greiner"
    elif first_name == "Stephen":
        return "Wong"
    else:
        return "Error: Not an instructor"


print(name_lookup("Scott"))