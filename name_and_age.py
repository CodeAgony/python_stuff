def name_and_age(name,age):
    if age >= 0:
        print("{} is {} years old".format(name, str(age)))
    else:
        print("Error: Invalid age")


name_and_age("Jane", 90)
