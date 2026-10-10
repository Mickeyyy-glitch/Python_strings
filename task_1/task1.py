text = 'язык программирования Python'

word = ''
res = []

for i in range(len(text)):
    if text[i] != ' ':
        word += text[i]

    if text[i] == ' ' or i == len(text) - 1:
        res.append(word)
        word = ''

print(*res[::-1])

new_word = ''
new_res = []

for i in range(len(text)):
    if text[i] != ' ':
        new_word += text[i]

    if text[i] == ' ' or i == len(text) - 1:
        new_res.append(new_word[::-1])
        new_word = ''

print(*new_res[::-1])
