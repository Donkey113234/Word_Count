import collections
s = input("Enter a sentence:")
c = collections.Counter(s)
print(s)

for letter,count in sorted(c.items()) :
    print('{letter}:{count}'.format(letter = letter, count = count))
