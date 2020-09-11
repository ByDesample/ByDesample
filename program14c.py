
input_file = "banned_words.txt"

masking_char = '*'

banned_words = set()

with open(input_file, encoding='utf8') as fp:
    for line in fp:
        banned_words.add(line.strip().lower())

s = input("Enter sentence: ")

words = s.split()

for i, word in enumerate(words):
    if word.lower() in banned_words:
        words[i] = word[0] + masking_char * (int(len(word)) -1)

print(' '.join(words))