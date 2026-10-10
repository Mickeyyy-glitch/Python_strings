
text = input().lower()

data = []
word = ''

for ch in text:
    if ch != ' ':
        word += ch
    else:
        if word:
            data.append(word)
        word = ''

if word:
    data.append(word)

freq = {}

for x in data:
    if x in freq:
        freq[x] += 1
    else:
        freq[x] = 1

sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=1)

print(sorted_freq[:5])
