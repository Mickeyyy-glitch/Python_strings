
from string import ascii_lowercase


alp = ascii_lowercase
text = input()
# After school, Jack went home, ate dinner, and watched a movie.
word = ''
res = []

for ch in text:
    if ch != ' ' and ch != ',' and ch != '.':
        word += ch

    if ch == ' ' or ch == ',' or ch == '.':
        if word:
            res.append(word)

        word = ''

K = len(max(res, key=len))

ans = ''

for ch in text:
    if ch.lower() in alp:
        for i in range(len(alp)):
            if alp[i] == ch.lower():
                if ch == ch.upper():
                    new_word = alp[(i + K) % 26].upper()
                else:
                    new_word = alp[(i + K) % 26]
                break

        ans += new_word

    else:
        ans += ch

print(ans)
print(K)
