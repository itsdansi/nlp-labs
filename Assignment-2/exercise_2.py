# Q2. Find all unique words in a corpus.

corpus = [
"I like NLP",
"I like AI",
"AI is amazing"
]

unique_vocabulary = set()
corpus_united = " ".join(corpus)
tokens = corpus_united.split()

for word in tokens:
    if word not in unique_vocabulary:
        unique_vocabulary.add(word)

vocabulary = sorted(unique_vocabulary)

print("Vocabulary")
for word in vocabulary:
    print(word)
print(f"Vocabulary Size = {len(vocabulary)}")

