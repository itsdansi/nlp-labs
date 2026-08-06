# Q. Count how many times each word appears in a sentence.
text = "I like NLP I like Python NLP is fun"


from collections import Counter

words = text.split()
# word_count = Counter(words)

word_count = {}

for w in words:
    if w in word_count:
        word_count[w] += 1
    else:
        word_count[w] = 1
        
print(word_count)