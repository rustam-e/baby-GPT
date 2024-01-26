# read it to inspect it
with open('tinyshakespeare.txt', 'r', encoding="utf-8") as f:
    text = f.read()

chars = sorted(list(set(text)))

vocab_size = len(chars)

s_to_i = { ch:i for i, ch in enumerate(chars) }

i_to_s = { i:ch for i, ch in enumerate(chars) }

encode = lambda str: [s_to_i[c] for c in str] # encoder: take a string, output a list of integers
decode = lambda list: ''.join([i_to_s[i] for i in list]) # decoder: take a list of numbers, output a string

print(encode('Rustam'))
print(decode(encode('Rustam')))