def is_vowel(a):
    if a in "ауоыиэяюёеАУОЫИЭЯЮЁЕ":
        return True


def pig_latin():
    word = input("Что скажешь?")
    output = []
    for a in word:
        if is_vowel(a):
            output.append("{}с{}".format(a, a.lower()))
        else:
            output.append(a)
    print(''.join(output))

pig_latin()
