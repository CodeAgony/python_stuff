def is_cool(name):
    return (name == "Joe") or (name == "Stephen") or (name == "John")

def test_if_cool(name):
    if is_cool(name):
        print(name, 'is cool')
    else:
        print(name, 'is not cool')


test_if_cool('Joe')
test_if_cool('Mike')
