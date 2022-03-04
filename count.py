Python 3.8.8 (tags/v3.8.8:024d805, Feb 19 2021, 13:18:16) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def word_count(str):
counts = dict()
words = str.split()
print(words)
for word in words:
if word in counts:
counts[word] += 1
else:
counts[word] = 1
return counts
print( word_count('the quick brown fox jumps over the lazy dog.'))