def capitalize(text):
    text = text.split()
    text_with_capital = []
    for i in text:
        i = i.capitalize()
        text_with_capital.append(i)
    return text_with_capital


txt = input()
print(*capitalize(txt))