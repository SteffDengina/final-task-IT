def minus_skobki(text):
    while '(' in text and ')' in text:
        start = text.find('(')
        end = text.find(')', start)
        text = text[:start] + text[end+1:]
    return text

user_input = input("Поле для ввода текста с круглыми скобками: ")
result = minus_skobki(user_input)
print(result)