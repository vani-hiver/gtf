s = input("Enter input here (combine all results from previous codes): ")
def convert(txt, key = "bee"):
    converted_text = ""

    if len(key) > len(txt): key = key[: len(txt)]
    elif len(key) < len(txt): key = (key * ((len(txt) // len(key)) + 1))[:len(txt)]

    for i in range(len(txt)):
        if txt[i].isupper(): v = 'A'
        elif txt[i].islower(): v = 'a'
        else:
            converted_text += txt[i]
            continue

        s = ord(key[i]) - ord(txt[i])
        if s < 0: s += 26
        converted_text += chr(s + ord(v))
    return converted_text
print("VISIT MEEEEEE ---------->     ", convert(s))
